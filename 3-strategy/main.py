import threading
import time
import logging
import logging.handlers
import json
import queue
import random
import gc


from transitions import Machine 

class AtomicFsm:
    def __init__(self):
        self._state = "IDLE"
        self._lock = threading.Lock()

    def transit(self, next_state):
        with self._lock:
            print(f"[TRANSITION] {self._state} -> {next_state}")
            time.sleep(0.1)
            self._state = next_state

class FormatatorStateMachine(logging.Formatter):
    def format(self, record):
        log_entry = {
            "ts": self.formatTime(record),
            "level": record.levelname,
            "state": getattr(record, "current_state", "UNKNOWN"),
            "msg": record.getMessage()
        }
        return json.dumps(log_entry)

class AtomicEngine:
    states = ['IDLE', 'SCANNING', 'ANALYZING', 'LOCKED']
    def __init__(self):
        self.machine = Machine(model=self, states=AtomicEngine.states, initial='IDLE')
        self.machine.add_transition(trigger='start_task', source='IDLE', dest='SCANNING')
        self.machine.add_transition(trigger='critical_stop', source='*', dest='LOCKED')

def run_logic_gate_test():
    print("\n[STEP 1] Teste de Atomicidade")
    fsm = AtomicFsm()
    threads = [threading.Thread(target=fsm.transit, args=(f"STATE_{i}",)) for i in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()

if __name__ == "__main__":
    try:
        run_logic_gate_test()
        print("\n[STEP 2] Teste de Engine Finalizado.")
    except Exception as e:
        print(f"[!] Erro: {e}")
    finally:
        gc.collect()
        print("\n[*] Sistema higienizado.")
