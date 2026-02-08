# 🔌 Drivers Layer

Abstrações puras para interação com o mundo exterior. Aqui o Python conversa diretamente com o Sistema Operacional e Hardware.

### Componentes:
* **FileSystem Driver:** Operações de I/O otimizadas e seguras.
* **Network Sockets:** Comunicação via TCP/UDP pura (Vanilla).
* **OS Interface:** Chamadas de sistema (`os`, `sys`, `shutil`) encapsuladas para evitar dependência de plataforma.

> **Princípio:** Interfaceie com o hardware, mas mantenha o código agnóstico.
