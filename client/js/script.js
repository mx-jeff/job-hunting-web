const empresa = document.querySelector('#empresa')
const vaga = document.querySelector('#vaga')
const btn = document.querySelector('#send')
const info = document.querySelector('#log')
const stopBtn = document.querySelector('#stop')
const credentails = document.querySelectorAll('#modelId input[type=text], input[type=password]')
const saveCredentials = document.querySelector('#save-credentials')
let loadSpin

const snipper = `
    <div id="load" class="d-flex align-items-center">
        <strong>Carregando...</strong>
        <div class="spinner-border ml-auto text-primary" role="status" aria-hidden="true"></div>
    </div>`

const BASE_URL = "http://localhost"
const PORT = 5000

const socket = io(`${BASE_URL}:${PORT}`, { transport: ['websocket'] })

stopBtn.disabled = true
socket.on('connect', function () {
    socket.emit('init', "connect");
});

// Mostrar progresso na tela
info.innerHTML = ``
socket.on('message', message => {
    console.log(message)
    info.innerHTML += `${message} \n`
    info.scrollTo(0, info.scrollHeight);

    if(message.length > 0){
        stopBtn.disabled = false
        btn.disabled = true
    }

    if(message == "[Infojobs] Saindo... volte sempre :)" || message == "[Vagas.com] Saindo... volte sempre :)"){
        btn.disabled = false
        stopBtn.disabled = true
    }
})

// habilitar botão ao sinal de erro
socket.on('error', err => {
    btn.disabled = false
})

// Enviar ao backend
btn.addEventListener('click', e => {
    e.preventDefault() 
    const [email_infojobs, password_infojobs, email_vagas, password_vagas] = credentails

    const JSONcredentails = localStorage.getItem('credentails')
    const storageCredentails = JSON.parse(JSONcredentails)

    console.log('opening connection...')
    socket.emit('open')
    console.log('sending data...')
    socket.emit(
        "job",
        empresa.value, 
        vaga.value, 
        storageCredentails['Email infojobs'] ?? email_infojobs.value, 
        storageCredentails['Senha infojobs'] ?? password_infojobs.value, 
        storageCredentails['Email vagas.com'] ?? email_vagas.value, 
        storageCredentails['Senha vagas.com'] ?? password_vagas.value
    )
})

// Parar processo se existir
stopBtn.addEventListener('click', click => {
    click.preventDefault()
    
    socket.emit('close')
        
    btn.disabled = false
    stopBtn.disabled = true
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
        credential.value = storageCredentiails[index]
    })
}
