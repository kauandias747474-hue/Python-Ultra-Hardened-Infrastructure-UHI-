# 🧪 7-Lab: Performance Benchmarking

[PT-BR]
O campo de provas científico do projeto. O Lab é onde as teses de engenharia são validadas através de métricas rigorosas, comparando a performance bruta do sistema contra implementações convencionais.

[EN]
The project's scientific proving ground. The Lab is where engineering theses are validated through rigorous metrics, comparing the system's raw performance against conventional implementations.

---

## 🔬 Atividades / Activities

O foco desta seção é a validação empírica do determinismo e da eficiência.

### Metodologia de Teste / Testing Methodology:

* **Micro-benchmarking (Vanilla vs. Generic):**
    * [PT-BR] Comparação direta entre o "Vanilla Python" otimizado (este projeto) e abstrações genéricas de mercado. Medimos o custo por instrução e o tempo de setup de cada tarefa.
    * [EN] Direct comparison between optimized "Vanilla Python" (this project) and generic market abstractions. We measure the cost per instruction and the setup time for each task.

* **Stress Testing:**
    * [PT-BR] Testes de carga extrema para validar o determinismo da **1-Engine**. O objetivo é encontrar o "ponto de quebra" onde o jitter começa a degradar a previsibilidade do sistema.
    * [EN] Extreme load testing to validate the determinism of the **1-Engine**. The goal is to find the "breaking point" where jitter begins to degrade system predictability.

* **Statistical Validation:**
    * [PT-BR] Uso de ferramentas de perfilamento térmico e de CPU para garantir que as otimizações de memória (2-Architect) resultem em menos ciclos de CPU desperdiçados.
    * [EN] Using thermal and CPU profiling tools to ensure that memory optimizations (2-Architect) result in fewer wasted CPU cycles.



---

## 🔍 O Código Demonstrativo / The Demo Code

### [PT-BR] O que este código prova?
1. **The Performance Gap:** Um script que coloca o Nano-Scheduler frente a frente com o `asyncio` em um cenário de 1 milhão de trocas de contexto, exibindo a economia real de tempo.
2. **Deterministic Boundaries:** Demonstra como o sistema se comporta sob 90% de uso de CPU, provando que a prioridade $O(\log n)$ mantém as tarefas críticas estáveis.
3. **Reproducibility:** Fornece um ambiente isolado para que qualquer desenvolvedor possa reproduzir os resultados e validar as métricas de baixa latência.

### [EN] What does this code prove?
1. **The Performance Gap:** A script that pits the Nano-Scheduler against `asyncio` in a 1-million context switch scenario, showing actual time savings.
2. **Deterministic Boundaries:** Demonstrates how the system behaves under 90% CPU load, proving that $O(\log n)$ priority keeps critical tasks stable.
3. **Reproducibility:** Provides an isolated environment so any developer can reproduce the results and validate low-latency metrics.
