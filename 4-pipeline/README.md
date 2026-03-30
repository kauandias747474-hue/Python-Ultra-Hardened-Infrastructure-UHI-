#  4-Pipeline O(1) Stream Engine

**[PT-BR]** Pipeline de dados de alta performance projetado para processar volumes massivos com uso constante de memória (O(1)) e validação rigorosa via Pydantic e Polars (Rust-based).

**[EN]** High-performance data pipeline designed to process massive volumes with constant memory usage (O(1)) and rigorous validation via Pydantic and Polars (Rust-based).

---

##  Arquitetura do Sistema / System Architecture

O projeto segue os princípios de **Clean Architecture** e **Separation of Concerns**, dividindo-se em três camadas independentes:
The project follows **Clean Architecture** and **Separation of Concerns** principles, divided into three independent layers:

### 1. Data Ingestion (Generators)
**[PT]** Utiliza `yield` para criar um iterador de dados, evitando o carregamento total de arquivos na RAM.
**[EN]** Uses `yield` to create a data iterator, avoiding full file loading into RAM.

**O(1) Memory Footprint:** Esta função entrega um registro por vez, mantendo o consumo de recursos estável independente do tamanho do arquivo original.

### 2. Validation Layer (Pydantic)
**[PT]** Garante a integridade dos dados (Saneamento) antes que eles atinjam o motor de cálculo.  
**[EN]** Ensures data integrity (Sanitization) before it reaches the computation engine.

**Data Validation:** O Pydantic valida tipos e regras de negócio (ex: valor > 0) em tempo real, servindo como uma barreira de segurança para o pipeline.

### 3. Computation Engine (Polars/Rust)
**[PT]** Motor de processamento paralelo que utiliza a API Lazy do Polars para otimizar o plano de execução.  
**[EN]** Parallel processing engine utilizing Polars' Lazy API to optimize the execution plan.

**Lazy Evaluation:** Otimização multithreading em Rust que processa dados de forma vetorizada apenas quando o resultado final é solicitado.

---

##  Conceitos Aplicados / Concepts Applied

* **Lazy Evaluation:** [PT] Cálculos só são processados no momento do final, otimizando o uso de CPU. [EN] Calculations are only processed at the final stage, optimizing CPU usage.
* **Batch Processing:** [PT] Processamento em lotes (ex: 10.000) para maximizar a velocidade de comunicação entre Python e Rust. [EN] Batch processing (e.g., 10,000) to maximize throughput between Python and Rust.
* **Type Safety:** [PT] Tipagem forte garantida para evitar que dados corrompidos entrem no fluxo. [EN] Strong typing guaranteed to prevent corrupted data from entering the stream.
* **Memory Management:** [PT] Garantia de complexidade de espaço O(1) para processar datasets maiores que a memória RAM disponível. [EN] Guarantee of O(1) space complexity to process datasets larger than available RAM.

---

##  Estrutura de Pastas / Folder Structure

/
├── main.py              # Orquestrador do Pipeline (Orchestrator)
├── polars_etl.py        # Motor de Processamento (Polars Engine)
├── stream_processor.py  # Gerador de Dados (Data Stream)
├── .gitignore           # Exclusão de cache e logs
└── logs/                # Auditoria e Debug logs

---
##  Aviso Importante / Important Notice

> **[PT-BR]** Este repositório é uma **demonstração técnica** acadêmica e profissional. O objetivo é ilustrar conceitos de Engenharia de Software, como processamento O(1), integração Python-Rust e validação rigorosa.
> 
> **[EN]** This repository is a professional and academic **technical demonstration**. The goal is to illustrate Software Engineering concepts such as O(1) processing, Python-Rust integration, and rigorous validation.

---

##  Como Executar / How to Run

1. **Instale as dependências / Install dependencies:**
pip install polars pydantic

2. **Execute o pipeline / Run the pipeline:**
python main.py
