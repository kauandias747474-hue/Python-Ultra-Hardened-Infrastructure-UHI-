#  3-Strategy: Deterministic Execution Logic


[PT-BR] Camada de decisão baseada em Estados Finitos (FSM) para garantir fluxo livre de race conditions.
[EN] Decision layer based on Finite State Machines (FSM) to ensure race-condition-free flow.

---

##  Lógica do Código / Code Logic

1.  **Atomic Transitions:**
    * [PT] Validação de pré-condições antes de qualquer mudança de estado no motor.
    * [EN] Pre-condition validation before any engine state change.
2.  **Safety Circuit (Transitions Framework):**
    * [PT] Uso da biblioteca **Transitions** para mapear grafos de estados complexos com triggers automáticos.
    * [EN] Using the **Transitions** library to map complex state graphs with automatic triggers.

##  Conceitos Aplicados / Concepts Applied

* **Finite State Machines (FSM):** [PT] Autômatos para controle de fluxo. [EN] Automata for flow control.
* **Immutability:** [PT] Garantia de que o estado não mude sem autorização. [EN] Ensuring state doesn't change without authorization.
* **Framework:** `Transitions` (FSM Engine), `Loguru` (Audit Trail).
