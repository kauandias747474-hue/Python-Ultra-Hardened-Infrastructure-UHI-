import zmq
import zmq.asyncio
import struct
import asyncio
import sys
import psutil 


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

ZMQ_ENDPOINT = "tcp://localhost:5555"
MSG_FORMAT = "=id"

async def consume_data(limite_mensagens=500):
    """
    Loop de consumo com parada automatica e timeout.
    """
    context = zmq.asyncio.Context()
    subscriber = context.socket(zmq.SUB)
    
    subscriber.connect(ZMQ_ENDPOINT)
    subscriber.setsockopt_string(zmq.SUBSCRIBE, "")
    subscriber.setsockopt(zmq.CONFLATE, 1)
    
    print(f"[*] Consumidor Online em {ZMQ_ENDPOINT}")
    print(f"[*] O programa parara automaticamente apos {limite_mensagens} mensagens.")
    print("[*] Ou se ficar 5 segundos sem receber nada (Timeout).\n")

    contador = 0
    try:
        while contador < limite_mensagens:
            try:
                
                payload = await asyncio.wait_for(subscriber.recv(), timeout=5.0)
                
                msg_id, valor = struct.unpack(MSG_FORMAT, payload)
                contador += 1
                
                print(f"[{contador}/{limite_mensagens}] ID: {msg_id} | Valor: {valor:.4f}")
                
            except asyncio.TimeoutError:
                print("\n[!] TIMEOUT: Nao recebi dados da Bridge por 5 segundos.")
                break # Sai do loop

        print(f"\n[OK] Processamento de {contador} pacotes finalizado.")

    except Exception as e:
        print(f"\n[ERRO] Falha critica: {e}")
    finally:
        print("[*] Liberando recursos do ZeroMQ...")
        subscriber.close()
        context.term()

async def main():

    try:
        p = psutil.Process()
        p.cpu_affinity([0])
    except:
        pass

    await consume_data(limite_mensagens=500)

if __name__ == "__main__":
    try:
        asyncio.run(main())
        print("[*] Programa encerrado com sucesso.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n[!] Interrupcao manual (Ctrl+C). Fechando...")
        sys.exit(0)
