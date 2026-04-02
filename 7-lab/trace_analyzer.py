import os 
import subprocess 
import sys 
import shutil 
import platform 
from datetime import datetime

def run_7lab_trace():

    print("--- 7-LAB: SISTEMA DE TELEMETRIA AVANÇADA ---")
    print(f"Node: {platform.node()} | OS: {platform.system()} {platform.release()}")
    print(f"Processador: {platform.processor()}")
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 45)
    
    print(" [7-LAB] Iniciando Microscopia de Execução...")
    
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"7lab_report_{timestamp}.json"
    

    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
        print(" [7-LAB] Cache de Bytecode limpo para teste puro.")

    try:
        print(f" [7-LAB] Rastreando main.py...")
        
     
        subprocess.run([
            "viztracer", 
            "--log_multiprocessing", 
            "--output_file", output_file, 
            "main.py"
        ], check=True)
        
        print(f"\n Rastreamento concluído: {output_file}")
        
  
        file_size = os.path.getsize(output_file) / (1024 * 1024)
        print(f" [7-LAB] Tamanho do dump de telemetria: {file_size:.2f} MB")
        
        print(" [7-LAB] Abrindo o Flame Graph no navegador...")
        subprocess.run(["vizviewer", output_file])
        
    except subprocess.CalledProcessError as e:
        print(f" Erro na execução do main.py: {e}")
    except FileNotFoundError:
        print(" Erro: VizTracer não instalado. Use: pip install viztracer")
    except Exception as e:
        print(f" Erro inesperado: {e}")

if __name__ == "__main__":
    run_7lab_trace()
