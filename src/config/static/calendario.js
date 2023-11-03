// Configura el calendario
$(document).ready(function() {
    $("#fechaS").datepicker({
        minDate: 0,
        dateFormat: 'yy-mm-dd'
    });

    $("#fechaR").datepicker({
        minDate: 0,
        dateFormat: 'yy-mm-dd'
    });

    // Cuando se hace clic en el espacio, abre el calendario
    $("#mostrarCalendario").on("click", function() {
        $("#fechaS").datepicker("show");
        $("#fechaR").datepicker("show");
    });
});

function buscar_vuelos(){
    const origen = document.getElementById("OrigenL").value;
    const destino = document.getElementById("DestinoL").value;
    const Fsalida = document.getElementById("fechaS").value;
    const Fregreso = document.getElementById("fechaR").value;

    axios.get('/consulvuelos', {
            responseType: 'json'
        })
        .then(function(response) {
            for (let i = 1; i <= Object.keys(datos).length; i++) {
                if (datos[i].origen == origen && datos[i].destino == destino) {
                    window.alert("su fecha de salida es :"+Fsalida+" su fecha de Retorno es :"+Fregreso);
                    window.alert("salio de :"+origen+" llego a :"+destino);
                }
            }
        })
        .catch(function(error) {
            console.log(error);
        });
}