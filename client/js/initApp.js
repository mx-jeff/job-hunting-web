import { spinner, btn, BASE_URL } from "./tags.js"


export async function initApp(){
    spinner.innerHTML = `
        <div class="spinner-border text-primary" role="status">
            <span class="sr-only">Loading...</span>
        </div> Aguarde...
    `
    btn.disabled = true

    const response = await fetch(BASE_URL)
    if(response.status != 200) return 

    spinner.innerHTML = ""
    btn.disabled = false
}