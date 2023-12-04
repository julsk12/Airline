function registrar() {
    var newnombre = document.getElementById('nombre').value;
    var newidentificacion = document.getElementById('identificacion').value;
    var newemail = document.getElementById('email').value;
    var newcontraseña = document.getElementById('contraseña').value;
    var newdireccion = document.getElementById('direccion').value;
    var newtelefono = document.getElementById('telefono').value;
    console.log(newnombre, newidentificacion, newemail, newdireccion, newtelefono);

    if(newnombre.trim() === "" || newidentificacion.trim() === "" || newemail.trim() === "" || newcontraseña.trim() === "" || newdireccion.trim() === "" || newtelefono.trim() === ""){
        alert('No deben quedar campos vacios');
        return;
    }

    if (!/^\d+$/.test(newtelefono) || !/^\d+$/.test(newidentificacion)) {
        alert('Solo numeros en estos campos');
        return;
    }

    if (!validarCorreo(newemail)) {
        alert('Email invalido');
        return;
    }

    axios.post('/api/registrar', {
        nombre: newnombre,
        correo: newemail,
        cedula: newidentificacion,
        password: newcontraseña,
        celular: newtelefono,
        direccion: newdireccion,
    }, {
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((res) => {
        console.log(res.data);
        alert('Registro Exitoso');
        Limpiar();
    })
    .catch((err) => {
        console.error(err);
    });
}

function iniciarSesion() {
    var user= document.getElementById('usuario').value;
    var contra = document.getElementById('contrasena').value;

    // Verifica las credenciales, implementa lógica de autenticación
    // Mensaje en consola
    if(user.trim() === "" || contra.trim() === ""){
        alert('No deben quedar campos vacios');
        return;
    }

    if (!/^\d+$/.test(contra)) {
        alert('Solo numeros en este campo');
        return;
    }

    if (!validarCorreo(user)) {
        alert('Correo Electrónico invalido');
        return;
    }

    if (user === 'Admino@gmail.com' && contra === '123') {
        alert('¡Bienvenido, ' + usuario + '!');
        return;
    }

    axios.get('/api/ingresar', {
        responseType: 'json'}).then(function(response) {
            let datos = response.data
            let nombre = user;
            let password = contra;
            console.log(nombre, password);
            for (let i = 1; i <= Object.keys(datos).length; i++) {
                if (datos[i].correou == nombre && datos[i].password == password) {
                    window.location.replace('/');
                    return;
                }
            }
            window.alert("Usuario o contraseña incorrectos");
        }).catch(function(error) {
            console.log(error);
        });
}

function validarCorreo(correo) {
    const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (regexCorreo.test(correo)) {
        return true;
    } else {
        return false;
    }
}

function Limpiar() {
    const newnombre = document.getElementById('nombre');
    const newidentificacion = document.getElementById('identificacion');
    const newemail = document.getElementById('email');
    const newcontraseña = document.getElementById('contraseña').value;
    const newdireccion = document.getElementById('direccion');
    const newtelefono = document.getElementById('telefono');

    newnombre.value = "";
    newidentificacion.value = "";
    newemail.value = "";
    newcontraseña.value = "";
    newdireccion.value = "";
    newtelefono.value = "";
}

