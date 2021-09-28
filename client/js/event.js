import { btn, stopBtn, credentails, spinner, info } from './tags.js'
import { init_socket } from "./socket.js"


export async function setEvent(){
    const socket = await init_socket()

    // Enviar ao backend
    btn.addEventListener('click', e => {
        const [email_infojobs, password_infojobs, email_vagas, password_vagas] = credentails

        info.innerHTML = ""
        spinner.innerHTML = `<div class="spinner-border text-primary" role="status">
            <span class="sr-only">Loading...</span>
        </div> Aguarde...`

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
        e.preventDefault() 
    })

    // Parar processo se existir
    stopBtn.addEventListener('click', click => {
        socket.emit('close')
            
        btn.disabled = false
        stopBtn.disabled = true
        click.preventDefault()
    })
}