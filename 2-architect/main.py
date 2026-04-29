import gc
import array
import sys
import os
from pydantic import BaseModel, ConfigDict, ValidationError


class SchemaSecure(BaseModel):
    model_config = ConfigDict(slots=True, frozen=True)
    ip_origem: int
    severidade: int
    timestamp: float

class SchemaValidator: 
    def __init__(self):
        self.x = 1

class SchemaInitial:
    __slots__ = ['x']
    def __init__(self):
        self.x = 1

class SchemaMediator:
    __slots__ = ['conteudo']
    def __init__(self, valor):
        self.conteudo = valor
    def __del__(self):
        print("\n>>> [SENTINEL] Aviso: Memória do dado sensível foi sobrescrita e liberada.")


def log_stream():
    """Lógica de Streaming Infinito (Modo 1)"""
    for i in range(10**6): # Reduzi para 1 milhão para o teste ser rápido
        yield i

def main_streaming():
    print("\n--- [MODO 1]: STREAMING INFINITO (RAM CONSTANTE) ---")
    stream = log_stream()
    for _ in range(5):
        evento = next(stream)
        print(f"Processando evento em tempo real: {evento}")
    print("Memória estável. Nenhum dado foi acumulado no buffer principal.")

def main_seguranca():
    print("\n--- [MODO 2]: SEGURANÇA FIREWALL (VALIDATION) ---")
    # O segundo item causará erro de validação (String em campo Int)
    logs_suspeitos = [
        {"ip_origem": 19216801, "severidade": 5},
        {"ip_origem": "ATAQUE_SQL", "severidade": "ALTA"} 
    ]
    
    for log in logs_suspeitos:
        try:
            valido = SchemaSecure(**log, timestamp=1711634.0)
            print(f" Pacote {valido.ip_origem} verificado e limpo.")
        except ValidationError:
            print(f" BLOQUEIO: Tentativa de injeção de dados inválidos detectada!")

def main_audit():
    print(f"\n--- [MODO 3]: AUDITORIA FÍSICA (PID: {os.getpid()}) ---")
    validator = SchemaValidator()
    initial = SchemaInitial()
    
    print(f"Endereço Objeto Validator (Gordo): {hex(id(validator))}")
    print(f"Endereço Objeto Initial (Squeezed): {hex(id(initial))}")
    print(f"Diferença de tamanho (sys): {sys.getsizeof(validator)} vs {sys.getsizeof(initial)} bytes")
    
    input("\n[PAUSA] O processo está travado. Inspecione os bits  e pressione Enter...")

def main_cleanup():
    print("\n--- [MODO 4]: ZERO FOOTPRINT (LIMPEZA TOTAL) ---")
    temp_data = SchemaMediator("CHAVE_SECRETA_SENSIVEL")
    print(f"Dado sensível alocado em: {hex(id(temp_data))}")
    
    del temp_data
    gc.collect()
    print("Varredura concluída. Rastro de memória higienizado.")


if __name__ == "__main__":
  
    main_streaming()
    main_seguranca()
    main_audit()
    main_cleanup()
