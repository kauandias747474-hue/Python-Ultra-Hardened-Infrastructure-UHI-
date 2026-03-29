import time 
import threading 
import signal
import sys
import gc

class LogicGate:
    def __init__(self):
        self._state = "IDLE"
        self._lock = threading.Lock()
        
    def transit(self, next_state):
        """Transição Atômica com Verbose de Thread"""
        with self._lock:
            thread_name = threading.current_thread().name
            print(f"[{thread_name}] Lock adquirido. Movendo: {self._state} -> {next_state}")
            
            # Simula latência de processamento de Kernel
            time.sleep(0.2) 
            
            self._state = next_state
            print(f"[{thread_name}] Transição completa. Estado: {self._state}")

def hard_reset():
    """Limpeza profunda de memória (Anti-Forensics)"""
    print("[*] Executando Hard Reset de memória...")
    gc.collect() 
    print("[*] RAM higienizada.")

def handle_interrupt(signum, frame):
    """Intercepta sinais do sistema (SIGINT/SIGTERM)"""
    print(f"\n[!] Sinal {signum} detectado. Abortando com segurança...")
    hard_reset()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

if __name__ == "__main__":
    gate = LogicGate()
    
    workers = [
        threading.Thread(target=gate.transit, args=(f"SEC_LEVEL_{i}",), name=f"Auth-Worker-{i}")
        for i in range(5)
    ]

    print("[SYSTEM] Sentinel Logic Gate Online. Pressione Ctrl+C para abortar.")
    
    for w in workers: w.start()
    for w in workers: w.join()
    
    print(f"[FINAL STATE] Registro em RAM: {gate._state}")
    hard_reset() 
