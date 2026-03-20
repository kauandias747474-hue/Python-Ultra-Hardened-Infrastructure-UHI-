#  1-Engine: User-Space Orchestration

### [PT-BR] Resumo Técnico do Nano-Scheduler
O **Nano-Scheduler** é um motor de execução de baixa latência projetado para escalonamento determinístico em *User-Space*.

* **O que faz:** Gerencia ciclos de tarefas (*bursts*) usando `array.array` para alocação contígua de memória, reduzindo o uso de RAM e a pressão do Garbage Collector.
* **Problemas Resolvidos:** Corrigimos o erro crítico de **Deadlock (OSError 36)** implementando travas de hardware não-bloqueantes (`msvcrt.locking` no Windows e `fcntl.flock` no Unix), permitindo que processos filhos (`multiprocessing`) acessem o console sem travar o kernel do simulador.
* **Conexão com o Benchmark:** O Scheduler se conecta ao Benchmark através de **Shared Memory (Memória Compartilhada)**. Ele reserva um segmento da RAM via `mmap`, onde escreve o estado atual da execução em tempo real. O Benchmark, por sua vez, mapeia o mesmo endereço de memória, permitindo uma leitura passiva sem interromper o fluxo do escalonador.

**Conceitos Importantes Aplicados:**
1.  **IPC (Inter-Process Communication):** Uso de `mmap` para criar um canal de dados ultraveloz entre dois processos independentes (Scheduler e Benchmark).
2.  **Binary Serialization (`struct`):** Os dados são transmitidos em formato binário puro (C-Style), eliminando o overhead de conversão de strings e garantindo que o Benchmark leia exatamente o que o processador está manipulando.
3.  **Zero-Copy Architecture:** O Benchmark não solicita os dados; ele os "enxerga" diretamente na RAM compartilhada, reduzindo a latência de I/O para níveis próximos de zero.

---

### [EN] Nano-Scheduler Technical Summary
The **Nano-Scheduler** is a low-latency execution engine designed for deterministic *User-Space* scheduling.

* **What it does:** Manages task cycles (*bursts*) using `array.array` for contiguous memory allocation, reducing RAM footprint and Garbage Collector pressure.
* **Problems Solved:** We fixed the critical **Deadlock (OSError 36)** by implementing non-blocking hardware locks (`msvcrt.locking` on Windows and `fcntl.flock` on Unix), allowing child processes (`multiprocessing`) to access the console without freezing the simulator's kernel.
* **Benchmark Interconnect:** The Scheduler connects to the Benchmark via **Shared Memory**. It reserves a RAM segment through `mmap`, where it writes the current execution state in real-time. The Benchmark then maps the same memory address, allowing for passive reading without interrupting the scheduler's flow.

**Key Engineering Concepts:**
1.  **IPC (Inter-Process Communication):** Using `mmap` to create an ultra-fast data channel between two independent processes (Scheduler and Benchmark).
2.  **Binary Serialization (`struct`):** Data is transmitted in pure binary format (C-Style), eliminating string conversion overhead and ensuring the Benchmark reads exactly what the processor is handling.
3.  **Zero-Copy Architecture:** The Benchmark doesn't request data; it "sees" it directly in shared RAM, reducing I/O latency to near-zero levels.
---

##  A Tese / The Thesis

### [PT-BR] Otimização de Baixo Nível
* **Mecanismo:** Corrotinas puras via `yield`. Sem o overhead de objetos `Task` ou `Future`, reduzindo drasticamente o consumo de memória e pressão do GC.
* **Prioridade $O(\log n)$:** Utilização de `heapq` para garantir que a tarefa com o *deadline* mais próximo seja sempre a próxima, permitindo um comportamento *Soft Real-Time*.
* **Otimização de Bytecode:** Injeção de `time.perf_counter_ns` em escopo local para forçar o uso de `LOAD_FAST` em vez de `LOAD_GLOBAL`, minimizando o jitter.

### [EN] Low-Level Optimization
* **Mechanism:** Pure coroutines via `yield`. No `Task` or `Future` object overhead, drastically reducing memory footprint and GC pressure.
* **$O(\log n)$ Priority:** Leveraging `heapq` to ensure the task with the nearest deadline is always next, enabling *Soft Real-Time* behavior.
* **Bytecode Tuning:** Injecting `time.perf_counter_ns` into local scope to force `LOAD_FAST` instead of `LOAD_GLOBAL`, minimizing jitter.

---

##  O Código Demonstrativo / The Demo Code

### [PT-BR]
O código demonstra três conceitos avançados de engenharia:
1.  **Spin-Lock Híbrido:** Uso de `time.sleep` para intervalos longos e *Busy-Wait* para precisão de nanossegundos, contornando a imprecisão do Kernel.
2.  **Zero-Allocation:** Uso de `heapq.heapreplace` para manter tarefas periódicas sem instanciar novos objetos no heap.
3.  **Telemetria de Jitter:** O motor calcula e expõe o desvio entre o tempo alvo e a execução real.

### [EN]
The code demonstrates three advanced engineering concepts:
1.  **Hybrid Spin-Lock:** Using `time.sleep` for long intervals and *Busy-Wait* for nanosecond precision, bypassing Kernel scheduling imprecision.
2.  **Zero-Allocation:** Utilizing `heapq.heapreplace` to maintain periodic tasks without instantiating new objects on the heap.
3.  **Jitter Telemetry:** The engine calculates and exposes the drift between target time and actual execution.

---

