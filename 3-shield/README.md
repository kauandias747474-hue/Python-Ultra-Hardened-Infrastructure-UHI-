# ⚡ 3-Strategy: Deterministic Execution Logic

[PT-BR]
Camada de decisão de alto nível baseada em estados finitos. Aqui, a lógica de negócio é traduzida em um fluxo determinístico, garantindo que o sistema nunca entre em estados inválidos ou execute comandos conflitantes.

[EN]
High-level decision layer based on finite states. Here, business logic is translated into a deterministic flow, ensuring the system never enters invalid states or executes conflicting commands.

---

## 🤖 Demonstração / Demonstration: The State-Machine Autómata

O foco desta implementação é o controle rigoroso de sequenciamento, essencial para automação industrial, robótica e sistemas críticos.

### Lógica e Segurança / Logic & Safety:

* **Atomic Transitions:**
    * [PT-BR] Bloqueio de comandos conflitantes em tempo de execução. A transição de estado é atômica; o sistema valida a pré-condição antes de permitir qualquer mudança, eliminando *race conditions* lógicas.
    * [EN] Runtime locking of conflicting commands. State transition is atomic; the system validates pre-conditions before allowing any change, eliminating logical race conditions.

* **FSM (Finite State Machine) Architecture:**
    * [PT-BR] Fluxo de automação desacoplado. A lógica de transição é separada da execução, facilitando testes unitários de comportamento e garantindo rastreabilidade total.
    * [EN] Decoupled automation flow. Transition logic is separated from execution, facilitating behavioral unit testing and ensuring full traceability.

* **Focus:**
    * [PT-BR] Sequenciamento de tarefas complexas e automação industrial (ex: protocolos de segurança e braços robóticos).
    * [EN] Complex task sequencing and industrial automation (e.g., safety protocols and robotic arms).



---

## 🔍 O Código Demonstrativo / The Demo Code

### [PT-BR] O que este código prova?
1. **Validation Engine:** O código demonstra um verificador que impede, por exemplo, que um motor seja ligado enquanto o sistema está em estado de "Erro" ou "Manutenção".
2. **Deterministic Flow:** Cada entrada gera exatamente uma saída previsível, facilitando auditorias de segurança e logs de conformidade.
3. **State Traceability:** Um histórico de transições leve que permite o "replay" de eventos para depuração (Debugging) de sistemas em produção.

### [EN] What does this code prove?
1. **Validation Engine:** The code demonstrates a checker that prevents, for example, a motor from being started while the system is in an "Error" or "Maintenance" state.
2. **Deterministic Flow:** Each input generates exactly one predictable output, facilitating safety audits and compliance logging.
3. **State Traceability:** A lightweight transition history that allows event "replay" for debugging production systems.
