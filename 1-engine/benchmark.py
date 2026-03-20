import time
import statistics 
import math 
import array
import collections
import gc
import sys 
import json 
import struct
import mmap


inicio_benchmark = time.time()

def get_size(obj, seen=None):
    """Calcula recursivamente o tamanho real de objetos em bytes."""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    
    return size

def run_monitor():
   
    print(f" Iniciando Benchmark... Tempo de boot: {time.time() - inicio_benchmark:.4f}s")
    
    try:
       
        shm = mmap.mmap(-1, 1024) 
        
        amostras_latencia = []
        
        for i in range(5):
            t_ciclo_inicio = time.time()
            
            raw_data = b'\x01\x00\x00\x00'
            task_id = struct.unpack('i', raw_data)[0]
            

            res_math = math.sqrt(16) * math.pow(2, 3)
            res_stat = statistics.mean([1, 2, 3, 4, 5])
            
            tamanho_atual = get_size(amostras_latencia)
            
            t_ciclo_fim = time.time()
            latencia = t_ciclo_fim - t_ciclo_inicio
            amostras_latencia.append(latencia)
            
            print(f"Task ID: {task_id} | Latência: {latencia:.6f}s | RAM List: {tamanho_atual} bytes")
            
          
            gc.collect()

      
        relatorio = {
            "media_latencia": statistics.mean(amostras_latencia),
            "desvio_padrao": statistics.stdev(amostras_latencia) if len(amostras_latencia) > 1 else 0,
            "objetos_analisados": len(amostras_latencia)
        }
        
        print("\n--- RELATÓRIO FINAL ---")
        print(json.dumps(relatorio, indent=4))

    except Exception as e:
        print(f" Erro no monitor: {e}")

if __name__ == "__main__":
    run_monitor()
