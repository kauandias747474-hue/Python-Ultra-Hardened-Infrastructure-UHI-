# ⚙️ 1-Engine: User-Space Orchestration

O núcleo atômico do sistema. Responsável pelo escalonamento determinístico de tarefas.

### ⚡ Demonstração: The Nano-Scheduler
* **Mechanism:** Escalonamento via `generators` (corrotinas puras) utilizando `yield`.
* **Priority:** Fila de prioridade $O(\log n)$ via `heapq`.
* **Optimization:** Injeção de `time.perf_counter_ns` em escopo local (`LOAD_FAST`) para redução de jitter.
