import struct
import mmap


STRUCT_FORMAT = "i f d" 
RECORD_SIZE = struct.calcsize(STRUCT_FORMAT)

class IndustrialData:
    """Objeto que traduz bytes da RAM para variáveis Python."""
    def __init__(self, sensor_id, temp, press):
        self.sensor_id = int(sensor_id)
        self.temp = float(temp)
        self.press = float(press)

    def pack(self):
        """Empacota os dados para salvar na memória."""
        return struct.pack(STRUCT_FORMAT, self.sensor_id, self.temp, self.press)
    
    @classmethod
    def unpack(cls, data_bytes):
        """Desempacota os bytes lidos da memória."""
        try:
            if not data_bytes or len(data_bytes) < RECORD_SIZE:
                return cls(0, 0.0, 0.0)
            unpacked = struct.unpack(STRUCT_FORMAT, data_bytes)
            return cls(unpacked[0], unpacked[1], unpacked[2])
        except (struct.error, Exception):
            return cls(0, 0.0, 0.0)

class DoubleBuffer:
    """Gerencia a leitura e escrita em páginas diferentes para evitar conflitos."""
    def __init__(self, shared_mem, num_records):
        self.mm = shared_mem
        self.num_records = num_records
        self.page_size = num_records * RECORD_SIZE
        self.write_page = 0 

    def get_offset(self, index, mode="write"):
        """Calcula a posição exata (offset) na memória."""
       
        page = self.write_page if mode == "write" else (1 - self.write_page)
        return (page * self.page_size) + (index * RECORD_SIZE)

    def swap(self):
        """Alterna a página de trabalho (Página 0 <-> Página 1)."""
        self.write_page = 1 - self.write_page
