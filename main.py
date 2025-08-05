import webview
from logic.pdf_splitter import split_pdf

class Api:
    def dividir_pdf(self, caminho_pdf, pasta_saida):
        try:
            split_pdf(caminho_pdf, pasta_saida)
            return {"status": "sucesso", "mensagem": "PDF dividido com sucesso!"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}

    def selecionar_pasta(self):
        caminho = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG)
        return caminho[0] if caminho else ""
    
    def selecionar_pdf(self):
        caminho = webview.windows[0].create_file_dialog(webview.OPEN_DIALOG, file_types=["PDF Files (*.pdf)"])
        
        if not caminho:
            return {"status": "cancelado", "mensagem": "Seleção cancelada."}

        if not caminho[0].lower().endswith(".pdf"):
            return {"status": "erro", "mensagem": "Selecione um arquivo PDF válido (.pdf)"}

        return {"status": "ok", "caminho": caminho[0]}

if __name__ == '__main__':
    api = Api()
    webview.create_window("Dividir PDF", "web/index.html", js_api=api, width=900, height=600)
    webview.start()