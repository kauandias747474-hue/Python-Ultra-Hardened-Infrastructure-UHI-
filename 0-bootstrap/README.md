#  0-Bootstrap: System Sanity & Initialization



---

## 🇧🇷 [PT-BR] Descrição do Módulo

Responsável pela **Injeção de Dependências de Ambiente** e validação atômica de pré-requisitos. Esta camada atua como o firewall lógico do ecossistema UHI, garantindo que o Kernel (`1-engine`) só seja instanciado em um ambiente validado e seguro. 

### 🏗️ Estrutura de Código & Conceitos Aplicados

#### **`bootstrap.py` (Fluxo de Execução - 100+ Linhas)**
* **Conceitos de Python:**
    * **Context Managers (`__enter__`/`__exit__`):** Garantia de que as travas de recursos do SO sejam liberadas em caso de crash.
    * **Subprocess & OS Signals:** Captura de sinais do sistema para encerramento limpo.
    * **Custom Exception Hierarchy:** Criação de uma árvore de exceções (`BootstrapError` -> `ResourceLimitError`) para diagnóstico preciso.
    * **Type Guarding:** Uso de `TypeGuard` do módulo `typing` para validar estados do sistema em runtime.

#### **`container.py` (Matriz de Dependências - 100+ Linhas)**
* **Conceitos de Programação:**
    * **Inversion of Control (IoC):** Centralização da criação de objetos, removendo o `import` direto de implementações na Engine.
    * **Singleton Pattern:** Uso de escopo `Singleton` do `dependency_injector` para evitar múltiplas alocações de memória global.
    * **Declarative Wiring:** Mapeamento de instâncias de `Drivers`, `Storage` e `Protocols`.
    * **Abstract Base Classes (ABC):** Uso do módulo `abc` para definir contratos que os drivers (pasta 5) devem obrigatoriamente seguir.

---

## 🇺🇸 [EN] Module Description

Responsible for **Environment Dependency Injection** and atomic prerequisite validation. This layer acts as the logical firewall of the UHI ecosystem, ensuring the Kernel (`1-engine`) is only instantiated in a validated and secure environment.

### 🏗️ Code Structure & Applied Concepts

#### **`bootstrap.py` (Execution Flow - 100+ Lines)**
* **Python Concepts:**
    * **Context Managers (`__enter__`/`__exit__`):** Ensures OS resource locks are released during crashes.
    * **Subprocess & OS Signals:** Captures system signals for graceful shutdown.
    * **Custom Exception Hierarchy:** Implementation of an exception tree (`BootstrapError` -> `ResourceLimitError`) for precise diagnostics.
    * **Type Guarding:** Utilizing `TypeGuard` from the `typing` module for runtime system state validation.

#### **`container.py` (Dependency Matrix - 100+ Lines)**
* **Programming Concepts:**
    * **Inversion of Control (IoC):** Centralizes object creation, removing direct implementation imports in the Engine.
    * **Singleton Pattern:** Using `Singleton` scope from `dependency_injector` to prevent multiple global memory allocations.
    * **Declarative Wiring:** Mapping instances of `Drivers`, `Storage`, and `Protocols`.
    * **Abstract Base Classes (ABC):** Utilizing the `abc` module to define contracts that drivers (folder 5) must strictly follow.

---

## ⚙️ Fluxo Atômico / Atomic Flow

1.  **Environment Audit:** Schema validation via **Pydantic V2** (Rust-backed performance).
2.  **Resource Limiting:** Kernel-level constraints using the **POSIX `resource` module** (`RLIMIT_AS`, `RLIMIT_NOFILE`).
3.  **Dependency Injection:** Dynamic wiring of the system components via `container.py`.
4.  **Cold Start Logic:** **Static Memory Pre-allocation** and binary buffer warm-up to eliminate **Jitter**.

---

## 🛠️ Stack Técnica / Technical Stack

| Camada / Layer | Ferramenta / Tool | Conceito Aplicado / Applied Concept |
| :--- | :--- | :--- |
| **Validation** | `Pydantic V2` | Data Integrity & Strict Typing / Integridade de Dados. |
| **Settings** | `Dynaconf` | 12-Factor App Config / Gestão de Configurações 12-Factor. |
| **IoC / DI** | `Dependency Injector` | Decoupling & Modular Architecture / Desacoplamento. |
| **Logging** | `Loguru` | Structured Logging & Interception / Logs Estruturados. |
| **OS Control** | `resource` | Sandboxing & Hardening / Limites de Processo. |

---

## Evidências de Engenharia / Engineering Proofs

* **Fail-Fast Design:** Immediate process termination upon validation failure.
* **Zero-Copy Intent:** Memory buffers prepared in the Bootstrap to avoid re-allocation in the Engine.
* **Vanilla-First Core:** Minimal external dependency footprint in the core validation logic.

> **⚠️ UHI Constraint:**
> [PT] Proibido o início da `1-engine` sem a validação atômica desta camada.
> [EN] Starting `1-engine` is strictly prohibited without the atomic validation of this layer.
