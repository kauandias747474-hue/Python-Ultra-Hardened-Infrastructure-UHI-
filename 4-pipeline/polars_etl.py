import polars as pl 
import logging 
import os 
import sys
from typing import List, Optional


logger = logging.getLogger("Stream_Processor.Polars")

class PolarsProcessor: 
    def __init__(self, batch_size: int = 10000):
        """
        Inicia o motor Polars com um tamanho de lote definido.
        O(1): A memória usada será proporcional ao batch_size.
        """
        self.batch_size = batch_size
        self.buffer = []
        # Schema explícito para performance máxima em Rust
        self.schema = {
            "id": pl.Int64, 
            "valor": pl.Float64, 
            "tipo": pl.String 
        }

    def push(self, validated_data: dict) -> Optional[pl.DataFrame]:
        """Adiciona ao buffer e retorna DataFrame se atingir o batch_size."""
        self.buffer.append(validated_data)
        
        if len(self.buffer) >= self.batch_size:
            return self.execute_batch()
        return None

    def execute_batch(self) -> Optional[pl.DataFrame]:
        """O coração do motor: Processamento Vetorizado em Rust."""
        if not self.buffer:
            return None

        try:
            # 1. Cria o DataFrame e limpa a RAM
            df = pl.DataFrame(self.buffer, schema=self.schema)
            self.buffer.clear()

            # 2. Transformação High-Speed (Lazy Mode)
            result = (
                df.lazy()
                .filter(pl.col("valor") > 0)
                .group_by("tipo")
                .agg([
                    pl.col("valor").sum().alias("total_valor"),
                    pl.col("id").count().alias("contagem")
                ])
                .collect()
            )
            return result

        except Exception as e:
            logger.error(f"Erro no processamento Polars: {e}")
            self.buffer.clear() 
            return None

    def finalize(self) -> Optional[pl.DataFrame]:
        """Processa os registros restantes no fim do stream."""
        return self.execute_batch()

if __name__ == "__main__":
    
    print("\n[TESTE LOCAL] Rodando motor Polars...")

    engine = PolarsProcessor(batch_size=3)
    
    test_data = [
        {"id": 1, "valor": 150.0, "tipo": "entrada"},
        {"id": 2, "valor": 50.0,  "tipo": "saida"},
        {"id": 3, "valor": 300.0, "tipo": "entrada"},
    ]
    
    for d in test_data:
        res = engine.push(d)
        if res is not None:
            print(">>> Lote Processado:")
            print(res)
