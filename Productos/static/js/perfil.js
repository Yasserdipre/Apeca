let changecargo = () => {
    let  data = document.getElementById("change").classList.add('d-none');
    let changedata = document.getElementById("send")
    changedata.classList.remove('d-none');
    changedata.classList.add('d-block')

}

let deletecargo = () => {
    let  data = document.getElementById("send").classList.add('d-none');
    let changedata = document.getElementById("change")
    changedata.classList.remove('d-none');
    changedata.classList.add('d-block')
}