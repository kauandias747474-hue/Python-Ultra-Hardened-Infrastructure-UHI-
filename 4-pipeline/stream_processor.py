import logging
import sys
import os 
import polars as pl 
from pydantic import BaseModel, Field, ValidationError 

def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    

    logger = logging.getLogger("Stream_Processor")
    logger.setLevel(logging.DEBUG)
    
    exec_format = logging.Formatter('%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s')

    file_audit = logging.FileHandler('logs/audit.log', encoding='utf-8')
    file_audit.setLevel(logging.INFO)
    file_audit.setFormatter(exec_format)


    file_debug.setLevel(logging.DEBUG)
    file_debug.setFormatter(exec_format)

    console_telemetry = logging.StreamHandler(sys.stdout)
    console_telemetry.setLevel(logging.INFO) 
    console_telemetry.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

    logger.addHandler(file_audit)
    logger.addHandler(file_debug)
    logger.addHandler(console_telemetry)
    return logger


logger = setup_logging()

class Transaction(BaseModel):
    id: int
    valor: float = Field(gt=0)
    tipo: str


class PolarsETL:
    def __init__(self, batch_size=10000):
        self.batch_size = batch_size
        self.buffer = []

        self.schema = {"id": pl.Int64, "valor": pl.Float64, "tipo": pl.String}

    def push(self, data: dict):
        self.buffer.append(data)
        if len(self.buffer) >= self.batch_size:
            return self.flush()
        return None

    def flush(self):
        if not self.buffer:
            return None
        
        df = pl.DataFrame(self.buffer, schema=self.schema)
        self.buffer.clear() 
        
   
        resumo = (
            df.lazy()
            .group_by("tipo")
            .agg(pl.col("valor").sum().alias("total"))
            .collect()
        )
        return resumo

def stream_reader(n):
    for i in range(n):
        yield {"id": i, "valor": 10.5 * (i + 1), "tipo": "venda" if i % 2 == 0 else "compra"}

def main_pipeline():
    logger.info("Sistema Iniciado. Preparando motor Polars...")
    
    batch_size = 5000
    etl_engine = PolarsETL(batch_size=batch_size)
    
    start_line = 0 
    logger.info(f"Retomando do registro: {start_line}")

    try:
        for i, registro_bruto in enumerate(stream_reader(20000)):
            if i < start_line: continue
            
            try:
                transacao = Transaction(**registro_bruto)
                resultado_lote = etl_engine.push(transacao.model_dump())
                
                if resultado_lote is not None:
                    # Usando print para garantir visibilidade imediata no terminal
                    print(f"\n--- LOTE PROCESSADO ({i} registros) ---")
                    print(resultado_lote)
                    logger.info(f"Lote finalizado no registro {i}")

            except ValidationError as e:
                logger.warning(f"Linha {i} descartada: {e}")
                continue

        # Finalização
        resto = etl_engine.flush()
        if resto is not None:
            print("\n=== RESUMO FINAL CONSOLIDADO ===")
            print(resto)
            logger.info("Processamento final concluído.")

    except Exception as e:
        logger.critical(f"FALHA CATÁSTROFICA: {e}", exc_info=True)
    finally:
        logger.info("Pipeline encerrado com segurança.")

if __name__ == "__main__":
    main_pipeline()
