# 📊 6-Telemetry: Systemic Observability

[PT-BR]
Monitoramento de performance em nível de interpretador e hardware. Este módulo demonstra como extrair métricas profundas do sistema operacional para validar o comportamento do software sob carga real.

[EN]
Performance monitoring at the interpreter and hardware levels. This module demonstrates how to extract deep metrics from the operating system to validate software behavior under real-world loads.

---

## 📈 Demonstração / Demonstration: The Context-Switch Counter

O foco desta implementação é a visibilidade sobre as interrupções que afetam o determinismo da execução.

### Engenharia de Observabilidade / Observability Engineering:

* **Metrics (OS Resource Inspection):**
    * [PT-BR] Captura de `ru_nvcsw` (trocas de contexto voluntárias) e `ru_nivcsw` (involuntárias) via módulo `resource`. Isso permite identificar quando o SO "expulsa" sua tarefa da CPU.
    * [EN] Capture of `ru_nvcsw` (voluntary context switches) and `ru_nivcsw` (involuntary) via the `resource` module. This identifies when the OS "evicts" your task from the CPU.

* **Goal (Latency Spikes Detection):**
    * [PT-BR] Identificar picos de latência causados por interrupções do Kernel ou preempção. O objetivo é garantir que o Nano-Scheduler mantenha o controle da CPU pelo maior tempo possível.
    * [EN] Identify latency spikes caused by Kernel interruptions or preemption. The goal is to ensure the Nano-Scheduler maintains CPU control for as long as possible.

* **Interpreter Profiling:**
    * [PT-BR] Monitoramento da carga do Garbage Collector (GC) e tempos de execução de ciclos de loop para correlacionar eventos de software com eventos de hardware.
    * [EN] Monitoring Garbage Collector (GC) load and loop cycle execution times to correlate software events with hardware events.



---

## 🔍 O Código Demonstrativo / The Demo Code

### [PT-BR] O que este código prova?
1. **Context-Switch Awareness:** O script demonstra como uma tarefa mal otimizada aumenta as trocas de contexto involuntárias, degradando a performance.
2. **Deterministic Profiling:** Captura de métricas com overhead mínimo, garantindo que o monitoramento não altere os resultados (Observability bias).
3. **Statistical Analysis:** Cálculo de percentis (P95, P99) de jitter para oferecer uma visão realista da confiabilidade do sistema.

### [EN] What does this code prove?
1. **Context-Switch Awareness:** The script demonstrates how poorly optimized tasks increase involuntary context switches, degrading performance.
2. **Deterministic Profiling:** Capturing metrics with minimal overhead, ensuring monitoring doesn't skew results (Observability bias).
3. **Statistical Analysis:** Calculation of jitter percentiles (P95, P99) to provide a realistic view of system reliability.
