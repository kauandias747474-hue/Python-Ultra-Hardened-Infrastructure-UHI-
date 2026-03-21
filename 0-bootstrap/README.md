#  0-Bootstrap: System Sanity & Initialization


---

## 🇧🇷 [PT-BR] Descrição do Módulo

Responsável pela **Injeção de Dependências de Ambiente** e validação atômica de pré-requisitos. Esta camada atua como o firewall lógico do ecossistema UHI, garantindo que o Kernel (`1-engine`) só seja instanciado em um ambiente validado e seguro.

---

## 🔌 Protocolo de Conectividade (The Handshake)

Para manter o design **Vanilla-First** e o desacoplamento, a conexão entre os arquivos segue uma hierarquia rigorosa:

### 1. Conexão `bootstrap.py` ➔ `container.py`
* **O Gatilho:** O `bootstrap.py` é o primeiro a ser executado. Ele valida o hardware e o OS.
* **A Ponte:** Somente após o `resource.setrlimit` (trava de RAM) ser aplicado com sucesso, o `bootstrap.py` instancia o `Container` do `container.py`.
* **A Lógica:** Se o bootstrap falhar, o container nunca é criado, impedindo que qualquer driver (pasta 5) ou banco de dados (pasta 8) aloque memória.

### 2. Conexão `container.py` ➔ `1-engine`
* **O Gatilho:** O `main.py` (na pasta apps) solicita a `Engine` ao `Container`.
* **A Ponte:** O `container.py` faz o "Wiring" (fiação). Ele lê as configurações validadas pelo Pydantic e injeta as instâncias dos drivers e protocolos diretamente no construtor da Engine.
* **A Lógica:** A Engine recebe tudo pronto. Ela não dá `import` no banco de dados; ela recebe o objeto de banco de dados já aberto e validado pelo Container.

### 3. Conexão com Pastas Externas (2 a 9)
* **O Gatilho:** O `container.py` usa **Lazy Loading** (carregamento tardio).
* **A Ponte:** Ele só importa módulos como `8-storage` ou `5-drivers` no momento em que a aplicação realmente precisa deles, mantendo o consumo de memória inicial (Cold Start) o mais baixo possível.

---

## 🏗️ Estrutura de Código & Conceitos Aplicados

#### **`bootstrap.py` (Fluxo de Execução - 100+ Linhas)**
* **Conceitos de Python Aplicados:**
    * **Context Managers (`__enter__`/`__exit__`):** Proteção de recursos do SO.
    * **Custom Exception Hierarchy:** Erros granulares para falhas de hardware vs falhas de software.
    * **Type Guarding:** Verificação de tipos em runtime para estados críticos.

#### **`container.py` (Matriz de Dependências - 100+ Linhas)**
* **Conceitos de Programação Aplicados:**
    * **Inversion of Control (IoC):** Centralização da criação de objetos.
    * **Singleton Pattern:** Garantia de que recursos globais não sejam duplicados.
    * **Abstract Base Classes (ABC):** Definição de interfaces para garantir que qualquer driver injetado seja compatível.

---

## 🇺🇸 [EN] Module Description & Connectivity

### 🔌 Connectivity Protocol (The Handshake)

1.  **`bootstrap.py` ➔ `container.py`:** The bootstrap validates OS/Hardware first. Only after successful hardening (`setrlimit`) is the DI Container instantiated.
2.  **`container.py` ➔ `1-engine`:** The `main.py` requests the Engine from the Container. The Container injects all necessary drivers/protocols into the Engine’s constructor.
3.  **External Folders (2 to 9):** The Container uses **Lazy Loading** to import specialized modules only when required, optimizing the **Cold Start**.

---

##  Stack Técnica / Technical Stack

| Camada / Layer | Ferramenta / Tool | Conceito Aplicado / Applied Concept |
| :--- | :--- | :--- |
| **Validation** | `Pydantic V2` | Data Integrity & Strict Typing. |
| **Settings** | `Dynaconf` | 12-Factor App Config & Environment Management. |
| **IoC / DI** | `Dependency Injector` | Decoupling & Modular Architecture. |
| **Logging** | `Loguru` | Structured Logging & Boot Interception. |
| **OS Control** | `resource` | Sandboxing & Kernel-level Hardening (POSIX). |

---

## Evidências de Engenharia / Engineering Proofs

* **Fail-Fast Design:** Immediate process termination if sanity checks fail.
* **Zero-Copy Intent:** Memory buffers prepared in Bootstrap to avoid re-allocation.
* **Vanilla-First Core:** Clean, high-performance logic with minimal overhead.

> **⚠️ UHI Constraint:**
> [PT] Proibido o início da `1-engine` sem a validação atômica desta camada.
> [EN] Starting `1-engine` is strictly prohibited without the atomic validation of this layer.
