import zmq
import struct 
import time 
from multiprocessing import shared_memory
import sys

SHM_NAME = "minha_memoria_zero_copy"
MSG_FORMAT = "=id"
MSG_SIZE = struct.calcsize(MSG_FORMAT)

def start_zmq_bridge():
    context = zmq.Context()
    pub_socket = context.socket(zmq.PUB)
    
    try:
     
        pub_socket.setsockopt(zmq.LINGER, 0)
        pub_socket.bind("tcp://*:5555")
        print("[*] ZMQ BRIDGE: Porta 5555 aberta.")
    except Exception as e:
        print(f"[ERRO] Falha ao abrir porta: {e}")
        sys.exit(1)

    print("[*] Aguardando memoria do IPC Server...")
    
    shm = None
    while shm is None:
        try: 
            shm = shared_memory.SharedMemory(name=SHM_NAME)
        except FileNotFoundError:
            time.sleep(0.5)
        except Exception as e:
            print(f"[!] Erro inesperado na SHM: {e}")
            time.sleep(1)

    buffer = shm.buf 
    last_processed_id = -1
    print(f"[OK] Conectado a RAM: {SHM_NAME}")

    try: 
        while True: 
         
           
            current_id = struct.unpack_from("=i", buffer, 0)[0]
            
            if current_id != last_processed_id:
                # Envio Zero-Copy
                pub_socket.send(buffer[:MSG_SIZE], copy=False)
                last_processed_id = current_id
            
          
            time.sleep(0.001) 
            
    except KeyboardInterrupt:
        print("\n[!] Encerrando Bridge...")
    finally:
        if shm:
            shm.close()
        pub_socket.close()
        context.term()
        print("[*] Recursos liberados.")

if __name__ == "__main__":
    start_zmq_bridge()
