#  8-Storage: Atomic Persistence & Mmap

[PT-BR] I/O de disco com performance de RAM via Virtual Memory Mapping.
[EN] Disk I/O with RAM performance via Virtual Memory Mapping.

---

## ⚙️ Lógica do Código / Code Logic

1.  **Zero-Copy Persistence:**
    * [PT] Uso de `mmap` para manipular arquivos como arrays em RAM.
    * [EN] Using `mmap` to manipulate files as RAM arrays.
2.  **Validation (Checksums):**
    * [PT] Uso de **hashlib** para garantir integridade atômica pós-escrita.
    * [EN] Using **hashlib** to ensure atomic integrity post-write.

## 🔍 Conceitos Aplicados / Concepts Applied

* **Virtual Memory Map:** [PT] Mapeamento direto de arquivo em memória. [EN] Direct file-to-memory mapping.
* **Atomicity:** [PT] Garantia de "tudo ou nada" em operações de escrita. [EN] "All or nothing" guarantee in write operations.
* **Framework:** `mmap` (Vanilla), `hashlib`.
