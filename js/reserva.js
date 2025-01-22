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

