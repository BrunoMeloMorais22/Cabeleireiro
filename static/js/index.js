const toggleButton = document.getElementById("toggleDarkMode");

toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");

    // Salva a preferência do usuário no navegador
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("modoEscuro", "ativado");
    } else {
        localStorage.setItem("modoEscuro", "desativado");
    }
});

// Mantém a escolha do usuário mesmo ao recarregar a página
if (localStorage.getItem("modoEscuro") === "ativado") {
    document.body.classList.add("dark-mode");
}
