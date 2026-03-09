# 🛠️ 5-Drivers: Low-Level I/O & IPC

Interfaces de comunicação de alta fidelidade com o ecossistema externo.

### 🔗 Demonstração: The IPC Bridge
* **Protocol:** Implementação de **Unix Domain Sockets** (`AF_UNIX`) para comunicação entre processos.
* **Performance:** Bypass da pilha TCP/IP do kernel para latência em microssegundos.
