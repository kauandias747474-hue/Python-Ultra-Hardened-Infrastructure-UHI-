# 7-Lab: Performance Benchmarking & Trace Analyzer
**[PT-BR]** Módulo de diagnóstico para validação de engenharia de software e análise de hardware.
**[EN]** Diagnostic module for software engineering validation and hardware analysis.

---

## Natureza do Módulo / Module Nature

**[PT-BR]** Este módulo do projeto foi desenvolvido como uma ferramenta de diagnóstico e experimentação técnica. Ele funciona como uma camada de observação sobre o interpretador Python, permitindo analisar como o computador processa dados, gerencia memória e utiliza múltiplos núcleos de processamento. O foco é fornecer visibilidade sobre as operações de baixo nível que ocorrem durante a execução do software.

**[EN]** This project module was developed as a tool for diagnostic and technical experimentation. It acts as an observation layer over the Python interpreter, allowing the analysis of how the computer processes data, manages memory, and utilizes multiple processing cores. The focus is to provide visibility into the low-level operations that occur during software execution.

---

## Estrutura e Conectividade / Structure & Connectivity

O projeto é dividido em três pilares que se comunicam para formar o diagnóstico completo:

### 1. O Núcleo de Execução (main.py)
Este é o "motor" do laboratório. Ele contém as implementações de cada conceito técnico (desde cálculos de rede até inferência de ML). 
* **Conexão:** Ele serve como o provedor de funções. Todos os outros arquivos importam as lógicas daqui para testá-las. Sem o `main.py`, não há o que medir ou analisar.

### 2. O Validador de Latência (latency_bench.py)
Este é o "cronômetro científico". Ele não possui lógica de negócio própria; ele importa as funções do `main.py` e as coloca sob estresse.
* **Conexão:** Ele usa as funções do núcleo para gerar a tabela comparativa. Ele prova, através de números, se a implementação feita no `main.py` é realmente eficiente ou se é apenas teoria.

### 3. O Analisador de Baixo Nível (Trace Analyzer / dis)
Integrado ao fluxo do núcleo, ele utiliza o módulo `dis` para abrir o "capô" das funções do `main.py`.
* **Conexão:** Enquanto o `latency_bench` foca no **tempo**, o Trace Analyzer foca na **causa**. Ele explica *por que* uma função foi lenta ou rápida ao mostrar as instruções que o Python enviou para a CPU.

---

## Mapa de Estudo: Os 20 Conceitos Aplicados

### Gestão de Memória (Eficiência de Espaço)

1. **__slots__**
   * **Localização:** `class ComSlots` no `main.py`.
   * **Conceito:** Substitui o dicionário flexível de atributos por uma estrutura estática, reduzindo o consumo de RAM.

2. **RAII (Resource Acquisition Is Initialization)**
   * **Localização:** `class LabResource` no `main.py`.
   * **Conceito:** Garante a liberação automática de recursos (limpeza de memória) ao sair de um bloco `with`.

3. **Localidade de Referência**
   * **Localização:** `run_array_int` no `main.py`.
   * **Conceito:** Dados contíguos na memória para acesso rápido via Cache da CPU.
   

4. **Zero-Copy (memoryview)**
   * **Localização:** `run_memory_view_test` no `main.py`.
   * **Conceito:** Manipulação de bytes apontando diretamente para o endereço original sem duplicar dados.

5. **Manual GC Control**
   * **Localização:** Bloco `if __name__ == "__main__"` no `main.py`.
   * **Conceito:** Desativa o Coletor de Lixo para evitar interferências durante medições de tempo.

### Alta Performance (Velocidade de Execução)

6. **Vetorização**
   * **Localização:** `run_ml_vectorized` no `main.py`.
   * **Conceito:** Cálculos em blocos simultâneos via NumPy para eliminar a lentidão de loops `for`.

7. **SIMD (Single Instruction, Multiple Data)**
   * **Localização:** Interno ao `numpy` no `main.py`.
   * **Conceito:** Processamento de múltiplos fluxos de dados com um único comando de hardware.
   

8. **Bitwise Logic**
   * **Localização:** `run_subnet_calc` no `main.py`.
   * **Conceito:** Operações binárias diretas na ALU (Unidade Lógica e Aritmética).

9. **IPC (Inter-Process Communication)**
   * **Localização:** `run_ipc_queue` no `main.py`.
   * **Conceito:** Canal de transporte de dados entre núcleos independentes da CPU via `Queue`.

10. **Serialização Rust-Backed**
    * **Localização:** `run_json_rust` no `main.py`.
    * **Conceito:** Uso de bibliotecas compiladas em Rust (`orjson`) para I/O ultra-veloz.

### Algoritmos e Complexidade (Lógica Estrutural)

11. **Hash Tables O(1)**
    * **Localização:** `run_set_search` no `main.py`.
    * **Conceito:** Busca instantânea independente do volume de dados.

12. **Busca Linear O(n)**
    * **Localização:** `run_list_search` no `main.py`.
    * **Conceito:** Demonstra a perda de performance em listas conforme o volume de dados cresce.

13. **Lazy Evaluation**
    * **Localização:** `run_generator_memory` no `main.py`.
    * **Conceito:** Geração de dados sob demanda para manter o consumo de RAM estável.

14. **Memoization**
    * **Localização:** `@lru_cache` no `main.py`.
    * **Conceito:** Cache de resultados anteriores para evitar cálculos repetitivos.

### Engenharia de Sistemas (Interação com o SO)

15. **Spawn Method**
    * **Localização:** Início do bloco principal no `main.py`.
    * **Conceito:** Criação segura de processos no Windows, evitando corrupção de memória.

16. **GIL Bypass**
    * **Localização:** `run_multiprocessing_test` no `main.py`.
    * **Conceito:** Uso de múltiplos processos para ignorar a trava global do Python.
    

17. **Bytecode Analysis**
    * **Localização:** Chamadas `dis.dis()` no final do `main.py`.
    * **Conceito:** Desmontagem do código em Opcodes para validar a eficiência do interpretador.

18. **Variable Scoping**
    * **Localização:** Comparação `run_local_access` vs `run_global_access` no `main.py`.
    * **Conceito:** Prova que variáveis locais usam instruções mais rápidas (`LOAD_FAST`).

19. **Micro-benchmarking**
    * **Localização:** Inteiro no `latency_bench.py`.
    * **Conceito:** Medição de fragmentos de código com alta precisão temporal e estatística.

20. **Introspecção de Ambiente**
    * **Localização:** Uso do módulo `platform` no `main.py`.
    * **Conceito:** Detecção automática das propriedades do hardware e SO para ajuste de execução.

---

## Conclusão de Estudo

**[PT-BR]**
A conexão entre esses arquivos permite que você mude algo no `main.py` e veja instantaneamente o impacto no `latency_bench.py` (tempo) e no Bytecode (lógica de máquina). Este módulo transforma a programação em um ciclo de engenharia: implementar, medir e analisar.

**[EN]**
The connection between these files allows you to change something in `main.py` and instantly see the impact on `latency_bench.py` (time) and Bytecode (machine logic). This module transforms programming into an engineering cycle: implement, measure, and analyze.

---

## Instruções de Uso

1. Prepare o ambiente: `pip install numpy orjson pytest-benchmark`.
2. Execute `python main.py` para verificar o diagnóstico e o Bytecode das funções.
3. Execute `pytest latency_bench.py` para analisar as métricas comparativas de latência.
