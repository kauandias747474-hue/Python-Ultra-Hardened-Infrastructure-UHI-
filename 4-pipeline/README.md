### 1. Data Ingestion (Generators)
**[PT]** Utiliza `yield` para criar um iterador de dados, evitando o carregamento total de arquivos na RAM.
**[EN]** Uses `yield` to create a data iterator, avoiding full file loading into RAM.

O(1) Memory Footprint: Esta função entrega um registro por vez, mantendo o uso de memória constante.

### 2. Validation Layer (Pydantic)
**[PT]** Garante a integridade dos dados (Saneamento) antes que eles atinjam o motor de cálculo.  
**[EN]** Ensures data integrity (Sanitization) before it reaches the computation engine.

Data Validation: O Pydantic valida tipos e regras (ex: valor > 0) em tempo real.

### 3. Computation Engine (Polars/Rust)
**[PT]** Motor de processamento paralelo que utiliza a API Lazy do Polars para otimizar o plano de execução.  
**[EN]** Parallel processing engine utilizing Polars' Lazy API to optimize the execution plan.

Lazy Evaluation: Otimização multithreading em Rust que processa dados apenas quando necessário.

---

###  Conceitos Aplicados / Concepts Applied

* **Lazy Evaluation:** [PT] Cálculos só são processados no momento do `.collect()`, otimizando CPU. [EN] Calculations are only processed at `.collect()`, optimizing CPU.
* **Batch Processing:** [PT] Processamento em lotes (ex: 10.000) para maximizar o throughput entre Python e Rust. [EN] Batch processing (e.g., 10,000) to maximize throughput between Python and Rust.
* **Type Safety:** [PT] Tipagem forte garantida pelo Pydantic para evitar "lixo" no pipeline. [EN] Strong typing guaranteed by Pydantic to prevent "garbage" in the pipeline.
* **Memory Management:** [PT] Garantia de complexidade de espaço O(1) independente do tamanho do dataset. [EN] Guarantee of O(1) space complexity regardless of dataset size.

---

###  Estrutura de Pastas / Folder Structure

/
├── main.py              # Orquestrador do Pipeline (Orchestrator)
├── polars_etl.py        # Motor de Processamento (Polars Engine)
├── stream_processor.py  # Gerador/Simulador de Dados (Data Stream)
├── .gitignore           # Exclusão de cache e logs (__pycache__, logs/)
└── logs/                # Telemetria e Auditoria (Audit & Debug logs)

---

###  Aviso Importante / Important Notice

> **[PT-BR]** Este repositório é uma **demonstração técnica** acadêmica e profissional. O objetivo é ilustrar conceitos de Engenharia de Software, como processamento O(1), integração Python-Rust e validação rigorosa.
> 
> **[EN]** This repository is a professional and academic **technical demonstration**. The goal is to illustrate Software Engineering concepts such as O(1) processing, Python-Rust integration, and rigorous validation.

---

###  Como Executar / How to Run

1. **Instale as dependências / Install dependencies:**
pip install polars pydantic

2. **Execute o pipeline / Run the pipeline:**
python main.py
