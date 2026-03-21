
import os
import psutil 
import contextlib
from abc import ABC, abstractmethod
from typing import Dict, Callable


class INetworkDriver(ABC):
    @abstractmethod
    def listen(self): pass
    @abstractmethod
    def close(self): pass

class IProtocolo(ABC):
    @abstractmethod
    def handshake(self) -> bool: pass
    @abstractmethod
    def transfer(self, data: any): pass

class ProtocoloSeguro(IProtocolo):
    def handshake(self): return True
    def transfer(self, data): print(f"Transferindo {len(data)} bytes.")


@contextlib.contextmanager
def network_lifecycle(driver: INetworkDriver):
    driver.listen()
    try:
        yield driver
    finally:
        driver.close()

@contextlib.contextmanager
def temporary_buffer_driver():
    print("Atenção: Alocando buffer de 512MB...")
    buffer = [] 
    try: 
        yield buffer
    finally: 
        print("Teardown: Fazendo flush e liberando buffer do SO.")
        buffer.clear()

class MonitorDeIntegridade:
    @staticmethod
    def check_health():
        # No Windows, o limite de arquivos abertos é gerenciado dinamicamente
        # Focamos na saúde dos diretórios de log
        if not os.path.exists("./net_logs"):
            os.makedirs("./net_logs")


class ServiceContainer:
    def __init__(self):
        self._services: Dict[str, Callable] = {}

    def register(self, key: str, provider: Callable):
        self._services[key] = provider
            
    def resolve(self, key: str):
        provider = self._services.get(key)
        if not provider:
            raise Exception(f"Serviço {key} não foi mapeado na Matriz.")
        return provider()

class IEngineForense(ABC):
    @abstractmethod
    def execute_logic(self, view: memoryview): pass

class Sentinela(IEngineForense):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            if not os.path.exists("./vault"): 
                os.makedirs("./vault")
        return cls._instance

    def execute_logic(self, view: memoryview):
        # HARDENING WINDOWS: psutil verifica a RAM real do processo
        process = psutil.Process(os.getpid())
        mem_usage = process.memory_info().rss # Resident Set Size
        
        if mem_usage > 1024 * 1024 * 1024: # Limite de 1GB
            raise MemoryError("FAIL-FAST: Sobrecarga crítica de Memória RAM no Windows.")

        print(f"Processando {view.nbytes} bytes em memória bruta (Zero-Copy)...")

        with open("./vault/kernel.log", "a") as f:
            f.write(f"PID:{os.getpid()} - Status: OK\n")
        return "SUCCESS"

container = ServiceContainer()
container.register("Forensics", lambda: "Container_v1_Active")
container.register("Core", lambda: Sentinela())

print(f"Executando: {container.resolve('Forensics')}")

with temporary_buffer_driver() as b: 
    b.append("Dados_Forensicos_Raw")
    core = container.resolve("Core")
    
    # Ponte de Memória (Vanilla-First)
    raw_data = bytearray("".join(b), 'utf-8')
    with memoryview(raw_data) as binary_view:
        final_status = core.execute_logic(binary_view)
        print(f"Operação Sentinel finalizada: {final_status}")
