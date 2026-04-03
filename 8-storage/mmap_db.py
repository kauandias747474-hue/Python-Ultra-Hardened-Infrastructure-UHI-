import mmap
import os

class MemoryEngine:
    def __init__(self, filename: str, size: int):
        self.filename = filename
        self.size = size
        self._initialize_file(size)
        self._map_memory()

    def _initialize_file(self, size):
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) < size:
            with open(self.filename, "wb") as f:
                f.write(b"\x00" * size)
                f.flush()

    def _map_memory(self):
        self.file = open(self.filename, "r+b")
        self.mm = mmap.mmap(self.file.fileno(), length=self.size, access=mmap.ACCESS_WRITE)

    def _expand_file(self, required_size):
      
        new_size = (required_size // 4096 + 1) * 4096
        self.mm.close()
        self.file.close()
        
        with open(self.filename, "r+b") as f:
            f.truncate(new_size)
        
        self.size = new_size
        self._map_memory()

    def write_at(self, offset: int, data: bytes):
        end = offset + len(data)
        if end > self.size:
            self._expand_file(end)
            
        self.mm[offset:end] = data
        self.mm.flush()

    def read_at(self, offset: int, length: int) -> bytes:
        if offset + length > self.size:
            return b"\x00" * length
        return self.mm[offset : offset + length]

    def close(self):
        if hasattr(self, 'mm'): self.mm.close()
        if hasattr(self, 'file'): self.file.close()
