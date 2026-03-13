# 🌊 4-Pipeline: O(1) Stream Engine

[PT-BR]
Processamento de fluxos massivos de dados com pegada de memória constante. Este módulo demonstra como transformar o Python em uma ferramenta de ETL (Extract, Transform, Load) de alta eficiência, capaz de processar volumes de dados que excedem a RAM disponível.

[EN]
Processing massive data streams with a constant memory footprint. This module demonstrates how to turn Python into a high-efficiency ETL (Extract, Transform, Load) tool, capable of processing data volumes that exceed available RAM.

---

## 🛠️ Demonstração / Demonstration: The Infinite Log Processor

O foco desta implementação é o processamento linear e infinito, garantindo estabilidade operacional independentemente do tamanho do input.

### Engenharia de Fluxo / Stream Engineering:

* **Mechanism (Lazy Evaluation):**
    * [PT-BR] Encadeamento de geradores (`yield`) e uso estratégico de `itertools`. Os dados são processados item por item, nunca carregando o dataset completo na memória.
    * [EN] Generator chaining (`yield`) and strategic use of `itertools`. Data is processed item by item, never loading the full dataset into memory.

* **Efficiency ($O(1)$ Space Complexity):**
    * [PT-BR] Processamento de Gigabytes de dados utilizando apenas Kilobytes de buffer físico. A pegada de memória permanece plana, eliminando riscos de `MemoryError`.
    * [EN] Processing Gigabytes of data using only Kilobytes of physical buffer. The memory footprint remains flat, eliminating `MemoryError` risks.

* **Pipelining:**
    * [PT-BR] Arquitetura de "filtro sobre filtro", onde cada estágio da pipeline é uma corrotina independente, permitindo manutenção modular e alta velocidade de passagem.
    * [EN] "Filter-on-filter" architecture, where each pipeline stage is an independent coroutine, allowing for modular maintenance and high throughput speed.



---

## 🔍 O Código Demonstrativo / The Demo Code

### [PT-BR] O que este código prova?
1. **Memory Ceiling:** O script simula a leitura de um arquivo de log infinito, provando através de telemetria em tempo real que o uso de RAM não cresce proporcionalmente ao volume processado.
2. **Generator Chaining:** Demonstra a elegância de compor lógica complexa (Parser -> Filter -> Aggregator) sem criar listas intermediárias.
3. **Backpressure Readiness:** A estrutura está preparada para sistemas que precisam pausar ou retomar o fluxo de dados sem perda de estado.

### [EN] What does this code prove?
1. **Memory Ceiling:** The script simulates reading an infinite log file, proving through real-time telemetry that RAM usage does not grow proportionally to the processed volume.
2. **Generator Chaining:** Demonstrates the elegance of composing complex logic (Parser -> Filter -> Aggregator) without creating intermediate lists.
3. **Backpressure Readiness:** The structure is ready for systems that need to pause or resume data flow without loss of state.
