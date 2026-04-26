import time
import mmap
from schema import IndustrialData, DoubleBuffer, RECORD_SIZE

def controller_worker_logic():
    """Conecta na RAM e faz a gestão da sincronia dos buffers."""
    try:
     
        shared_mem = mmap.mmap(-1, 32000, tagname="UHI_RAM_GLOBAL", access=mmap.ACCESS_WRITE)
        db = DoubleBuffer(shared_mem, 1000)
        
        while True:
            t_start = time.perf_counter()

            offset = db.get_offset(1, mode="read")
            raw_bytes = shared_mem[offset : offset + RECORD_SIZE]
            data = IndustrialData.unpack(raw_bytes)
            
            db.swap()
            
            elapsed = time.perf_counter() - t_start
            time.sleep(max(0, 0.1 - elapsed))
            
    except Exception as e:
        print(f" [CONTROLLER ERROR] Erro de sincronia: {e}")

def controller_worker():
    """Ponto de entrada chamado pelo Sentinel."""
    try:
        controller_worker_logic()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    pass
