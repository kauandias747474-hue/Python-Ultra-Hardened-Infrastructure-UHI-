import array 
import sys 
import struct
from pydantic import BaseModel, ConfigDict, Field
from collections import deque

monitor_de_trafego = deque(maxlen=3)

for i in range(1,6):
    monitor_de_trafego.appen(f"LOG_EVENTO_{i}")
    print(f"Estado do Buffer (Máximo 3): {list(monitor_de_trafego)}")
    
    print(f"Tamanho disponível na RAM: {sys.getsizeof(monitor_de_trafego)} bytes")

formato = 'iif'

dados_binarios = struct.pack(formate, 192, 5, 1711634.0)


print(f"--- RELATÓRIO BINÁRIO ---")
print(f"Bytes puros: {dados_binarios}")
print(f"Tamanho fixo: {sys.getsizeof(dados_binarios)} bytes (Cabeçalho Python + 12 bytes de dados)")


original = struct.unpack(formato, dados_binarios)
print(f"Recuperado do bit: {original}")


def processar_massa_de_dadosvalidada(dados_brutos): 
    

    
    lista_validada = [] 
    for item in dados_brutos:
        try:
            
            
            valido = MetricaValidator(valor=item)
            lista_validada.append(valido.valor)
        except Exception as e: 
            print(f"Dado inválido descartado: {item} -> {e}")
            
    
    
    
    metricas = array.array('d', lista_validada)
    
    
    tamanho_bytes = sys.getsizeof(metricas)
    print(f"Processando {len(metricas)} métricas...")
    print(f"Espaço total em RAM: {tamanho_bytes} / 1024 / 1024: 2.f} MB")
    
    
    total = sum(metricas)
    
    
    dados_sujos = [1.5, -10.0, 3.2, "erro", 5.5]
    total = processar_massa_de_dadosvalidada(dados_sujos)
    print(f"Soma final segura: {total}")
