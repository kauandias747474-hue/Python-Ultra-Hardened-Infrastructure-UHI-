import dis
import time
import timeit
import gc
import array
import asyncio
import threading
import multiprocessing
import platform
import json
from functools import lru_cache
from contextlib import contextmanager
from multiprocessing import Queue 
from typing import List, Tuple, Union, Any

import orjson
import numpy as np


NAME, AGE = "Alice", 30
DATA_SAMPLE_LIST = ["python", "java", "javascript", "rust", "typescript"] * 1000
DATA_DICT_SAMPLE = {"status": "ok", "codes": [200, 404, 500], "payload": "UHI-LAB" * 100}
LARGE_LIST = list(range(10000))
LARGE_SET = set(LARGE_LIST)
GLOBAL_VAR = 100

class ComSlots:
    """Impede a criação de __dict__ por instância, economizando RAM."""
    __slots__ = ['x', 'y']
    def __init__(self, x, y): self.x, self.y = x, y

class LabResource:
    """Garante que recursos sejam liberados mesmo em caso de erro."""
    def __init__(self, name): self.name = name
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass


def run_subnet_calc(ip="192.168.1.10", mask="255.255.255.0"):
    """Cálculo de rede usando lógica binária direta na ALU."""
    ip_p = [int(x) for x in ip.split('.')]
    ms_p = [int(x) for x in mask.split('.')]
    return [(ip_p[i] & ms_p[i]) for i in range(4)]


def run_ml_vectorized():
    """Substitui loops Python por operações paralelas no processador (SIMD)."""
    weights = np.array([0.5, 0.8, -0.2, 1.5], dtype=np.float64)
    inputs = np.array([10.5, 20.1, 5.0, 30.2], dtype=np.float64)
    return np.dot(inputs, weights) + 2.0

def run_ml_inference(inputs=[10.5, 20.1, 5.0, 30.2]):
    """Simulação clássica de inferência (comparativo)."""
    MODEL_WEIGHTS = [0.5, 0.8, -0.2, 1.5]
    return sum(i * w for i, w in zip(inputs, MODEL_WEIGHTS)) + 2.0

def run_list_int():
    """Cache Misses: Ponteiros espalhados."""
    return sum([i for i in range(10000)])

def run_array_int():
    """Cache Hits: Dados contíguos na RAM."""
    return sum(array.array('i', range(10000)))

def run_list_search(target=9999): return target in LARGE_LIST # O(n)
def run_set_search(target=9999):  return target in LARGE_SET  # O(1)

def run_global_access():
    total = 0
    for i in range(1000): total += GLOBAL_VAR
    return total

def run_local_access():
    local_v = GLOBAL_VAR 
    total = 0
    for i in range(1000): total += local_v
    return total

def cpu_heavy_task(n=100000): return sum(i * i for i in range(n))

def run_threading_test():
    """Concorrência: Sofre com o GIL em tarefas de CPU."""
    t1 = threading.Thread(target=cpu_heavy_task)
    t2 = threading.Thread(target=cpu_heavy_task)
    t1.start(); t2.start()
    t1.join(); t2.join()

def run_multiprocessing_test():
    """Paralelismo Real: Novos processos (Memória Isolada)."""
    p1 = multiprocessing.Process(target=cpu_heavy_task)
    p2 = multiprocessing.Process(target=cpu_heavy_task)
    p1.start(); p2.start()
    p1.join(); p2.join()

def run_generator_memory():
    """Consumo de RAM constante: Processa um item por vez."""
    return sum(x for x in range(1000000))

@lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

def run_fstring(): return f"Name: {NAME}, Age: {AGE}"

def worker_q(q): q.put("DONE")

def run_ipc_queue():
    """Sincronização e transferência de dados entre núcleos da CPU."""
    q = Queue()
    p = multiprocessing.Process(target=worker_q, args=(q,))
    p.start()
    msg = q.get()
    p.join()
    return msg

def run_memory_view_test():
    """Manipulação de buffers sem duplicação na RAM."""
    raw_data = bytearray(b"X" * 1024 * 1024)
    view = memoryview(raw_data)
    return len(view[500:1000])

def run_json_rust():
    """Serialização ultra-rápida via orjson (C-extensions/Rust)."""
    return orjson.dumps(DATA_DICT_SAMPLE)

def run_pattern_matching(status_code: int) -> str:
    """Árvore de decisão moderna do Python 3.10+."""
    match status_code:
        case 200 | 201: return "OK"
        case 404: return "NOT_FOUND"
        case _: return "UNKNOWN"


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn', force=True)
    print(f"--- AMBIENTE: {platform.system()} | CPU: {platform.processor()} ---")
    
   
    with LabResource("UHI-Scanner") as res:
        print(f"🔹 Diagnóstico Ativo | ID Memória: {id(DATA_SAMPLE_LIST)}")

    
    gc.collect()
    gc.disable() 

    start = time.perf_counter()
    
    # Ciclo de Experimentos Completo
    run_subnet_calc()
    run_ml_vectorized()
    run_ml_inference()
    run_array_int()
    run_list_search()
    fib(30)
    run_local_access()
    run_generator_memory()
    run_multiprocessing_test()
    run_ipc_queue()
    run_memory_view_test()
    run_json_rust()
    run_pattern_matching(200)
    
    gc.enable() 
    end_time = time.perf_counter()
    
    print(f"\n Ciclo 7-LAB finalizado em: {end_time - start:.6f}s")

    print("\n--- BYTECODE: NETWORKING ---")
    dis.dis(run_subnet_calc)
    print("\n--- BYTECODE: PATTERN MATCHING ---")
    dis.dis(run_pattern_matching)
