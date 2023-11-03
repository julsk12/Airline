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
    const Fsalida = document.getElementById("fechaS").value;
    const Fregreso = document.getElementById("fechaR").value;

    window.alert("su fecha de salida es :"+Fsalida+"su fecha de Retorno es :"+Fregreso);
}