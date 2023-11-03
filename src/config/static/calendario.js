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