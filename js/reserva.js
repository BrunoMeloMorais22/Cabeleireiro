function clicar(event){
    const horario = document.querySelectorAll('#horario span')
    horario.forEach((horario) =>{
        horario.classList.remove('selecionado')
    })

    event.target.classList.add('selecionado')
}

document.querySelectorAll('#horario span').forEach((span) => {
    span.addEventListener('click', clicar);
});


document.getElementById('button-reserva').addEventListener('click', function(event){
    event.preventDefault()

    let nome = document.getElementById('nome').value
    let email = document.getElementById('email').value
    let feedback = document.getElementById('feedback')

    if(nome === "" || email === ""){
        feedback.textContent = "Por favor, preencha com os seus dados"
        feedback.style.color = "red"
    }

    else{
        feedback.textContent = "Reserva feita com sucesso"
        feedback.style.color = "green"

        let p = document.createElement('p')
        p.textContent = "Você será redirecionado para a página inicial em 3 segundos"
        feedback.appendChild(p)


        setTimeout(() => {
            window.location.href = 'index.html'
        }, 3000);
    }

})


