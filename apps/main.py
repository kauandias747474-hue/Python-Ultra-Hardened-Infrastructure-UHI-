import mmap
import os
import multiprocessing
import time
import sys

from schema import RECORD_SIZE
import fast_scraper
import industrial_controller

class ProcessSentinel:
    """Monitora os processos e garante que eles nunca fiquem offline."""
    def __init__(self, target, name):
        self.target = target
        self.name = name
        self.process = None

    def spawn(self):
        """Inicia o processo sem passar o objeto mmap por argumento (Evita WinError 87)."""
        self.process = multiprocessing.Process(target=self.target, name=self.name, daemon=True)
        self.process.start()
        print(f"✅ [SENTINEL] {self.name} ATIVADO (PID: {self.process.pid})")

    def keep_alive(self):
        """Verifica a saúde do processo e reinicia se necessário."""
        if self.process is None or not self.process.is_alive():
            print(f"⚠️ [ALERTA] {self.name} parou de responder! Reiniciando unidade...")
            self.spawn()

def setup_ram_global():
    """Cria o arquivo físico e a seção de memória compartilhada nomeada."""
    FILE = "data.bin"

    TOTAL_SIZE = 1000 * 16 * 2 

    if os.path.exists(FILE):
        try:
            os.remove(FILE)
        except OSError:
            print("❌ ERRO: O arquivo data.bin está sendo usado. Feche outros terminais.")
            sys.exit(1)

    with open(FILE, "wb") as f:
        f.write(b"\x00" * TOTAL_SIZE)
        f.flush()

    fd = open(FILE, "r+b")
  
    mem = mmap.mmap(fd.fileno(), 0, tagname="UHI_RAM_GLOBAL", access=mmap.ACCESS_WRITE)
    return fd, mem

if __name__ == "__main__":
    
    multiprocessing.freeze_support()
    
    print("-" * 50)
    print("🚀 INICIALIZANDO NÚCLEO UHI - CONEXÃO INTEGRAL")
    print("-" * 50)

   
    f_handle, shared_memory = setup_ram_global()
    print("🧠 [MAIN] Memória Compartilhada Criada (Tag: UHI_RAM_GLOBAL).")

 
    s_scraper = ProcessSentinel(fast_scraper.scraper_worker, "UNIDADE_SCRAPER")
    s_controller = ProcessSentinel(industrial_controller.controller_worker, "UNIDADE_CONTROLE")
    
    
    s_scraper.spawn()
    s_controller.spawn()

    print("\n🛰️ SISTEMA TOTALMENTE OPERACIONAL")
    print("🛑 Pressione CTRL+C para encerrar o núcleo.\n")

    try:
        while True:
          
            s_scraper.keep_alive()
            s_controller.keep_alive()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n\n🛑 [SHUTDOWN] Desligando hardware e liberando RAM...")
    finally:
        shared_memory.close()
        f_handle.close()
        print("✅ [OFFLINE] Sistema encerrado com sucesso.")
