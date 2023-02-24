const $login = document.getElementById('login');
const $txtNombre = document.getElementById('txtNombre');
const $txtApellidos = document.getElementById('txtApellidos');
const $contraseña = document.getElementById('contraseña');
const $confirmarcontraseña = document.getElementById('confirmarcontraseña');

(function (){
    $login.addEventListener('submit', function (e) {
        let nombre= String($txtNombre.value).trim();
        let apellidos= String($txtApellidos.value).trim();
        if (nombre.length == 0){
            alert('El Nombre no puede ir vacio')
            e.preventDefault();
        }
        else if (apellidos.length == 0){
            alert('El Apellido no puede ir vacio')
            e.preventDefault();
        }

        else if ($contraseña.value != $confirmarcontraseña.value){
            document.getElementById("error").classList.add("mostrar");
            e.preventDefault();
        }
        
    });
    
   
}
    
    )();