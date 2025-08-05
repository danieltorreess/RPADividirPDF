from pathlib import Path
from pypdf import PdfReader, PdfWriter

def split_pdf(caminho_pdf: str, pasta_saida: str):
    caminho = Path(caminho_pdf)
    saida = Path(pasta_saida)
    reader = PdfReader(str(caminho))

    for i, pagina in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(pagina)

        nome_base = caminho.stem
        novo_nome = f"{nome_base}_{i + 1}.pdf"
        caminho_saida = saida / novo_nome

        with open(caminho_saida, 'wb') as f:
            writer.write(f)
