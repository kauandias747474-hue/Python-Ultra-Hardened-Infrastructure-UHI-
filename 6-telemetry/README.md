# 6-Telemetry

### 🇧🇷 [PT-BR] Resumo do Projeto
Este projeto implementa um sistema de telemetria em tempo real para monitoramento de recursos de hardware e métricas do interpretador Python. A aplicação utiliza uma arquitetura multithread para garantir que a coleta e exposição de dados ocorram em paralelo à execução da tarefa principal, sem impactar a performance.

### 🇺🇸 [EN] Project Overview
This project implements a real-time telemetry system for monitoring hardware resources and Python interpreter metrics. The application leverages a multithreaded architecture to ensure that data collection and exposition happen in parallel with the main task execution, without impacting performance.

---

##  Tecnologias / Technologies
* **Python 3.14+**
* **psutil**: Inspeção de recursos do sistema / System resources inspection.
* **prometheus_client**: Exposição de métricas / Metrics exposition.
* **Threading**: Execução concorrente / Concurrent execution.

---

##  Estrutura do Código / Code Structure

### 1. `system_monitor.py` (The Sensor)
* **PT**: Atua como a camada de abstração de hardware. Resolve disparidades entre Windows e Linux (usando `psutil` como fallback para o módulo `resource`) e extrai dados críticos como CPU, RAM, Context-Switches e Page Faults.
* **EN**: Acts as the hardware abstraction layer. It resolves Windows/Linux disparities (using `psutil` as a fallback for the `resource` module) and extracts critical data like CPU, RAM, Context-Switches, and Page Faults.

### 2. `metrics_explorer.py` (The Exporter)
* **PT**: Transforma dados brutos em métricas formatadas para o Prometheus. Cria um servidor HTTP na porta 8000 que expõe um endpoint `/metrics`.
* **EN**: Transforms raw data into Prometheus-formatted metrics. It creates an HTTP server on port 8000 that exposes a `/metrics` endpoint.

### 3. `main.py` (The Orchestrator)
* **PT**: O ponto de entrada que inicia o servidor de métricas em uma Thread secundária (`daemon=True`) e executa uma `heavy_task` para gerar carga de processamento real para monitoramento.
* **EN**: The entry point that starts the metrics server in a secondary Thread (`daemon=True`) and runs a `heavy_task` to generate real processing load for monitoring.

---

##  Conceitos Aplicados / Concepts Applied

* **Observability vs Monitoring**: 
    * [PT] Foco em entender o estado interno do sistema através das suas saídas externas (métricas).
    * [EN] Focused on understanding the system's internal state through its external outputs (metrics).
* **Context Switching & Page Faults**: 
    * [PT] Medição de interrupções de CPU e gerenciamento de memória virtual no Kernel.
    * [EN] Measuring CPU interruptions and virtual memory management within the Kernel.
* **Multithreading & Concurrency**: 
    * [PT] Uso de threads para evitar que o servidor de monitoramento bloqueie a execução da lógica de negócio.
    * [EN] Using threads to prevent the monitoring server from blocking the business logic execution.

---

##  Por que este código é interessante? / Why is this interesting?

[PT] *Embora seja um código demonstrativo, ele resolve problemas reais de engenharia, como a compatibilidade entre sistemas operacionais (Windows vs Linux) e o gerenciamento de concorrência. É uma prova de conceito de como sistemas de larga escala (SRE/DevOps) monitoram a saúde de milhares de servidores simultaneamente. É a transição de um "script simples" para uma "aplicação observável".*

[EN] *Although it is a demonstrative code, it solves real engineering problems, such as OS compatibility (Windows vs Linux) and concurrency management. It is a proof of concept of how large-scale systems (SRE/DevOps) monitor the health of thousands of servers simultaneously. It represents the transition from a "simple script" to an "observable application."*

---


##  Como Executar / How to Run

### 🇧🇷 Português
1. **Instale as dependências:**
   Abra o seu terminal e execute o comando abaixo:
*pip install psutil prometheus_client*


2. **Execute o sistema:**
No mesmo terminal, inicie o orquestrador do projeto:
*python main.py*


3. **Verifique os resultados:**
Abra o seu navegador e acesse o endereço:
*http://localhost:8000/metrics*

*Você verá as métricas brutas (Gauges) sendo atualizadas em tempo real a cada segundo.*

---

### 🇺🇸 English
1. **Install dependencies:**
Open your terminal and run the following command:
*pip install psutil prometheus_client*


2. **Run the system:**
In the same terminal, start the project orchestrator:
*python main.py*


3. **Check the results:**
Open your browser and navigate to:
*http://localhost:8000/metrics*

*You will see the raw metrics (Gauges) being updated in real-time every second.*

---
