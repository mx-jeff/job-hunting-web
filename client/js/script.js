const socket = io("http://localhost:5000");
const buttonIniciar = document.querySelector('#iniciar')
const info = document.querySelector('#info')

buttonIniciar.addEventListener('click', () => {
    socket.emit("job", "python", "mx.jeferson.10@hotmail.com", "yeLVYQ7rr7vW@YB")
})

socket.on('connect', function () {
    socket.emit('init', "connect");
});

socket.on('message', message => {
    console.log(message)
    info.innerHTML += message + "\n"
})