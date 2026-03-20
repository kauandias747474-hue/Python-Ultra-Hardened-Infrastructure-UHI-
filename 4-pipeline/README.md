#  4-Pipeline: O(1) Stream Engine


[PT-BR] Processamento de volumes massivos de dados com pegada de memória constante (Lazy Evaluation).
[EN] Processing massive data volumes with constant memory footprint (Lazy Evaluation).

---

##  Lógica do Código / Code Logic

1.  **Generator Chaining:**
    * [PT] Encadeamento de `yield` para processar arquivos gigigantes linha a linha.
    * [EN] Chaining `yield` to process giant files line by line.
2.  **High-Speed ETL (Polars):**
    * [PT] Integração com **Polars** (Rust-based) para processamento paralelo de streams de dados.
    * [EN] Integration with **Polars** (Rust-based) for parallel data stream processing.

##  Conceitos Aplicados / Concepts Applied

* **Lazy Evaluation:** [PT] Processamento sob demanda para economizar RAM. [EN] On-demand processing to save RAM.
* **Backpressure:** [PT] Controle de fluxo para evitar sobrecarga. [EN] Flow control to avoid overhead.
* **Framework:** `Polars` (Fast Dataframes), `itertools` (Vanilla optimization).
