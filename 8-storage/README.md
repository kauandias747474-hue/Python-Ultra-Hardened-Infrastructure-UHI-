#  8-Storage: Atomic Persistence & Mmap

Este módulo foca na criação de um motor de armazenamento de baixa latência e alta confiabilidade, combinando performance de memória RAM com segurança de escrita atômica.

---

##  Lógica do Código / Code Logic

### 1. Zero-Copy Persistence (Memory Mapping)
* **[PT-BR]** O arquivo `mmap_db.py` utiliza **Virtual Memory Mapping**. Em vez de realizar operações tradicionais de leitura e escrita em disco (I/O), o arquivo é mapeado diretamente no espaço de endereçamento da memória RAM. Isso permite acesso **O(1)** (tempo constante) aos registros, tratando o arquivo como um grande array de bytes.
* **[EN]** The `mmap_db.py` file uses **Virtual Memory Mapping**. Instead of traditional disk I/O operations, the file is mapped directly into the RAM address space. This allows **O(1)** (constant time) access to records, treating the file as a large byte array.



### 2. Atomic Write & Shadow Paging
* **[PT-BR]** O `atomic_writer.py` implementa a técnica de **Shadow Paging**. Para evitar a corrupção de dados, as alterações são gravadas primeiro em um arquivo temporário (`.tmp`). Somente após o sucesso da gravação física (`fsync`), o arquivo original é substituído via `os.replace`.
* **[EN]** `atomic_writer.py` implements the **Shadow Paging** technique. To avoid data corruption, changes are first written to a temporary file (`.tmp`). Only after successful physical writing (`fsync`), the original file is replaced via `os.replace`.



---

##  Conceitos & Erros Aprendidos / Concepts & Lessons Learned

### Desafios Técnicos / Technical Challenges
* **Pre-allocation:** Aprendi que o `mmap` exige que o arquivo no disco já tenha o tamanho pretendido (pre-padding) para evitar erros de barramento (Bus Errors).
* **State Management:** A importância de resetar ponteiros de arquivo (`seek(0)`) e garantir que o buffer de memória esteja sincronizado antes da persistência.
* **Crash Consistency:** A capacidade de um software voltar ao estado estável após um desligamento repentino.

###  O Teste de Estresse Real (Falta de Energia) / The Real-World Stress Test
* **[PT-BR] Curiosidade:** Durante o desenvolvimento deste módulo, ocorreu uma **queda de energia real** em minha residência. O arquivo de configuração do Git (`.git/config`) foi corrompido, resultando no erro `fatal: bad config line 1`. Isso provou, na prática, a fragilidade de sistemas que não usam escrita atômica. Enquanto o Git falhou, meu sistema foi projetado para sobreviver exatamente a esse cenário, mantendo a integridade do banco de dados.
* **[EN] Trivia:** During the development of this module, a **real power outage** occurred. The Git config file (`.git/config`) was corrupted, leading to the error `fatal: bad config line 1`. This proved in practice the fragility of systems that do not use atomic writing. While Git failed, my system was designed to survive exactly this scenario, maintaining database integrity.

---

##  Arquitetura do Sistema / System Architecture

O sistema é dividido em camadas de responsabilidade (Clean Architecture):

1. **`main.py` (Orquestrador):** Gerencia a interface, criptografia RSA/AES e lógica de IDs.
2. **`mmap_db.py` (Infraestrutura):** Fornece o motor de memória de alta performance e suporte a **Dynamic Resizing** (o banco cresce conforme a necessidade).
3. **`atomic_writer.py` (Segurança):** Atua como a camada de persistência física, garantindo que o "commit" dos dados seja seguro contra falhas de hardware.



---

##  Glossário Técnico / Technical Glossary

* **ACID (Atomicity):** [PT] Garantia de "tudo ou nada". [EN] "All or nothing" guarantee.
* **O(1) Access:** [PT] Velocidade de acesso independente do tamanho do arquivo. [EN] Access speed independent of file size.
* **fsync:** [PT] Comando que obriga o hardware a gravar os dados do cache no disco físico. [EN] Command that forces the hardware to write cache data to the physical disk.
* **Hash Integrity:** [PT] Uso de SHA-256 para verificar se o dado foi alterado indevidamente. [EN] Using SHA-256 to verify if data has been improperly altered.



---
