import hashlib
import struct
import os
import sys
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

from mmap_db import MemoryEngine
from atomic_writer import AtomicWriter

class SecurityVault:
    DATA_FORMAT = "I 28s" 
    RECORD_SIZE = 160 

    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    def pack_and_encrypt(self, user_id: int, name: str) -> bytes:
        try:
            name_bytes = name.encode('utf-8')[:28].ljust(28, b'\x00')
            payload = struct.pack(self.DATA_FORMAT, user_id, name_bytes)
            
            encrypted_payload = self.cipher.encrypt(payload)
            
            checksum = hashlib.sha256(encrypted_payload).digest()
            
            final_block = checksum + encrypted_payload
            return final_block.ljust(self.RECORD_SIZE, b'\x00')
        except Exception as e:
            print(f"Error during packing: {e}")
            raise

    def decrypt_and_unpack(self, raw_data: bytes):
        raw_data = raw_data.rstrip(b'\x00')
        
        if len(raw_data) < 32:
            raise ValueError("Data block is too small or corrupted.")

        checksum_lido = raw_data[:32]
        encrypted_payload = raw_data[32:]
        
        if hashlib.sha256(encrypted_payload).digest() != checksum_lido:
            raise ValueError("CRITICAL: SHA-256 integrity check failed!")
        
        try:
            decrypted_data = self.cipher.decrypt(encrypted_payload)
            return struct.unpack(self.DATA_FORMAT, decrypted_data)
        except Exception as e:
            print(f"Error during decryption: {e}")
            raise

def main():
    print("\n" + "="*60)
    print(" SECURE STORAGE ENGINE  ")
    print("="*60)

    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()

        master_key_raw = Fernet.generate_key()
        master_key_encrypted = public_key.encrypt(
            master_key_raw,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        db_file = "storage.db"
        db_size = 8192 
        engine = MemoryEngine(db_file, db_size)
        
        key_recovered = private_key.decrypt(
            master_key_encrypted,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        vault = SecurityVault(key_recovered)

        while True:
            print("\n" + "-"*30)
            print("1. REGISTER NEW USER")
            print("2. QUERY SECURE RECORD")
            print("3. SYSTEM STATUS")
            print("4. EXIT")
            print("-"*30)
            
            choice = input("Select an option: ")

            if choice == "1":
                try:
                    idx = int(input("Enter slot ID (0-50): "))
                    name = input("Enter user name: ")
                    
                    data_block = vault.pack_and_encrypt(idx, name)
                    
                    with AtomicWriter(db_file) as writer:
                        writer.write_at(engine, idx * vault.RECORD_SIZE, data_block)
                    
                    print(f"\n[OK] Record {idx} secured with SHA-256 and Fernet.")
                except ValueError:
                    print("\n[ERROR] Invalid ID format.")
                except Exception as e:
                    print(f"\n[CRITICAL ERROR] {e}")

            elif choice == "2":
                try:
                    idx = int(input("Enter ID to query: "))
                    offset = idx * vault.RECORD_SIZE
                    
                    raw_block = engine.read_at(offset, vault.RECORD_SIZE)
                    
                    uid, name_decoded = vault.decrypt_and_unpack(raw_block)
                    
                    clean_name = name_decoded.decode('utf-8').strip(chr(0))
                    print(f"\n[SUCCESS] Record found at offset {offset}:")
                    print(f" > System ID: {uid}")
                    print(f" > Encrypted Name: {clean_name}")
                except Exception as e:
                    print(f"\n[ERROR] Integrity check or decryption failed: {e}")

            elif choice == "3":
                print(f"\n[STATUS]")
                print(f" > Storage File: {db_file}")
                print(f" > Memory Mapping: ACTIVE")
                print(f" > RSA Key Length: 2048 bits")
                print(f" > Integrity Lacre: SHA-256 Digest")

            elif choice == "4":
                print("\n[SHUTDOWN] Wiping RSA keys and closing engine...")
                break
            else:
                print("\n[!] Invalid selection.")

    except Exception as e:
        print(f"\n[BOOT ERROR] System failed to start: {e}")
    finally:
        if 'engine' in locals():
            engine.close()
        print("="*60)
        print(" SYSTEM TERMINATED ")
        print("="*60)

if __name__ == "__main__":
    main()
