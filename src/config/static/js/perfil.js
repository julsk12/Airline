const IDU = localStorage.getItem('IDU');

function cargarus() {
    const RENnombre = document.getElementById('R1');
    const RENemail = document.getElementById('R2');
    const RENtelefono = document.getElementById('R3');
    const RENdireccion = document.getElementById('R4');

    axios.get('/api/perfilUS', {
        responseType: 'json'}).then(function(response) {
            let datos = response.data
            for (let i = 1; i <= Object.keys(datos).length; i++) {
                if (datos[i].correou == IDU) {
                    RENnombre.innerHTML = `<p id="R1"><strong>Nombre: </strong>${datos[i].nombreu}</p>`;
                    RENemail.innerHTML = `<p id="R2"><strong>Correo Electrónico: </strong>${datos[i].correou}</p>`;
                    RENtelefono.innerHTML = `<p id="R3"><strong>Número de Teléfono: </strong>${datos[i].celularu}</p>`;
                    RENdireccion.innerHTML = `<p id="R4"><strong>Dirección: </strong>${datos[i].direccionu}</p>`;
                    return;
                }
            }
            window.alert("Por favor iniciar sesion");
        }).catch(function(error) {
            console.log(error);
        });
}

document.addEventListener('DOMContentLoaded', function() {
    cargarus();
});