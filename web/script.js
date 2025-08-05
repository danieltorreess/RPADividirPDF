async function salvar() {
  const caminhoPDF = document.getElementsByName("input-pdf")[0].value;
  const caminhoSalvar = document.getElementById("input-save").value;
  const status = document.getElementById("status");

  if (!caminhoPDF || !caminhoSalvar) {
    alert("Preencha todos os campos antes de salvar.");
    return;
  }

  // Mostra o loader antes de iniciar o processo
  status.innerHTML = `<div class="loader"></div>`;
  status.style.color = "white";

  // Aguarda o backend dividir o PDF
  const res = await window.pywebview.api.dividir_pdf(caminhoPDF, caminhoSalvar);

  // Exibe mensagem de sucesso ou erro
  status.innerText = res.mensagem;
  status.style.color = res.status === "sucesso" ? "#00ffcc" : "red";

  if (res.status === "sucesso") {
    // Limpa campos
    document.getElementsByName("input-pdf")[0].value = "";
    document.getElementById("input-save").value = "";

    // Limpa status após 3s
    setTimeout(() => {
      status.innerText = "";
    }, 3000);
  }
}

async function escolherPasta() {
  const caminho = await window.pywebview.api.selecionar_pasta();
  if (caminho) {
    document.getElementById("input-save").value = caminho;
  }
}

async function escolherPDF() {
  const res = await window.pywebview.api.selecionar_pdf();

  if (res.status === "ok") {
    document.getElementsByName("input-pdf")[0].value = res.caminho;
  } else if (res.status === "erro") {
    alert(res.mensagem);
  }
}