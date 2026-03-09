# 📊 6-Telemetry: Systemic Observability

Monitoramento de performance em nível de interpretador e hardware.

### 📈 Demonstração: The Context-Switch Counter
* **Metrics:** Captura de `ru_nvcsw` e `ru_nivcsw` via módulo `resource`.
* **Goal:** Identificar picos de latência causados por interrupções do Sistema Operacional.
