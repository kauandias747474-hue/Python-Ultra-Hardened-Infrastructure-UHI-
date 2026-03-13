# 💾 8-Storage: Atomic Persistence & Mmap

[PT-BR]
I/O de disco otimizado para velocidade de RAM. Este módulo demonstra como manipular a memória virtual para realizar persistência de dados com latência ultra-baixa, eliminando o overhead de chamadas de sistema tradicionais de leitura e escrita.

[EN]
Disk I/O optimized for RAM speed. This module demonstrates how to manipulate virtual memory to achieve ultra-low latency data persistence, eliminating the overhead of traditional read and write system calls.

---

## 📂 Demonstração / Demonstration: The Mmap Fast-Read

O foco desta implementação é o acesso instantâneo a grandes volumes de dados persistidos e a garantia de integridade estrutural.

### Engenharia de Persistência / Persistence Engineering:

* **Technique (Memory Mapping):**
    * [PT-BR] Uso de `mmap` para mapear arquivos binários diretamente na memória virtual do processo. Isso permite que o SO gerencie o cache de páginas, tratando o arquivo como se fosse um array em RAM, o que acelera acessos aleatórios.
    * [EN] Using `mmap` to map binary files directly into the process's virtual memory. This allows the OS to manage page caching, treating the file as a RAM array, which accelerates random access.

* **Atomic Persistence:**
    * [PT-BR] Implementação de técnicas de escrita atômica (como *shadow paging* ou *WAL*) para prevenir a corrupção de arquivos em caso de quedas de energia ou travamentos do sistema.
    * [EN] Implementation of atomic writing techniques (such as shadow paging or WAL) to prevent file corruption during power failures or system crashes.

* **Binary Serialization:**
    * [PT-BR] Foco em layouts binários fixos, permitindo que o interpretador leia estruturas de dados sem a necessidade de parsing complexo de strings ou JSON.
    * [EN] Focus on fixed binary layouts, allowing the interpreter to read data structures without the need for complex string or JSON parsing.



---

## 🔍 O Código Demonstrativo / The Demo Code

### [PT-BR] O que este código prova?
1. **Instant Loading:** Demonstra como "abrir" um arquivo de múltiplos Gigabytes e acessar qualquer byte instantaneamente sem carregá-lo por completo na RAM.
2. **Zero-Copy Persistence:** Mostra a modificação de dados diretamente no mapa de memória, deixando que o Kernel sincronize o disco de forma assíncrona e eficiente.
3. **Crash Resilience:** Um exemplo de como garantir que, mesmo que o processo seja interrompido, o estado anterior do arquivo permaneça válido.

### [EN] What does this code prove?
1. **Instant Loading:** Demonstrates how to "open" a multi-Gigabyte file and access any byte instantly without loading it entirely into RAM.
2. **Zero-Copy Persistence:** Shows data modification directly in the memory map, letting the Kernel sync to disk asynchronously and efficiently.
3. **Crash Resilience:** An example of how to ensure that even if the process is interrupted, the previous file state remains valid.
