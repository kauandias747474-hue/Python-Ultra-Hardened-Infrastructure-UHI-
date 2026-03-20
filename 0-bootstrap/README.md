#  0-Bootstrap: System Sanity & Initialization
#  0-Bootstrap: Sanidade do Sistema & Inicialização

[PT-BR] Responsável pela **Injeção de Dependências de Ambiente** e validação crítica de pré-requisitos. Esta camada atua como o **Gatekeeper** do ecossistema UHI, garantindo que o Kernel só seja instanciado em um ambiente validado.

[EN] Responsible for **Environment Dependency Injection** and critical prerequisite validation. This layer acts as the **Gatekeeper** of the UHI ecosystem, ensuring the Kernel is only instantiated in a validated environment.

---

## ⚙️ Lógica de Inicialização / Initialization Logic

[PT-BR] O código deste módulo implementa um fluxo atômico de 4 estágios:
[EN] This module's code implements a 4-stage atomic flow:

1.  **Environment Audit (Pydantic V2 & Dynaconf):**
    * [PT] Validação de Schema: Uso de **Pydantic** para garantir que as variáveis de ambiente sigam o contrato de segurança.
    * [EN] Schema Validation: Using **Pydantic** to ensure environment variables follow the security contract.
2.  **Resource Limiting (OS Hardening):**
    * [PT] Aplicação de travas via módulo `resource` (POSIX) para limitar RAM (`RLIMIT_AS`) e arquivos abertos (`RLIMIT_NOFILE`).
    * [EN] Applying locks via the `resource` module (POSIX) to limit RAM (`RLIMIT_AS`) and open files (`RLIMIT_NOFILE`).
3.  **Dependency Injection (IoC):**
    * [PT] Uso de **Dependency Injector** para desacoplar o motor principal de drivers e logs.
    * [EN] Using **Dependency Injector** to decouple the main engine from drivers and logs.
4.  **Cold Start Logic:**
    * [PT] Alocação de memória estática e preparação de buffers binários para evitar picos de latência (Jitter).
    * [EN] Static memory allocation and binary buffer preparation to avoid latency spikes (Jitter).



---

##  Frameworks & Ferramentas / Frameworks & Tools

| Camada / Layer | Ferramenta / Tool | Objetivo Técnico / Technical Goal |
| :--- | :--- | :--- |
| **Validation** | `Pydantic V2` | [PT] Validação em Rust / [EN] Rust-backed validation. |
| **Settings** | `Dynaconf` | [PT] Gestão de Configurações / [EN] Configuration Management. |
| **IoC / DI** | `Dependency Injector` | [PT] Inversão de Controle / [EN] Inversion of Control. |
| **Logging** | `Loguru` | [PT] Auditoria de Boot / [EN] Boot Auditing. |
| **OS Control** | `resource` | [PT] Limites de Kernel / [EN] Kernel Limits. |

---

##  O que este código prova? / What does this code prove?

* **Fail-Fast Design:** * [PT] O sistema interrompe a execução imediatamente se os pré-requisitos não forem atendidos.
    * [EN] The system halts execution immediately if prerequisites are not met.
* **Observability First:** * [PT] Logs de auditoria gerados antes da lógica de negócio.
    * [EN] Audit logs generated before business logic.
* **Modern Engineering:** * [PT] Demonstra o uso de **Inversão de Controle (IoC)**, padrão essencial para sistemas de missão crítica.
    * [EN] Demonstrates the use of **Inversion of Control (IoC)**, an essential pattern for mission-critical systems.



> **UHI Constraint:** > [PT] Proibido o início da `1-engine` sem a validação atômica desta camada.
> [EN] Starting `1-engine` is strictly prohibited without the atomic validation of this layer.
