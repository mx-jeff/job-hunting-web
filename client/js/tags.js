export const empresa = document.querySelector('#empresa')
export const spinner = document.querySelector('.snipper')
export const vaga = document.querySelector('#vaga')
export const btn = document.querySelector('#send')
export const info = document.querySelector('#log')
export const stopBtn = document.querySelector('#stop')
export const credentails = document.querySelectorAll('#modelId input[type=text], input[type=password]')
export const saveCredentials = document.querySelector('#save-credentials')
export const form = document.querySelector('form#data')

const DEV = false
export const BASE_URL = (DEV) ? "http://localhost:5000" : "https://job-hunting-socket.herokuapp.com"