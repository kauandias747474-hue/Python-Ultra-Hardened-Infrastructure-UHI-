import asyncio
import mmap
import sys
from schema import IndustrialData, DoubleBuffer, RECORD_SIZE

async def run_scraper_logic():
    """Conecta na RAM pelo nome e escreve dados simulados em 100Hz."""
    try:
       
        shared_mem = mmap.mmap(-1, 32000, tagname="UHI_RAM_GLOBAL", access=mmap.ACCESS_WRITE)
        db = DoubleBuffer(shared_mem, 1000)
        counter = 0
        
        while True:
           
            temp_fake = 25.0 + (counter % 45)
            press_fake = 101.3 + (counter % 5)
            
            obj = IndustrialData(sensor_id=1, temp=temp_fake, press=press_fake)

            offset = db.get_offset(obj.sensor_id, mode="write")
            shared_mem[offset : offset + RECORD_SIZE] = obj.pack()
            
            counter += 1
         
            await asyncio.sleep(0.01)
            
    except Exception as e:
        print(f"❌ [SCRAPER ERROR] Falha na conexão com a RAM: {e}")

def scraper_worker():
    """Ponto de entrada para o processo filho."""
    try:
        asyncio.run(run_scraper_logic())
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    pass
