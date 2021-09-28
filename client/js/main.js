import { listener_socket } from './socket.js'
import { setEvent } from './event.js'
import { setLocalStorage } from './localStorage.js'
import { initApp } from "./initApp"


function main() {
    // init app
    initApp()

    // listener_socket.js
    listener_socket()

    // setEvent.js
    setEvent()

    // setLocalStorage.js
    setLocalStorage()
}

main()
