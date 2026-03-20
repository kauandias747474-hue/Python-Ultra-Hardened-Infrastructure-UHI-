import array
import collections
import heapq
import mmap 
import struct
import multiprocessing
import inspect
import gc
import sys
import time


try:
    import fcntl
    HAS_FCNTL = True
except ImportError:
    try:
        import msvcrt
        HAS_FCNTL = False
    except ImportError:
        HAS_FCNTL = None

def lock_output():
    """Garante acesso exclusivo ao console sem travar o sistema (Non-blocking)."""
    if HAS_FCNTL is True:
        try:
            fcntl.flock(sys.stdout.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (OSError, IOError):
            pass
    elif HAS_FCNTL is False:
        try:
            msvcrt.locking(sys.stdout.fileno(), msvcrt.LK_NBLCK, 1)
        except (OSError, IOError):
            pass

def unlock_output():
    """Libera o console/hardware."""
    if HAS_FCNTL is True:
        try:
            fcntl.flock(sys.stdout.fileno(), fcntl.LOCK_UN)
        except (OSError, IOError):
            pass
    elif HAS_FCNTL is False:
        try:
            msvcrt.locking(sys.stdout.fileno(), msvcrt.LK_UNLCK, 1)
        except (OSError, IOError):
            pass


class NanoScheduler:
    __slots__ = ['tasks', 'current_task', 'shared_mem', 'packer']

    def __init__(self):
        self.tasks = array.array('I')
        self.current_task = 0
        self.shared_mem = mmap.mmap(-1, 1024)
        self.packer = struct.Struct('I') 

    def add_task(self, task_id):
        self.tasks.append(task_id)

    def next_task(self):
        if not self.tasks:
            return None
        task_id = self.tasks[self.current_task]
        self.current_task = (self.current_task + 1) % len(self.tasks)
        return task_id

    def remove_task(self, task_id):
        if task_id in self.tasks:
            index = self.tasks.index(task_id)
            del self.tasks[index]
            if index < self.current_task:
                self.current_task -= 1
            elif index == self.current_task:
                self.current_task = 0

def worker(task_id):
    lock_output()
    print(f"  [PROCESSO FILHO] Executando carga da tarefa: {task_id}")
    unlock_output()

if __name__ == "__main__":
    burst_times = [5, 3, 2]
    scheduler = NanoScheduler()
    
    print(" NanoScheduler: Motor Iniciado com Sucesso...")
    
    for i in range(len(burst_times)):
        scheduler.add_task(i)

    for i, b_time in enumerate(burst_times):
        for _ in range(b_time):
            current_id = scheduler.next_task()
            
            if current_id is not None:
                packed_data = scheduler.packer.pack(current_id)
                scheduler.shared_mem.seek(0)
                scheduler.shared_mem.write(packed_data)
                
                print(f"Executando ID: {current_id} | Burst: {b_time}")

                high_priority_queue = []
                heapq.heappush(high_priority_queue, (1, "NÚCLEO_SISTEMA"))
                while high_priority_queue:
                    prio, name = heapq.heappop(high_priority_queue)
                    print(f"  -> Prioridade Máxima: {name}")

                gc.collect()

    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    lock_output()
    print("\n CICLO FINALIZADO.")
    unlock_output()

    methods = [m[0] for m in inspect.getmembers(NanoScheduler, predicate=inspect.isfunction)]
    print(f"Membros da Classe: {methods}")
