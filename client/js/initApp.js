import { spinner, btn } from "./tags.js"


export async function initApp(){
    spinner.innerHTML = `
        <div class="spinner-border text-primary" role="status">
            <span class="sr-only">Loading...</span>
        </div> Aguarde...
    `
    btn.disabled = true

    const DEV = false
    const BASE_URL = (DEV) ? "http://localhost:5000" : "https://job-hunting-socket.herokuapp.com"

    const response = await fetch(BASE_URL)
    if(response.status != 200) return 

    spinner.innerHTML = ""
    btn.disabled = false

    return BASE_URL
}