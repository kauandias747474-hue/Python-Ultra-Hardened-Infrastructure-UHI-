import logging 
import logging.handlers
import time 
import queue 
import random 
import json 
import gc 
from transitions import Machine 


class StateMachine(logging.Machine)
   def format(self, record):
       log_entry = { 
           "ts": self.formatTime(record),
           "level": record.levelname,
           "state": getattr(record,"current_state", "UNKNOWN"),
           "msg": record.getMessage(),
           "trigger": getattr(record, "trigger", "N/A"),
           "mem_addr": str(getattr(record, "mem_addr", "N/A")) 
           }
           return json.dumps(log_entry)
           
           
log_queue = queue.Queue(-1)
queue_handler = logging.handlers.QueueHandler(log_queue)

console_handler = logging.StreamHandler()
console_handler.setFormatter(ForensicFormatter())

listener = logging.handlers.QueueListener(log_queue, console_handler)
listener.start()

logger = logging.getLogger("SentinelEngine")
logger.setLevel(logging.INFO)
logger.addHandler(queue_handler)



 class MachineEngine:
     states = ['IDLE', 'SCANNING', 'ANALYZING, 'LOCKED']
     
     def __init__(self):
         
    self.machine = Machine(model=self, states=AtomicEngine.states, initial='IDLE', send_event=True) 
    
    
    self.machine.add_transition(trigger='start_task', source='IDLE', dest='SCANNING', prepare='check_root_auth')
        self.machine.add_transition(trigger='process_data', source='SCANNING', dest='ANALYZING')
        self.machine.add_transition(trigger='critical_stop', source='*', dest='LOCKED', after='on_lock_alert')
        
        self.machine.after_state_change = 'verify_and_log'
        
    
    def check_root_auth(self, event):
        logger.info("Verificando credenciais...", extra={"trigger": event.event.name})

    def on_lock_alert(self, event):
        logger.critical("CIRCUITO DE TRAVAMENTO ATIVADO", extra={"trigger": event.event.name})

    def verify_and_log(self, event):
        logger.info(f"Mudança validada", extra={
            "current_state": self.state,
            "trigger": event.event.name,
            "mem_addr": id(self)
        })


engine = AtomicEngine()

try: 
    print(f"[*] Estado Inicial: {engine.state}")
    engine.start_task()
    engine.process_data()
    engine.critical_stop()
        
   
    triggers = ['start_task', 'process_data', 'critical_stop']
    for _ in range(10):
        t = random.choice(triggers)
        try:
            getattr(engine, t)()
        except Exception:
            pass 

except Exception as e:
    print(f"[!] Erro de Segurança: {e}")
       
finally:
    time.sleep(1.0) 
    listener.stop()

    gc.collect() 
    print("[*] Memória higienizada.")
