import os
import sys
from pydantic import BaseModel, ConfigDict


 def auditar


class SchemaSecure(BaseModel): 
    
    model_config = ConfigDict(slots=True, frozen=True)
    
    
    ip_origem: int
    severidade: int 
    timestamp: float 
    
    ev = SchemaSecure(ip_origem=3232235521, severidade =5, timestamp=171163400.0)
    print(f"Objeto alocado. Tamanho: {sys.getsizeof(ev)} bytes.")
    
    
    
    
class SchemaValidator:
    def __init__(self):
        self.x = 1

class SchemaInitial:
    __slots__ = ['x']
    def __init__(self):
        self.x = 1


validator = SchemaValidator()
initial = SchemaInitial()

print(f"PID: {os.getpid()}")
print(f"ID validator (Gordo): {hex(id(validator))}")
print(f"ID initial (Squeezed): {hex(id(initial))}")

input("Anexe  e pressione Enter...")


class SchemaMediator: 
    __slots__ = ['conteudo']
    def __init__(self, valor):
        self.conteudo = valor
        
        def __del__(self):
            
            print(">>> Aviso: Memória do dado sensível foi sobreescrita e liberada.")
            
    def processar_segredo():
        segredo = DadoSensivel("CHAVE_CRIPTOGRÁFICA_X")
        print(f"Objeto vivo do endereço: {hex(id(segredo))}")
        
        
        processar_segredo()
        
        
        gc.collect()
        print("Fluxo finalizado.")
