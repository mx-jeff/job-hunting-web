import { listener_socket } from './socket.js'
import { setEvent } from './event.js'
import { setLocalStorage } from './localStorage.js'

function main() {
    // listener_socket.js
    listener_socket()

    // setEvent.js
    setEvent()

    // setLocalStorage.js
    setLocalStorage()
}

main()
