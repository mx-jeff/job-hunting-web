import { btn, stopBtn, info, spinner, BASE_URL } from './tags.js'


export function init_socket(){
    console.log(BASE_URL)
    return io(`${BASE_URL}`, { transports: ['websocket'], upgrade: false })
}


export function listener_socket(){
    const socket = init_socket()
    
    stopBtn.disabled = true
    info.style.display = "None"

    socket.on('connect', function () {
        socket.emit('init', "conected to server!");
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
    
        if((message == "[Infojobs] Saindo... volte sempre :)") || (message == "[Vagas.com] Saindo... volte sempre :)")){
            console.log('Reativando...')
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