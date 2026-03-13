# ⚙️ 1-Engine: User-Space Orchestration

Este repositório contém uma implementação minimalista de um **Nano-Scheduler** em Python. O objetivo é demonstrar como o escalonamento determinístico em *User-Space* pode reduzir o jitter e o overhead de contexto em comparação com soluções genéricas como o `asyncio`.

## ⚡ A Tese: Otimização de Baixo Nível

O código foca na eficiência bruta, tratando corrotinas como unidades de tempo e prioridade. A demonstração baseia-se em três pilares:

* **Mechanism:** Uso de `generators` puros e `yield`. Ao evitar o overhead de objetos `Task` e `Future`, o motor mantém o stack de execução leve e amigável ao cache da CPU.
* **Priority (O(log n)):** Implementação de uma fila de prioridade via `heapq`. O sistema garante que a tarefa com o *deadline* mais próximo seja sempre a próxima, permitindo um comportamento de tempo-real (Soft Real-Time).
* **Bytecode-Level Tuning:** Injeção de `time.perf_counter_ns` como variável local (`LOAD_FAST`). Isso elimina a busca no dicionário de globais (`LOAD_GLOBAL`), economizando ciclos de CPU em cada iteração do loop crítico.



[Image of binary heap data structure]


---

## 🔍 O Código Demonstrativo

O arquivo principal ilustra como arquitetar um sistema de orquestração que prioriza o determinismo:

1.  **Hybrid Spin-Lock:** Para precisão de microssegundos, o código demonstra uma espera híbrida: `time.sleep` para longos intervalos e um `while` loop (Spin-lock) para os nanossegundos finais, evitando a imprecisão do escalonador do SO.
2.  **Zero-Allocation Cycle:** Uso de `heapq.heapreplace` para tarefas periódicas, garantindo que a fila seja atualizada sem instanciar novos objetos, mantendo o Garbage Collector (GC) estável.
3.  **Jitter Telemetry:** A própria engine mede o desvio (atraso) de cada execução, provando a eficácia do modelo através de métricas reais de latência.



---

## 🚀 Por que isso é relevante?

Este código não é apenas um script; é uma prova de conceito para:
* **High-Frequency Systems:** Onde cada microssegundo de atraso conta.
* **Embedded Python:** Onde recursos de CPU e RAM são escassos.
* **Sistemas de Controle:** Que exigem que o intervalo entre tarefas seja constante e previsível.

---
