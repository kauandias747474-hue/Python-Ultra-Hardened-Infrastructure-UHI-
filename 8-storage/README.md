# 💾 8-Storage: Atomic Persistence & Mmap

I/O de disco otimizado para velocidade de RAM.

### 📂 Demonstração: The Mmap Fast-Read
* **Technique:** Mapeamento de arquivos binários diretamente na memória virtual via `mmap`.
* **Persistence:** Escrita atômica para prevenção de corrupção de dados em quedas de energia.
