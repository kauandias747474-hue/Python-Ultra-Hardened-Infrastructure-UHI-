import threading
import time
import random
from metrics_exporter import run_exporter # Importando do arquivo com T

def monitor_perf(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try: return func(*args, **kwargs)
        finally: pass
    return wrapper

@monitor_perf
def heavy_task():
    """Loop que gera carga e 'trava' o terminal propositalmente."""
    print("[-] Engine operacional: Gerando carga de CPU...")
    while True:
        _ = [x**2 for x in range(10000)]
        time.sleep(random.uniform(0.1, 0.3))

if __name__ == "__main__":
    print("=== SISTEMA DE TELEMETRIA INICIADO ===")
    
    # 1. INICIAR O SITE PRIMEIRO (Numa via paralela/Thread)
    try:
        # Usamos daemon=True para o site fechar se você fechar o programa
        t = threading.Thread(target=run_exporter, args=(8000,), daemon=True)
        t.start()
        time.sleep(1) # Dá 1 segundo para o servidor 'subir' antes da carga
    except Exception as e:
        print(f"[!] Erro ao ligar o site: {e}")

    # 2. INICIAR A CARGA DEPOIS
    try:
        heavy_task()
    except KeyboardInterrupt:
        print("\n[!] Encerrando...")
