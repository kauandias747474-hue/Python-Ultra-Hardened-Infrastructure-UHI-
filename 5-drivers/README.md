# 5-Drivers: Low-Level I/O, IPC & Zero-Copy

### [PT-BR] Descrição
Este módulo demonstra uma infraestrutura de comunicação entre processos (IPC) de ultra-baixa latência, utilizando uma arquitetura de **Zero-Copy**. O objetivo é mover dados entre diferentes aplicações sem o overhead de escrita em disco ou múltiplas cópias na memória RAM, simulando o núcleo de um motor de missão crítica (como sistemas de HFT - High Frequency Trading ou Defesa Cibernética).

### [EN] Description
This module demonstrates an ultra-low latency inter-process communication (IPC) infrastructure using a **Zero-Copy** architecture. The goal is to move data between different applications without the overhead of disk I/O or multiple RAM copies, simulating a mission-critical core engine (such as HFT - High Frequency Trading or Cyber Defense systems).

---

##  Componentes do Sistema / System Components

### 1. `ipc_server.py`
* **[PT]** **O Produtor**. Atua como o "Dono da Memória". Ele aloca um segmento de Memória Compartilhada (Shared Memory) diretamente no Kernel do Windows e escreve dados binários (`struct`) em tempo real, evitando qualquer I/O de disco.
* **[EN]** **The Producer**. Acts as the "Memory Owner". It allocates a Shared Memory segment directly in the Windows Kernel and writes binary data (`struct`) in real-time, bypassing any disk I/O.

### 2. `zmq_bridge.py`
* **[PT]** **O Distribuidor**. Uma ponte invisível que monitora a RAM via ponteiros. Assim que detecta um novo ID, despacha o pacote via ZeroMQ (PUB/SUB) usando a técnica *Zero-Copy*, garantindo que o dado chegue à rede sem ser duplicado pelo interpretador Python.
* **[EN]** **The Distributor**. An invisible bridge monitoring RAM via pointers. Once it detects a new ID, it dispatches the packet via ZeroMQ (PUB/SUB) using *Zero-Copy* techniques, ensuring data reaches the network without being duplicated by the Python interpreter.

### 3. `main.py`
* **[PT]** **O Consumidor**. Um motor assíncrono otimizado com a política *Proactor (IOCP)* do Windows e *CPU Affinity* (fixado no Núcleo 0). Ele recebe, desempacota e processa o stream de dados com jitter mínimo e proteção contra travamentos (Timeout).
* **[EN]** **The Consumer**. An async engine optimized with Windows *Proactor (IOCP)* policy and *CPU Affinity* (pinned to Core 0). It receives, unpacks, and processes the data stream with minimum jitter and crash protection (Timeout).

---

##  Conceitos Aplicados / Concepts Applied

* **Shared Memory IPC:** * [PT] Sincronização via RAM compartilhada para ignorar a lentidão da pilha TCP/IP local.
    * [EN] Synchronization via shared RAM to bypass local TCP/IP stack overhead.
* **Zero-Copy Networking:** * [PT] Uso de ponteiros de memória no ZeroMQ para transmitir dados sem criar cópias temporárias.
    * [EN] Using memory pointers in ZeroMQ to transmit data without creating temporary copies.
* **CPU Pinning & Affinity:** * [PT] Travamento de processos em núcleos específicos para maximizar o uso do Cache L1/L2 e evitar Context Switching.
    * [EN] Pinning processes to specific CPU cores to maximize L1/L2 Cache hits and avoid Context Switching.
* **Binary Serialization (`struct`):** * [PT] Comunicação em formato binário puro (Little Endian), eliminando o custo de CPU de formatos como JSON/XML.
    * [EN] Pure binary format communication (Little Endian), eliminating the CPU cost of JSON/XML formats.

---

##  Para que serve este código? / What is this for?

**[PT]** Este projeto serve como prova de conceito para sistemas onde cada microssegundo conta. Ele demonstra como integrar diferentes processos de forma desacoplada, utilizando gerenciamento de hardware de baixo nível (Memória e CPU) para atingir performance industrial em ambiente Windows.

**[EN]** This project serves as a proof of concept for systems where every microsecond matters. It demonstrates how to integrate different processes in a decoupled way, using low-level hardware management (Memory and CPU) to achieve industrial-grade performance in a Windows environment.

---

##  Requisitos / Requirements
```powershell
pip install pyzmq tornado psutil
