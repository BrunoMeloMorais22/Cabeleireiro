
document.getElementById('formContato').addEventListener('submit', function(event){
    event.preventDefault()

    let nome = document.getElementById('nome').value
    let email = document.getElementById('email').value
    let telefone = document.getElementById('telefone').value

    if(nome === "" || email === ""){
        let p = document.createElement('p')
        p.textContent = "Por favor, preencha todos os campos"
        p.style.color = "red"
        p.style.fontSize = "20px"
        p.style.fontWeight = "900"
        p.style.marginLeft = "20px"

        document.getElementById('info').appendChild(p)

        setTimeout(() => {
            p.remove()
        }, 2000);
    }
    else{
        let p = document.createElement('p')
        p.textContent = "Mensagem enviada com sucesso"
        p.style.color = "green"
        p.style.fontSize = "20px"
        p.style.fontWeight = "900"

        document.getElementById('info').appendChild(p)

        setTimeout(() => {
            p.remove()
            document.getElementById('formContato').reset()
        }, 2000);
    }

})
