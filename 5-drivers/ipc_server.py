from multiprocessing import shared_memory
import struct 
import time 
import random 

SHM_NAME = "minha_memoria_zero_copy"
MSG_FORMAT = "=id" 
MSG_SIZE = struct.calcsize(MSG_FORMAT)

def start_ipc_server():
    print(f"[*] INICIANDO O IPC SERVER...")
    try: 

        shm = shared_memory.SharedMemory(name=SHM_NAME, create=True, size=MSG_SIZE)
        print(f"[OK] Memoria {SHM_NAME} alocada.")
        
        msg_id = 0
        try: 
            while True:
                msg_id += 1
                valor_simulado = random.uniform(10.0, 100.0)
                
               
                struct.pack_into(MSG_FORMAT, shm.buf, 0, msg_id, valor_simulado)
              
                time.sleep(0.001) 
        except KeyboardInterrupt:
            print("\n[!] Interrompido pelo usuario.")
            
    except FileExistsError:
        print(f"[ERRO] A memoria {SHM_NAME} ja existe. Use um script de limpeza.")
    finally:
        if 'shm' in locals():
            shm.close()
            shm.unlink() 
            print("[*] Memoria desalocada.")

if __name__ == "__main__":
    start_ipc_server()
