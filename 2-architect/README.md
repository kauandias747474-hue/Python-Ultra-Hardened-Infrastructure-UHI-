# 🏛️ 2-Architect: Memory Layout & Structures

[PT-BR]
Engenharia de dados focada em **densidade de memória** e **velocidade de acesso**. Este módulo demonstra como manipular o gerenciamento de objetos do Python para alcançar eficiência próxima a linguagens de baixo nível.

[EN]
Data engineering focused on **memory density** and **access speed**. This module demonstrates how to manipulate Python's object management to achieve efficiency close to low-level languages.

---

## 💎 Demonstração / Demonstration: The Memory Squeezer

O código foca na redução drástica do *footprint* de memória de grandes coleções de objetos através de técnicas de layout estrutural.

### Técnicas Aplicadas / Techniques Applied:

* **Exhaustive `__slots__` Usage:**
    * [PT-BR] Eliminação do `__dict__` e `__weakref__` internos. Ao fixar os atributos, o Python utiliza um array compacto em vez de um dicionário dinâmico, economizando memória e acelerando o acesso via `OFFSET`.
    * [EN] Elimination of internal `__dict__` and `__weakref__`. By fixing attributes, Python uses a compact array instead of a dynamic dictionary, saving memory and accelerating access via `OFFSET`.

* **`typing.Final` & Attribute Lookup:**
    * [PT-BR] Uso de `Final` para sinalizar ao interpretador e ferramentas de análise estática que o valor é constante, permitindo otimizações de busca e integridade de dados.
    * [EN] Using `Final` to signal the interpreter and static analysis tools that the value is constant, allowing for lookup optimizations and data integrity.

* **Memory Impact:**
    * [PT-BR] **Redução de ~60%** no overhead de RAM por objeto.
    * [EN] **~60% reduction** in RAM overhead per object.



---

## 🔍 O Código Demonstrativo / The Demo Code

### [PT-BR] O que este código prova?
1. **Memory Profiling:** O script utiliza `sys.getsizeof` e inspeção de referências para mostrar a diferença real em bytes entre uma classe padrão e uma classe otimizada.
2. **Access Speed:** Um benchmark de microsegundos comparando a velocidade de leitura/escrita em classes com e sem `__slots__`.
3. **Scale Test:** Demonstração da criação de 1 milhão de objetos, monitorando o heap de memória do sistema em tempo real.

### [EN] What does this code prove?
1. **Memory Profiling:** The script uses `sys.getsizeof` and reference inspection to show the actual byte difference between a standard class and an optimized class.
2. **Access Speed:** A micro-benchmark comparing read/write speeds in classes with and without `__slots__`.
3. **Scale Test:** Demonstration of creating 1 million objects, monitoring the system memory heap in real-time.
