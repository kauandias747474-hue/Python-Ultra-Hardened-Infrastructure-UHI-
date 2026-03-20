#  6-Telemetry: Systemic Observability

[PT-BR] Extração de métricas profundas de hardware e interpretador em tempo real.
[EN] Real-time deep hardware and interpreter metrics extraction.

---

##  Lógica do Código / Code Logic

1.  **OS Resource Inspection:**
    * [PT] Monitoramento de Context-Switches e falhas de página via `resource`.
    * [EN] Monitoring Context-Switches and page faults via `resource`.
2.  **Exposition (Prometheus):**
    * [PT] Uso de **prometheus_client** para expor métricas internas para dashboards.
    * [EN] Using **prometheus_client** to expose internal metrics to dashboards.

##  Conceitos Aplicados / Concepts Applied

* **Observability vs Monitoring:** [PT] Entendimento do estado interno via saídas. [EN] Understanding internal state through outputs.
* **Context Switching:** [PT] Medição de interrupções de CPU. [EN] Measuring CPU interruptions.
* **Framework:** `Prometheus Client`, `psutil` (System metrics).
