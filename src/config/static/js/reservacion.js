const progress = document.getElementById('progress')
const back = document.getElementById('back')
const next = document.getElementById('next')
const wraps = document.querySelectorAll('.text-wrap')
let tarifa = ""
let currentActive = 1

next.addEventListener('click', () => {
    if (currentActive === 1) {
        if (tarifa === "") {
            Swal.fire({
                title: "Oops!",
                text: "Por favor seleciona una tarifa",
                icon: "error"
            });
        }  
    }
    if (currentActive === 2) {
        let pasajeros = document.getElementById("Pasajeros").value;
    for (let index = 1; index < pasajeros; index++) {
        let primer_nombre = document.getElementById(`nombre_pasajero${index}`).value;
        let genero = document.getElementById(`genero_pasajero${index}`).value;
        let primer_apellido = document.getElementById(`apellido_pasajero${index}`).value;
        console.log(primer_apellido, primer_nombre, genero)
        if (primer_nombre === "" || primer_apellido === "" || genero === "") {
            Swal.fire({
                title: "Oops!",
                text: "Por favor llena todos los campos",
                icon: "error"
            });
        }else{
            currentActive++
            if (currentActive > wraps.length) {
                currentActive = wraps.length
            }
            update()
        }
    }
    }
})

function validar_datos() {
    
}

back.addEventListener('click', () => {
    currentActive--
    if (currentActive < 1) {
        currentActive = 1
    }

    update()
})

function update() {
    wraps.forEach((wrap, index) => {
        if (index < currentActive) {
            wrap.classList.add('active')
        } else {
            wrap.classList.remove('active')
        }
    })

    const actives = document.querySelectorAll('.active')
    progress.style.width = (actives.length - 1) / (wraps.length - 1) * 80 + '%'

    if (currentActive === 1) {
        back.disabled = true
    } else if (currentActive === wraps.length) {
        next.disabled = true
    } else {
        back.disabled = false
        next.disabled = false
    }
}



function npasajeros() {
    let pasajeros = document.getElementById("Pasajeros").value;
    morfismo = document.getElementById("seccion2");
    console.log(pasajeros);
    lista = "";
    for (let index = 1; index < pasajeros; index++) {
        lista += `
        <label id="pasajero${index + 1}" style="margin-top: 20px;">Pasajero ${index + 1}</label><br>
        <label style="fw-bold text-danger mb-3" for="genero">Género:</label>
        <select class="input-info" id="genero_pasajero${index}">
            <option value="masculino">Masculino</option>
            <option value="femenino">Femenino</option>
            <option value="otro">Otro</option>
        </select>
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_nombre">Primer nombre:</label>
        <input class="input-info" type="text" id="nombre_pasajero${index}">
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_apellido">Primer apellido:</label>
        <input class="input-info" type="text" id="apellido_pasajero${index}">
        `}
    morfismo.innerHTML = lista;
}

document.getElementById('s').addEventListener('click', function () {
    Swal.fire({
        title: "MUY BIEN!",
        text: "Has seleccionado la tarifa S",
        icon: "success"
    });
    tarifa = "S"
    document.getElementById("seccion-pasajeros").style.display = "grid"
    document.getElementById("seccion1").style.display = "none"
    currentActive++
    if (currentActive > wraps.length) {
        currentActive = wraps.length
    }

    update()
});

document.getElementById('m').addEventListener('click', function () {
    Swal.fire({
        title: "MUY BIEN!",
        text: "Has seleccionado la tarifa M",
        icon: "success"
    });
    tarifa = "M"
    document.getElementById("seccion-pasajeros").style.display = "grid"
    document.getElementById("seccion1").style.display = "none"
    currentActive++
    if (currentActive > wraps.length) {
        currentActive = wraps.length
    }

    update()
});

document.getElementById('l').addEventListener('click', function () {
    Swal.fire({
        title: "MUY BIEN!",
        text: "Has seleccionado la tarifa L",
        icon: "success"
    });
    tarifa = "L"
    document.getElementById("seccion1").style.display = "none"
    document.getElementById("seccion-pasajeros").style.display = "grid"
    currentActive++
    if (currentActive > wraps.length) {
        currentActive = wraps.length
    }

    update()
});

function showLoading(event, button) {
    event.preventDefault(); // Prevent form submission
  
    button.innerHTML = "Processing Payment...";
  
    setTimeout(function() {
      button.innerHTML = "Payment completed.";
    }, 3000); // Change to the desired duration in milliseconds
  }