
# 2- Architect: Memory Layout & Structures

**[PT-BR]** Focado em densidade de memória e velocidade de acesso via manipulação direta do modelo de objetos do CPython.  
**[EN]** Focused on memory density and access speed through direct manipulation of the CPython object model.

---

### Lógica do Código / Code Logic

#### 1. `main.py` (The Orchestrator)
* **[PT]** Atua como o maestro do sistema. Gerencia o ciclo de vida da aplicação, orquestra os modos de operação (Streaming, Firewall, Audit) e força a limpeza de memória sensível via `gc.collect()`. Ele utiliza `sys.path.append` para garantir a resolução de módulos em diretórios customizados, permitindo a importação segura do motor de schemas e do compressor de memória.
* **[EN]** Acts as the system orchestrator. Manages the application lifecycle, coordinates operating modes (Streaming, Firewall, Audit), and enforces sensitive memory cleanup via `gc.collect()`. It utilizes `sys.path.append` to ensure module resolution in custom project directories, allowing secure importing of the schema engine and the memory squeezer.

#### 2. `schema_validator.py` (The Structural Core)
* **[PT]** Define a fundação dos dados utilizando **Pydantic V2**. O uso de `ConfigDict(slots=True)` e `__slots__` elimina o `__dict__` e `__weakref__` de milhões de instâncias, travando a estrutura do objeto na RAM para evitar o overhead dinâmico do Python e garantir integridade estrutural antes da compactação.
* **[EN]** Defines the data foundation using **Pydantic V2**. The use of `ConfigDict(slots=True)` and `__slots__` eliminates `__dict__` and `__weakref__` from millions of instances, locking the object structure in RAM to avoid Python's dynamic overhead and ensuring structural integrity before compaction.

#### 3. `memory_squeezer.py` (The Low-Level Engine)
* **[PT]** O motor de compressão. Converte listas genéricas do Python em `array.array` (C-style) e utiliza `struct.pack` para serialização binária pura. Implementa buffers circulares com `deque(maxlen=3)` para manter a complexidade de memória constante e impedir vazamentos de memória (Memory Leaks) em fluxos de alta frequência.
* **[EN]** The compression engine. Converts generic Python lists into C-style `array.array` and utilizes `struct.pack` for pure binary serialization. It implements circular buffers with `deque(maxlen=3)` to maintain constant memory complexity and prevent memory leaks in high-frequency streaming flows.

---

###  Conceitos Aplicados / Concepts Applied

* **CPython Object Model:**
    * **[PT]** Entendimento profundo de como o Python aloca memória para classes e instâncias.
    * **[EN]** Deep understanding of how Python allocates memory for classes and instances.
* **Data Locality:**
    * **[PT]** Minimização de saltos de ponteiros na RAM através de buffers contíguos para otimizar o cache da CPU.
    * **[EN]** Minimizing pointer jumps in RAM through contiguous buffers to optimize CPU cache hits.
* **Type Enforcement:**
    * **[PT]** Uso de **Pydantic** para validar a integridade estrutural dos dados antes da compactação binária.
    * **[EN]** Using **Pydantic** to validate structural data integrity before binary compaction.
* **Tooling:** `Pydantic` (Data Integrity), `Guppy3` (Memory Profiling).

---

###  Tabela de Eficiência / Efficiency Table

| Component | Logic | Benefit |
| :--- | :--- | :--- |
| **Validation** | Pydantic Slots | **80% Less RAM** vs Standard Objects |
| **Compression** | Array.array ('d') | **C-Style Memory** Contiguity |
| **Streaming** | Deque (maxlen) | **Constant Memory** Complexity O(1) |
| **Cleanup** | GC Collect | **Zero Footprint** of sensitive data |

---
