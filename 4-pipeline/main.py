import logging
import sys
import os
import polars as pl
from pydantic import BaseModel, Field, ValidationError
from typing import Optional, Generator


def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    logger = logging.getLogger("Stream_Processor")
    logger.setLevel(logging.DEBUG)
    
    fmt = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s')

    file_h = logging.FileHandler('logs/audit.log', encoding='utf-8')
    file_h.setFormatter(fmt)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

    logger.addHandler(file_h)
    logger.addHandler(console)
    return logger


class Transaction(BaseModel):
    id: int
    valor: float = Field(gt=0)
    tipo: str


class PolarsProcessor:
    def __init__(self, batch_size: int = 5000):
        self.batch_size = batch_size
        self.buffer = []
        self.schema = {"id": pl.Int64, "valor": pl.Float64, "tipo": pl.Utf8}

    def push(self, data: dict) -> Optional[pl.DataFrame]:
        self.buffer.append(data)
        if len(self.buffer) >= self.batch_size:
            return self.execute_batch()
        return None

    def execute_batch(self) -> Optional[pl.DataFrame]:
        if not self.buffer:
            return None
        try:
    
            df = pl.DataFrame(self.buffer, schema=self.schema)
            self.buffer.clear() 

            return (
                df.lazy()
                .group_by("tipo")
                .agg([
                    pl.col("valor").sum().alias("total"),
                    pl.col("id").count().alias("contagem")
                ])
                .collect()
            )
        except Exception as e:
            print(f"Erro no Polars: {e}")
            return None


def stream_reader(n: int):
    for i in range(n):
        yield {
            "id": i, 
            "valor": 150.0 * (i + 1), 
            "tipo": "entrada" if i % 2 == 0 else "saida"
        }


def main():
    # Iniciamos os componentes
    log = setup_logging()
    log.info("Iniciando motor de processamento...")
    
    motor = PolarsProcessor(batch_size=5000)
    
    try:
        # Loop de processamento de 15 mil registros
        for i, dado_bruto in enumerate(stream_reader(15000)):
            
            try:
                # Valida o dado (Pydantic)
                valido = Transaction(**dado_bruto)
                
                # Manda para o "balde" (Polars)
                resultado = motor.push(valido.model_dump())

                # Se o balde encheu, o Polars cospe o resultado
                if resultado is not None:
                    log.info(f"Lote processado no registro {i}")
                    print("\n--- [DADOS PROCESSADOS PELO POLARS] ---")
                    print(resultado)
                    print("---------------------------------------\n")

            except ValidationError:
                log.warning(f"Linha {i} descartada: Dados inválidos.")
                continue

        # Finalização (processa o que sobrou no balde)
        sobra = motor.execute_batch()
        if sobra is not None:
            log.info("Processando registros finais...")
            print("\n=== RESUMO FINAL CONSOLIDADO ===")
            print(sobra)

    except KeyboardInterrupt:
        log.critical("Processo interrompido pelo usuário.")
    finally:
        log.info("Pipeline encerrado.")

if __name__ == "__main__":
    main()
