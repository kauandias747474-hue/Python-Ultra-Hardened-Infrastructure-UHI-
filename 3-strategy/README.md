## 3-Strategy: Deterministic Execution Logic & System Resilience

### [PT-BR]
Camada de decisão baseada em Máquinas de Estados Finitos (FSM) e Mutex Locks para garantir um fluxo de execução determinístico, livre de *race conditions* e resiliente a interrupções do Sistema Operacional.

**Nota Importante:** Este repositório é uma **demonstração técnica de conceitos aplicados**. O código atual serve como Prova de Conceito (PoC) para validar a arquitetura lógica de um motor forense. No momento, considero que o código ainda necessita de refatorações profundas; ele passará por revisões constantes para atingir o padrão de "blindagem" (hardening).
### [EN]
Decision layer based on Finite State Machines (FSM) and Mutex Locks to ensure deterministic execution flow, free of race conditions, and resilient to Operating System interrupts.

**Important Note:** This repository is a **technical demonstration of applied concepts**. The current code serves as a Proof of Concept (PoC) to validate the logical architecture of a forensic engine. At the moment, I consider the code in need of deep refactoring; it will undergo constant revisions to reach the "hardening" .

---

## 🛠 Arquitetura e Implementação / Architecture & Implementation

### 1. Atomic Transitions (Mutex Guarding)
* **Por que usei?** Em sistemas multi-thread, o fenômeno de *Race Condition* (Condição de Corrida) pode corromper o estado da memória. Se duas threads tentarem mudar o estado do Sentinel ao mesmo tempo, o sistema entraria em colapso lógico ou sofreria um *crash*.
* **Como usei?** Implementei um **Mutex (Mutual Exclusion)** usando `threading.Lock()`. Isso garante que apenas uma thread por vez possa acessar o recurso crítico de transição de estado.
* **Why?** To prevent Race Conditions in multi-threaded environments that could lead to memory corruption.
* **How?** Using `threading.Lock()` to ensure that only one thread can access the state transition at a time.

def transit(self, next_state):
    with self._lock:  # Garante atomicidade: o lock abre mesmo se houver erro
        self._state = next_state 

### 2. Deterministic FSM (Safety Circuit)
* **Por que usei?** Para eliminar a imprevisibilidade. Um software de Forensics não pode permitir que uma análise (`ANALYZING`) comece sem que um scan (`SCANNING`) tenha sido disparado. A FSM impõe uma "hierarquia de eventos".
* **Como usei?** Utilizei a biblioteca `Transitions` para mapear um grafo onde o estado futuro é dependente e validado pelo estado anterior.
* **Why?** To eliminate unpredictability and enforce a strict event hierarchy.
* **How?** Using the `Transitions` framework to map a state graph where future states are validated by the current one.

# Exemplo de Transição Segura / Safe Transition Example:
self.machine.add_transition('analyze', 'SCANNING', 'ANALYZING')

### 3. Signal Resilience (Kernel Communication)
* **Por que usei?** Softwares de baixo nível precisam respeitar os sinais do Kernel (POSIX). Se o Sentinel for interrompido bruscamente (Ctrl+C), ele pode deixar travas (locks) abertas na RAM ou arquivos corrompidos.
* **Como usei?** Implementei o módulo `signal` para interceptar `SIGINT` (interrupção de teclado) e realizar um encerramento limpo (Graceful Shutdown).
* **Why?** To respect Kernel POSIX signals and prevent stale locks or corrupted files upon sudden termination.
* **How?** Using the `signal` module to intercept `SIGINT` and trigger a Graceful Shutdown.

### 4. Anti-Forensics & Memory Hygiene
* **Por que usei?** O Python gerencia memória de forma automática, mas objetos sensíveis podem "sobreviver" no heap da RAM por tempo indeterminado. Em um contexto forense, isso é uma vulnerabilidade de vazamento de dados.
* **Como usei?** Criei a rotina `hard_reset` invocando o Garbage Collector (`gc.collect()`) de forma forçada e síncrona para limpar trilhas de memória.
* **Why?** To minimize the persistence of sensitive data in RAM (Anti-Forensics).
* **How?** Implementing a `hard_reset` routine that forces synchronous Garbage Collection.

---

##  Resumo de Conceitos Aplicados / Applied Concepts Summary

| Conceito / Concept | Aplicação / Application | Objetivo / Goal |
| :--- | :--- | :--- |
| **Mutex Lock** | `threading.Lock()` | Integridade da RAM / RAM Integrity. |
| **FSM** | `Transitions Framework` | Fluxo Determinístico / Deterministic Flow. |
| **Signal Handling** | `signal.SIGINT` | Resiliência de S.O. / O.S. Resilience. |
| **GC Hygiene** | `gc.collect()` | Anti-Forensics / Minimize RAM traces. |

---
