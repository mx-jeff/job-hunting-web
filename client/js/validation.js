import { credentails, spinner } from './tags.js'


export function validate(){
    const [email_infojobs, password_infojobs, email_vagas, password_vagas] = credentails
    
    const infojobs_empty= email_infojobs.length == 0 && password_infojobs.length == 0
    const vagas_empty = email_vagas.length == 0 && password_vagas.length == 0
    
    const infojobs_not_empty = email_infojobs.length > 0 && password_infojobs.length > 0
    const vagas_not_empty = email_vagas.length > 0 && password_vagas.length > 0
    
    if(infojobs_empty && vagas_not_empty){
        spinner.textContent = "Insira login e a senha do infojobs antes de continuar!"
        return
    
    } else if(vagas_empty && infojobs_not_empty){
        spinner.textContent = "Insira login e a senha do infojobs antes de continuar!"
        return
    
    } else if(vagas_empty && infojobs_empty){
        spinner.textContent = "Insira login e senha do site de emprego antes de continuar!"
        return
    }
    
    return true
}