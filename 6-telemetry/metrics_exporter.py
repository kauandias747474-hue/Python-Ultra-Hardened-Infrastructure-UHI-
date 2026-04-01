import time
import logging
from prometheus_client import Gauge, start_http_server
from system_monitor import get_system_metrics

CPU_GAUGE = Gauge('system_cpu_usage_percent', 'Uso de CPU em %')
RAM_GAUGE = Gauge('system_ram_usage_bytes', 'Uso de RAM em bytes')
CTX_GAUGE = Gauge('system_context_switches_total', 'Total de trocas de contexto')
FAULT_GAUGE = Gauge('system_page_faults_total', 'Total de falhas de página')

def run_exporter(port=8000):
    """Inicia o servidor e entra no loop de atualização."""
    # Inicia o servidor HTTP do Prometheus
    start_http_server(port)
    print(f"[*] Servidor de métricas ativo: http://localhost:{port}/metrics")
    
    while True:
        try:

            data = get_system_metrics()
     
            CPU_GAUGE.set(data['cpu_percent'])
            RAM_GAUGE.set(data['ram_used'])
            CTX_GAUGE.set(data['ctx_switches'])
            FAULT_GAUGE.set(data['page_faults'])
            
        
            print(f">>> Telemetria OK | CPU: {data['cpu_percent']}% | RAM: {data['ram_used']} bytes")
            
        except Exception as e:
            print(f"[!] Erro crítico na coleta: {e}")
            
        time.sleep(1) 
