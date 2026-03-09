# 🌊 4-Pipeline: O(1) Stream Engine

Processamento de fluxos massivos de dados com pegada de memória constante.

### 🛠️ Demonstração: The Infinite Log Processor
* **Mechanism:** Encadeamento de geradores e `itertools` para Lazy Evaluation.
* **Efficiency:** Processamento de GBs de dados utilizando apenas KBs de buffer físico.
