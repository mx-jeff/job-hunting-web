import { saveCredentials, credentails } from './tags.js'


export function setLocalStorage() {
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
}