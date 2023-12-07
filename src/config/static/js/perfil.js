const IDU = localStorage.getItem('IDU');

function cargarus() {
    const RENnombre = document.getElementById('R1');
    const RENemail = document.getElementById('R2');
    const RENtelefono = document.getElementById('R3');
    const RENdireccion = document.getElementById('R4');
    const RENreserva = document.getElementById('R5');

    axios.get('/api/perfilUS', {
        responseType: 'json'}).then(function(response) {
            let datos = response.data
            for (let i = 1; i <= Object.keys(datos).length; i++) {
                if (datos[i].correou == IDU) {
                    RENnombre.innerHTML = `<p id="R1"><strong>Nombre: </strong>${datos[i].nombreu}</p>`;
                    RENemail.innerHTML = `<p id="R2"><strong>Correo Electrónico: </strong>${datos[i].correou}</p>`;
                    RENtelefono.innerHTML = `<p id="R3"><strong>Número de Teléfono: </strong>${datos[i].celularu}</p>`;
                    RENdireccion.innerHTML = `<p id="R4"><strong>Dirección: </strong>${datos[i].direccionu}</p>`;
                    axios.get('/api/reservaUS', {
                        responseType: 'json'}).then(function(response) {
                            let datos = response.data
                            for (let i = 1; i <= Object.keys(datos).length; i++) {
                                RENreserva.innerHTML = `<p id="R5"><strong>numero de asientos: </strong>${datos[i].asientosReservadosu}</p>
                                <p ><strong>Asientos reservados: </strong>${datos[i].nasientou}</p>
                                <p ><strong>Tipo de boleto: </strong>${datos[i].tipoBoletou}</p>
                                <p ><strong>ID Vuelo: </strong>${datos[i].id_vuelou}</p>`;
                                return;   
                            }
                            window.alert("Por favor iniciar sesion");
                        }).catch(function(error) {
                            console.log(error);
                        });
                }
            }
            window.alert("Por favor iniciar sesion");
        }).catch(function(error) {
            console.log(error);
        });
}

function cerrarUS() {
    window.alert("Sesion Finalizada");
    localStorage.removeItem('IDU');
    window.location.replace('/');
}

document.addEventListener('DOMContentLoaded', function() {
    cargarus();
});