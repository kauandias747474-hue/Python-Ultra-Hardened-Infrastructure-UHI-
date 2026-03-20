#  5-Drivers: Low-Level I/O & IPC


[PT-BR] Comunicação de ultra-baixa latência entre processos (Kernel Bypass).
[EN] Ultra-low latency inter-process communication (Kernel Bypass).

---

##  Lógica do Código / Code Logic

1.  **Unix Domain Sockets (UDS):**
    * [PT] Comunicação via `AF_UNIX` para evitar o overhead da pilha TCP/IP.
    * [EN] Communication via `AF_UNIX` to bypass TCP/IP stack overhead.
2.  **Smart Messaging (ZeroMQ):**
    * [PT] Uso de **ZeroMQ (pyzmq)** para gerenciar filas de mensagens e padrões Pub/Sub.
    * [EN] Using **ZeroMQ (pyzmq)** to manage message queues and Pub/Sub patterns.

##  Conceitos Aplicados / Concepts Applied

* **Inter-Process Communication:** [PT] Sincronização de processos via Sockets. [EN] Process synchronization via Sockets.
* **Event Loops:** [PT] Uso de `uvloop` para acelerar o I/O assíncrono. [EN] Using `uvloop` to accelerate async I/O.
* **Framework:** `pyzmq` (ZeroMQ), `uvloop` (Fast Asyncio).
