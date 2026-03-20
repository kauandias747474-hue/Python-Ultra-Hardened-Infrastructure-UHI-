#  2-Architect: Memory Layout & Structures


[PT-BR] Focado em densidade de memória e velocidade de acesso via manipulação direta do modelo de objetos do CPython.
[EN] Focused on memory density and access speed through direct manipulation of the CPython object model.

---

## ⚙️ Lógica do Código / Code Logic

1.  **Memory Squeezer (Slots Implementation):**
    * [PT] Uso exaustivo de `__slots__` para eliminar o `__dict__` e `__weakref__` de milhões de instâncias.
    * [EN] Exhaustive use of `__slots__` to eliminate `__dict__` and `__weakref__` from millions of instances.
2.  **Type Enforcement (Pydantic & Annotated):**
    * [PT] Uso de **Pydantic** para validar a integridade estrutural dos dados antes da compactação.
    * [EN] Using **Pydantic** to validate structural data integrity before compaction.

##  Conceitos Aplicados / Concepts Applied

* **CPython Object Model:** [PT] Entendimento de como o Python aloca memória para classes. [EN] Understanding how Python allocates memory for classes.
* **Data Locality:** [PT] Minimização de saltos de ponteiros na RAM. [EN] Minimizing pointer jumps in RAM.
* **Framework:** `Pydantic` (Data Integrity), `Guppy3` (Memory Profiling).
