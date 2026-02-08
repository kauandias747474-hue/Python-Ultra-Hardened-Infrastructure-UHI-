# 🌊 Pipeline Layer (Stream Processing)

Especializada em **Processamento de Dados de Alta Performance**. Esta camada utiliza o poder dos iteradores e geradores nativos do Python.

### Características:
* **Memory Efficiency:** Processamento de arquivos Giga/Terabyte com consumo fixo de RAM ($O(1)$).
* **Lazy Evaluation:** O dado só é processado no momento exato em que é necessário.
* **Data Flow:** Transformação de dados em estágios, permitindo paralelismo lógico.

> **Princípio:** Não carregue na memória o que você pode transmitir via fluxo.
