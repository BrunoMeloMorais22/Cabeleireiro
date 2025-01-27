
document.getElementById('myPerfil').addEventListener('submit', function(event){
    event.preventDefault();
    let nome = document.getElementById('nome').value
    let email = document.getElementById('email').value
    let feedbackperfil = document.getElementById('feedbackperil')

    if(nome === "" || email === ""){
        feedbackperfil.textContent = "Preencha os campos"
        feedbackperfil.style.color = "red"
    }

    else{
        feedbackperfil.textContent = "Perfil criado"
        feedbackperfil.style.color = "green"

        setTimeout(() => {
            feedbackperfil.textContent = "Voltando ao menu principal..."
            window.location.href = "index02.html"
        }, 2000);
    }

})