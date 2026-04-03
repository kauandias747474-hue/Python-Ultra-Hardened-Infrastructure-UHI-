import struct
import mmap
import os
import hashlib

class BinaryStreamer:
    def __init__(self, filename, size=1024*1024):
        if not os.path.exists(filename):
            with open(filename, "wb") as f:
                f.write(b'\x00' * size)
        
        self.f = open(filename, "r+b")
        self.map = mmap.mmap(self.f.fileno(), size)
        
    def generate_checksum(self, data: bytes) -> bytes:
        return hashlib.md5(data).digest()

    def pack_fixed_data(self, record_id: int) -> bytes:
        return struct.pack('>I', record_id)

    def write_at(self, offset: int, data: bytes):
        self.map[offset:offset+len(data)] = data
        
    def close(self):
        if self.map:
            self.map.close()
        if self.f:
            self.f.close()
