import os
import hashlib

class AtomicWriter:
    def __init__(self, target_file: str):
        self.target_file = target_file

    def __enter__(self):
        return self

    def _generate_backup_hash(self, data):
        return hashlib.sha256(data).hexdigest()

    def write_at(self, engine, offset: int, data: bytes):
       
        engine.write_at(offset, data)
    
        temp_name = self.target_file + ".tmp"
        try:
            with open(temp_name, "wb") as f:
                engine.mm.seek(0)
                current_state = engine.mm.read()
                f.write(current_state)
                f.flush()
                os.fsync(f.fileno()) 
            
            
            os.replace(temp_name, self.target_file)
            
        except Exception as e:
            if os.path.exists(temp_name):
                os.remove(temp_name)
            raise RuntimeError(f"Falha crítica na escrita atômica: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
