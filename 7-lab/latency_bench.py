import pytest
import array

from main import (
    run_subnet_calc, 
    run_ml_vectorized, 
    run_ml_inference,
    run_array_int, 
    run_list_int, 
    run_list_search, 
    run_set_search,
    run_local_access, 
    run_global_access, 
    run_threading_test,
    run_multiprocessing_test, 
    run_generator_memory,
    run_ipc_queue, 
    run_memory_view_test, 
    run_json_rust, 
    run_pattern_matching
)


def test_bench_cache_hit_array(benchmark):
    """Mede a eficiência de dados contíguos (SIMD-ready)."""
    benchmark(run_array_int)

def test_bench_cache_miss_list(benchmark):
    """Mede o impacto de ponteiros espalhados na RAM."""
    benchmark(run_list_int)


def test_bench_algo_linear_list(benchmark):
    """Busca O(n) - Lento conforme a lista cresce."""
    benchmark(run_list_search, target=9999)

def test_bench_algo_constant_set(benchmark):
    """Busca O(1) - Velocidade constante via Hash Table."""
    benchmark(run_set_search, target=9999)

def test_bench_json_orjson_rust(benchmark):
    """Serialização ultra-rápida escrita em Rust."""
    benchmark(run_json_rust)


def test_bench_math_vectorized_numpy(benchmark):
    """Operações paralelas via instruções SIMD da CPU."""
    benchmark(run_ml_vectorized)

def test_bench_math_pure_python(benchmark):
    """Cálculo sequencial (um por um)."""
    benchmark(run_ml_inference)


def test_bench_multiprocessing(benchmark):
    """Paralelismo real ignorando o GIL do Python."""
    benchmark(run_multiprocessing_test)

def test_bench_scope_local(benchmark):
    """Acesso a variáveis locais (LOAD_FAST)."""
    benchmark(run_local_access)

def test_bench_scope_global(benchmark):
    """Acesso a variáveis globais (LOAD_GLOBAL - mais lento)."""
    benchmark(run_global_access)
