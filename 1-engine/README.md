# ⚙️ 1-Engine: User-Space Orchestration

[PT-BR]
O **Nano-Scheduler** é uma demonstração técnica de um motor de execução determinística em Python. O objetivo deste código é provar que o escalonamento em *User-Space*, quando otimizado ao nível de bytecode, pode superar o `asyncio` padrão em cenários de baixa latência e alta precisão.

[EN]
The **Nano-Scheduler** is a technical demonstration of a deterministic execution engine in Python. This code aims to prove that User-Space scheduling, when optimized at the bytecode level, can outperform standard `asyncio` in low-latency, high-precision scenarios.

---

## ⚡ A Tese / The Thesis

### [PT-BR] Otimização de Baixo Nível
* **Mecanismo:** Corrotinas puras via `yield`. Sem o overhead de objetos `Task` ou `Future`, reduzindo drasticamente o consumo de memória e pressão do GC.
* **Prioridade $O(\log n)$:** Utilização de `heapq` para garantir que a tarefa com o *deadline* mais próximo seja sempre a próxima, permitindo um comportamento *Soft Real-Time*.
* **Otimização de Bytecode:** Injeção de `time.perf_counter_ns` em escopo local para forçar o uso de `LOAD_FAST` em vez de `LOAD_GLOBAL`, minimizando o jitter.

### [EN] Low-Level Optimization
* **Mechanism:** Pure coroutines via `yield`. No `Task` or `Future` object overhead, drastically reducing memory footprint and GC pressure.
* **$O(\log n)$ Priority:** Leveraging `heapq` to ensure the task with the nearest deadline is always next, enabling *Soft Real-Time* behavior.
* **Bytecode Tuning:** Injecting `time.perf_counter_ns` into local scope to force `LOAD_FAST` instead of `LOAD_GLOBAL`, minimizing jitter.

---

## 🔍 O Código Demonstrativo / The Demo Code

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

## 🚀 Impacto / Relevance

| [PT-BR] Público | [EN] Audience | Benefício / Benefit |
| :--- | :--- | :--- |
| **Recrutadores** | **Recruiters** | Domínio de CS Fundamentals & Opcodes. |
| **Clientes** | **Clients** | Sistemas ultra-eficientes e previsíveis. |
| **Devs** | **Devs** | Alternativa leve ao overhead do `asyncio`. |

---
