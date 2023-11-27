function registrar() {
    var newnombre = document.getElementById('nombre').value;
    var newidentificacion = document.getElementById('identificacion').value;
    var newemail = document.getElementById('email').value;
    var newdireccion = document.getElementById('direccion').value;
    var newtelefono = document.getElementById('telefono').value;
    console.log(newnombre, newidentificacion, newemail, newdireccion, newtelefono);

    if(newnombre.trim() === "" || newidentificacion.trim() === "" || newemail.trim() === "" || newdireccion.trim() === "" || newtelefono.trim() === ""){
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

    alert('vamos a registrar');

    axios.post('/api/registrarUS', {
        nombre: newnombre,
        correo: newemail,
        password: newidentificacion,
        celular: newtelefono,
        direccion: newdireccion,
    }).then((res) => {
        console.log(res.data);
        alert('Registro Exitoso');
    }).catch((err) => {
        console.log(err);
    })

    alert('ya ?');
}

function validarCorreo(correo) {
    const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (regexCorreo.test(correo)) {
        return true;
    } else {
        return false;
    }
}