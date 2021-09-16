const socket = io("http://localhost:5000");
const empresa = document.querySelector('#empresa')
const vaga = document.querySelector('#vaga')
const btn = document.querySelector('#send')
const info = document.querySelector('#log')
const stopBtn = document.querySelector('#stop')
const credentails = document.querySelectorAll('#modelId input[type=text], input[type=password]')
const saveCredentials = document.querySelector('#save-credentials')
let loadSpin


info.style.display = "none"
socket.on('connect', function () {
    socket.emit('init', "connect");
});

// Mostrar progresso na tela
info.innerHTML = ``
socket.on('message', message => {
    console.log(message)
    // if(message){
    //     loadSpin.innerHTML = ''
    // }
    info.innerHTML += `${message} \n`

    // info.style.height = 'auto';
    // info.style.height = (info.scrollHeight + 10) + 'px';
    info.scrollTo(0, info.scrollHeight);
})

// habilitar botão ao sinal de erro
socket.on('error', err => {
    btn.disabled = false
    info.style.display = "none"
})

// Enviar ao backend
btn.addEventListener('click',() => {
    const [email_infojobs, password_infojobs, email_vagas, password_vagas] = credentails

    const JSONcredentails = localStorage.getItem('credentails')
    const storageCredentails = JSON.parse(JSONcredentails)

    btn.disabled = true
    
    // info.innerHTML = `<div id="load" class="d-flex align-items-center">
    // <strong>Carregando...</strong>
    // <div class="spinner-border ml-auto text-primary" role="status" aria-hidden="true"></div>
    // </div></br>`

    // socket.emit("job", "python", "mx.jeferson.10@hotmail.com", "yeLVYQ7rr7vW@YB")
    info.style.display = 'block'

    socket.emit(
        "job",
        empresa.value, 
        vaga.value, 
        storageCredentails['Email infojobs'] ?? email_infojobs.value, 
        storageCredentails['Senha infojobs'] ?? password_infojobs.value, 
        storageCredentails['Email vagas.com'] ?? email_vagas.value, 
        storageCredentails['Senha vagas.com'] ?? password_vagas.value
    )
    loadSpin = document.querySelector('#load')
})

// Salvar as crendenciais no local storage
saveCredentials.addEventListener('click', () => {
    const [email_infojobs, password_infojobs, email_vagas, password_vagas] = credentails

    const saveData = {
        'Email infojobs': email_infojobs.value,
        'Senha infojobs': password_infojobs.value,
        'Email vagas.com': email_vagas.value,
        'Senha vagas.com': password_vagas.value
    }

    localStorage.setItem('credentails', JSON.stringify(saveData))
})

// se tiver dados na local storage, popular-los com a local storage
if(localStorage.getItem('credentails') !== null) {
    const JSONcredentails = localStorage.getItem('credentails')
    const storage = JSON.parse(JSONcredentails)

    const storageCredentiails = Object.values(storage)

    credentails.forEach((credential, index) => {
        // console.log('html: ', credential)
        // console.log("value: ", storageCredentiails[index])
        credential.value = storageCredentiails[index]
    })
}
