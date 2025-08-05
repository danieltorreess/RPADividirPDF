# Criar ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar as dependências básicas
pip install pywebview pypdf
pip install pyinstaller
pip install pillow

# Atualizar o meu requirements.txt
pip freeze > requirements.txt

# Comando da aplicação - Dock duplicado
pyinstaller --windowed --onefile --add-data "web:web" --icon=web/assets/pdf-icon.ico main.py

# Comando da aplicação - Dock único
pyinstaller --windowed --add-data "web:web" --icon=web/assets/pdf-icon.ico main.py

# Deletar pastas dist e build caso tenha saído algo errado
rm -rf build dist __pycache__ main.spec

# Salvar dependências
pip freeze > requirements.txt

# Criar a estrutura inicial do projeto
RPADividirPDF/
├── main.py
├── logic/
│   └── pdf_splitter.py
├── web/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── assets/  # (vamos adicionar os ícones depois)
├── requirements.txt
└── .venv/

# GitHub
git init
git add .
git commit -m "Projeto RPA dividir PDF"
git status
git remote add origin https://github.com/danieltorreess/RPADividirPDF.git
git branch -M main
git push -u origin main