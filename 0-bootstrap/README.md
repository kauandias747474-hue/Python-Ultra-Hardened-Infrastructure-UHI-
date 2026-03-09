# 🚀 0-Bootstrap: System Sanity & Initialization

Responsável pela **Injeção de Dependências de Ambiente** e validação de pré-requisitos antes da subida do Kernel.

### ⚙️ Engine de Inicialização
* **Environment Audit:** Verificação de versão do CPython e flags de otimização.
* **Resource Limiting:** Definição de limites de memória e descritores de arquivo via `resource`.
* **Cold Start Logic:** Preparação de buffers iniciais e alocação de memória estática.

> **UHI Constraint:** Proibido o início da `1-engine` sem a validação atômica desta camada.
