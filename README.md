# 🐍 Extrator Ren’Py

📌 **Objetivo**: Estudar **Python** e **Ren’Py**, criando uma ferramenta para **extrair e decompilar arquivos `.rpyc`** utilizando `unrepyc` e `rpycdec`.  

> ⚠️ Este projeto é **estritamente educacional** e não tem fins comerciais nem de modificação não autorizada de jogos.

---

## 🎯 Objetivos
- Estudar a linguagem **Python** aplicando-a em contextos reais.  
- Aprender como o **Ren’Py** organiza, compila e executa seus scripts.  
- Explorar a engenharia reversa de arquivos `.rpyc` **apenas para fins educacionais**.  

---

## 📖 Aprendizados
- Prática com Python (módulos, organização e virtualenv)  
- Manipulação de arquivos `.rpyc` de Ren’Py  
- Estruturação de projetos reutilizáveis  

---

## 🧰 Tecnologias / Ferramentas
- **[Python 3.10+](https://www.python.org/)**  
- **[unrepyc](https://github.com/CensoredUsername/unrpyc)** – Para descompilar arquivos `.rpyc`  
- **[rpycdec](https://github.com/Shizmob/rpyc)** – Ferramenta alternativa de descompilação  
- `venv` – Ambiente virtual do Python  
- `pip` – Gerenciador de pacotes  

---

## 📂 Estrutura do projeto


├── Output/ # Arquivos de saída extraídos
├── Utils/ # Funções auxiliares (handlers, helpers, etc.)
├── venv/ # Ambiente virtual Python
├── .gitignore # Arquivos ignorados pelo Git
├── extrator.py # Script principal do projeto
├── README.md # Documentação
└── requirements.txt # Dependências do projeto

---


## 🚀 Como usar

1. **Clone o repositório:**

```bash
git clone https://github.com/Theus750/Extractor-Renpy.git
cd seu-repo
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt

---


## 🧪 Exemplos de uso

python extrator.py "C:\Jogo\game\scripts"  "destino\dos\arquivos"      

# Os arquivos processados vão aparecer dentro da pasta:

"destino\dos\arquivos"

##🤝 Contribuições
Sinta-se à vontade para abrir issues e enviar pull requests.
Sugestões de melhorias, correções e novas funcionalidades são sempre bem-vindas.



### 📌 Roadmap

Abaixo estão os planos de evolução deste projeto:

- [ ] ❌ **Adicionar suporte a múltiplas pastas de entrada**  
  Permitir que o usuário informe várias pastas contendo arquivos `.rpyc` de uma vez só.

- [ ] ❌ **Criar interface de linha de comando (CLI)**  
  Usar bibliotecas como `argparse` ou `click` para permitir uso mais flexível via terminal.

- [ ] ❌ **Melhorar logs e mensagens de erro**  
  Implementar logs mais informativos e mensagens de erro mais claras, com tratamento de exceções.

- [ ] ❌ **Escrever testes automatizados**  
  Adicionar testes com `unittest` ou `pytest` para garantir estabilidade e facilitar futuras alterações.


