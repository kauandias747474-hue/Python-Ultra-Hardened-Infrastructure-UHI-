#  9-Protocols: Binary Wire Logic


[PT-BR] Substituição de JSON por protocolos binários compactos e determinísticos.
[EN] Replacing JSON with compact, deterministic binary protocols.

---

##  Lógica do Código / Code Logic

1.  **Binary Packing:**
    * [PT] Uso do módulo `struct` para serialização de alta densidade.
    * [EN] Using the `struct` module for high-density serialization.
2.  **Fast Serialization (Msgpack):**
    * [PT] Integração com **MessagePack** para suporte a estruturas dinâmicas em alta velocidade.
    * [EN] Integration with **MessagePack** for high-speed dynamic structure support.

##  Conceitos Aplicados / Concepts Applied

* **Endianness:** [PT] Ordem de bytes em sistemas distribuídos. [EN] Byte order in distributed systems.
* **Serialization Overhead:** [PT] Minimização do custo de CPU na conversão de dados. [EN] Minimizing CPU cost in data conversion.
* **Framework:** `msgpack`, `struct` (Vanilla).
