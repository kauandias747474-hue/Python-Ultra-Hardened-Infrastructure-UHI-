import os
import psutil
import threading
import copy


try:
    import resource
except ImportError:
    resource = None

def get_system_metrics():
    """Coleta métricas adaptando-se ao Windows e corrigindo erros de atributo."""
    mem = psutil.virtual_memory()
    proc = psutil.Process(os.getpid())

    ctx = proc.num_ctx_switches()
    ctx_switches = ctx.voluntary + ctx.involuntary


    try:
        m_info = proc.memory_info()
   
        page_faults = getattr(m_info, 'page_faults', 0)
    except:
        page_faults = 0


    cpu_usage = psutil.cpu_percent(interval=0.1)

    return {
        "cpu_percent": cpu_usage,
        "ram_used": mem.used,
        "ctx_switches": ctx_switches,
        "page_faults": page_faults,
        "pid": os.getpid()
    }

def stream_kernel_metrics():
    if os.path.exists("/proc/stat"):
        with open("/proc/stat", "r") as f:
            for line in f: yield line.strip()

def capture_snapshot(current_state):
    return copy.deepcopy(current_state)
