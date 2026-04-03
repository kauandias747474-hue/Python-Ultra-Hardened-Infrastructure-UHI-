#  8-Storage

Este projeto documenta a implementação de um motor de armazenamento de alto desempenho que utiliza mapeamento de memória virtual e técnicas de persistência atômica para garantir a integridade dos dados.

---

##  Arquitetura do Sistema / System Architecture

O sistema é estruturado em três camadas distintas de responsabilidade, isolando a lógica de negócio da infraestrutura de hardware.

1.  **`main.py` (Orchestrator):**
    * **[PT-BR]** Gerencia o fluxo da aplicação e a **Criptografia Híbrida**. Ele processa os dados antes de enviá-los para a camada de persistência, garantindo que o armazenamento receba apenas informações cifradas e estruturadas.
    * **[EN]** Manages the application flow and **Hybrid Encryption**. It processes data before sending it to the persistence layer, ensuring that the storage receives only encrypted and structured information.

2.  **`mmap_db.py` (Memory Engine):**
    * **[PT-BR]** Implementa **Memory-Mapped I/O**. Esta camada trata o arquivo em disco como uma extensão da memória RAM, permitindo leitura e escrita diretas através de endereços de memória, eliminando a sobrecarga de chamadas de sistema tradicionais.
    * **[EN]** Implements **Memory-Mapped I/O**. This layer treats the disk file as an extension of RAM, allowing direct read and write through memory addresses, eliminating the overhead of traditional system calls.

3.  **`atomic_writer.py` (Persistence Layer):**
    * **[PT-BR]** Responsável pela **Consistência de Escrita**. Utiliza a técnica de *Shadow Paging* para garantir que o arquivo de banco de dados nunca entre em estado corrompido em caso de interrupções abruptas.
    * **[EN]** Responsible for **Write Consistency**. It uses the *Shadow Paging* technique to ensure the database file never enters a corrupted state in case of abrupt interruptions.

---

##  Pilares Técnicos / Technical Pillars

### 1. Virtual Memory Mapping (mmap)

* **[PT-BR] Acesso O(1):** A localização de qualquer registro é feita via cálculo de *offset* ($ID \times Tamanho$). O `mmap` permite que o sistema operacional gerencie o cache de páginas de forma eficiente, oferecendo performance de RAM para dados em disco.
* **[EN] O(1) Access:** Locating any record is done via offset calculation ($ID \times Size$). `mmap` allows the operating system to manage page caching efficiently, offering RAM performance for data on disk.

### 2. Shadow Paging & Atomicity

* **[PT-BR] Persistência Atômica:** O processo de escrita segue três etapas: 1) Escrita em arquivo temporário; 2) Flush de hardware (`fsync`); 3) Substituição atômica do arquivo original (`os.replace`). Isso garante que o arquivo original só seja alterado após a gravação completa e segura do novo estado.
* **[EN] Atomic Persistence:** The writing process follows three steps: 1) Writing to a temporary file; 2) Hardware flush (`fsync`); 3) Atomic replacement of the original file (`os.replace`). This ensures the original file is only changed after the complete and secure recording of the new state.

### 3. Criptografia Híbrida / Hybrid Encryption

* **[PT-BR] Segurança em Repouso:** O sistema utiliza **RSA-2048** para a gestão de chaves e **AES-256** para a cifragem dos dados. A integridade é verificada através de **SHA-256 Checksums**, detectando qualquer alteração não autorizada nos bytes do arquivo.
* **[EN] Security at Rest:** The system uses **RSA-2048** for key management and **AES-256** for data encryption. Integrity is verified through **SHA-256 Checksums**, detecting any unauthorized changes to the file bytes.

---

##  Estudo de Caso: Falha de Energia / Case Study: Power Outage

**[PT-BR] Contexto Técnico:** Durante a fase de desenvolvimento, uma falha de energia real permitiu validar a arquitetura. 
* **Observação:** Arquivos de sistema que não utilizavam escrita atômica foram corrompidos no momento da queda (ex: `.git/config`). 
* **Resultado:** O arquivo `storage.db` permaneceu íntegro. Como a operação de substituição (`os.replace`) é atômica no nível do kernel, o banco de dados manteve o último estado estável, demonstrando a eficácia da proteção contra corrupção por desligamento inesperado (*Crash Consistency*).

**[EN] Technical Context:** During the development phase, a real power failure allowed the architecture to be validated.
* **Observation:** System files that did not use atomic writing were corrupted at the time of the crash (e.g., `.git/config`).
* **Result:** The `storage.db` file remained intact. Since the replacement operation (`os.replace`) is atomic at the kernel level, the database maintained the last stable state, demonstrating the effectiveness of protection against corruption by unexpected shutdown (*Crash Consistency*).

---

##  Lições de Engenharia / Engineering Lessons

| Problema (Issue) | Causa (Cause) | Solução Técnica (Technical Solution) |
| :--- | :--- | :--- |
| **Bus Error** | Mapear arquivo vazio. | **Pre-allocation:** Garantir que o arquivo tenha o tamanho correto antes do mapeamento. |
| **Empty Read** | Ponteiro no final do arquivo. | **Pointer Management:** Uso de `seek(0)` para garantir leitura completa do buffer. |
| **Data Corruption** | Interrupção de escrita. | **Atomic Swapping:** Uso de arquivos temporários e substituição atômica. |

---

##  Glossário de Revisão / Review Glossary

* **`fsync()`**: 
    * [PT] Sincroniza o estado do arquivo na memória com o dispositivo de armazenamento físico.
    * [EN] Synchronizes the file state in memory with the physical storage device.
* **`Crash Consistency`**: 
    * [PT] Garantia de que o sistema de arquivos ou banco de dados permanece consistente após uma falha.
    * [EN] Guarantee that the file system or database remains consistent after a failure.
* **`Memory-Mapped I/O`**: 
    * [PT] Técnica que mapeia arquivos ou recursos em endereços de memória.
    * [EN] Technique that maps files or resources into memory addresses.



---
