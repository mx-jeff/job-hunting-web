import { btn, stopBtn, info, spinner } from './tags.js'
import { initApp } from "./initApp.js"


export async function init_socket(){
    const BASE_URL = await initApp()
    return io(`${BASE_URL}`, { transports: ['websocket'], upgrade: false })
}


export async function listener_socket(){
    const socket = await init_socket()
    
    stopBtn.disabled = true
    info.style.display = "None"

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
            spinner.innerHTML = ""
            stopBtn.disabled = false
            btn.disabled = true
            info.style.display = "Block"
        }
    
        if(message == "[Infojobs] Saindo... volte sempre :)" || message == "[Vagas.com] Saindo... volte sempre :)"){
            btn.disabled = false
            stopBtn.disabled = true
        }
    })
    
    socket.off('message', message => {
        info.innerHTML = "Conexão Perdida!"
    })
    
    // habilitar botão ao sinal de erro
    socket.on('error', err => {
        btn.disabled = false
    })
    
    socket.on('disconnect', () => {
        socket.removeAllListeners()
    })
}