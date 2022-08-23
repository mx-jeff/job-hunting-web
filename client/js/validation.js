import { credentails, spinner } from './tags.js'


export function validate(empresa, vaga){
    const [email_infojobs, password_infojobs, email_vagas, password_vagas] = credentails
    
    // console.log("Validando!")

    if(vaga.length == 0){
        spinner.innerHTML = "<div style='color: red; font-weight: bold'>Insira a vaga desejada antes de continuar!</div>"
        return
    }

    if(empresa == "infojobs"){
        const infojobs_empty = email_infojobs.value.length == 0 || password_infojobs.value.length == 0
        // const infojobs_not_empty = email_infojobs.value.length > 0 && password_infojobs.value.length > 0
    
        if(infojobs_empty){
            spinner.innerHTML = "<div style='color: red'>Insira login e/ou senha do infojobs antes de continuar!</div>"
            return
        }

        // console.log("ok!")
        return true
    }
    
    else if(empresa == "vagas.com"){    
        const vagas_empty = email_vagas.value.length == 0 || password_vagas.value.length == 0
        // const vagas_not_empty = email_vagas.value.length > 0 && password_vagas.value.length > 0
        
        if(vagas_empty){
            spinner.innerHTML = "<div style='color: red'>Insira login e/ou senha do vagas.com antes de continuar!</div>"
            return
        }

        // console.log("ok!")
        return true
    } 
    
    else {
        spinner.innerHTML = "<div style='color: red'>Insira vaga selecionada, alem das credenciais antes de continuar!</div>"
        return
    }
}