
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
        feedbackperfil.style.color = "green"
        feedbackperfil.textContent = "Perfil criado. Voltando ao menu principal..."
        feedbackperfil.style.fontWeight = "800"

        setTimeout(() => {
            window.location.href = "/index02?nome=" + encodeURIComponent(nome) + "&email=" + encodeURIComponent(email);
        }, 2000);
    }

})