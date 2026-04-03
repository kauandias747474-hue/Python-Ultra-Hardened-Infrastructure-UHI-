import mmap
import os
import sys
from schema import IndustrialData, RECORD_SIZE

class InstantSearch:
    """
    Classe Sniper: Localiza dados na RAM/Disco em tempo constante O(1).
    Não percorre o arquivo; ela calcula o pulo (offset) matemático.
    """
    def __init__(self, file_path="data.bin"):
        self.file_path = file_path

    def get_record_by_id(self, sensor_id: int):
      
        if not os.path.exists(self.file_path):
            print(f"❌ Erro: O arquivo '{self.file_path}' não existe. Rode o main.py primeiro.")
            return None

        offset = sensor_id * RECORD_SIZE
        
    
        file_size = os.path.getsize(self.file_path)
        if offset + RECORD_SIZE > file_size:
            print(f"⚠️ Erro: Sensor ID {sensor_id} está fora do limite do arquivo ({file_size} bytes).")
            return None

        with open(self.file_path, "rb") as f:
            try:
                
                mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                
                binary_chunk = mm[offset : offset + RECORD_SIZE]
                
                mm.close()
                
            
                return IndustrialData.unpack(binary_chunk)
                
            except Exception as e:
                print(f"❌ Falha técnica na leitura da RAM: {e}")
                return None

if __name__ == "__main__":
    """
    Permite rodar via terminal: python smart_search.py [ID]
    """
    if len(sys.argv) > 1:
        try:
            id_para_busca = int(sys.argv[1])
            

            scanner = InstantSearch()
            item = scanner.get_record_by_id(id_para_busca)
            
            if item:
                print("-" * 40)
                print(f"🎯 RESULTADO DA BUSCA SNIPER (O(1))")
                print("-" * 40)
                print(f"📡 Sensor ID : {item.sensor_id}")
                print(f"🌡️ Temperatura: {item.temp:.2f} °C")
                print(f"🌀 Pressão    : {item.press:.2f} bar")
                print("-" * 40)
            
        except ValueError:
            print("❌ Erro: O ID do sensor deve ser um número inteiro.")
    else:
        print("\n💡 Como usar o Sniper:")
        print("   python smart_search.py [ID_DO_SENSOR]")
        print("   Exemplo: python smart_search.py 5\n")
