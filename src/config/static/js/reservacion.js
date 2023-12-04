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
        for (let index = 1; index <= pasajeros; index++) {
            console.log(pasajeros)
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
            } else {
                currentActive++
                if (currentActive > wraps.length) {
                    currentActive = wraps.length
                }
                update()
            }
        }
    }
    if (currentActive === 3) {
        let pago = document.getElementById("pago")
        document.getElementById("seccion-pasajeros").style.display = "none"

        pago.style.display = "block"
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
            <option value="mascota">Mascota</option>
            <option value="niño">Niño</option>
            <option value="bebe">Bebe</option>
            <option value="otro">Otro</option>
        </select>
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_nombre">Identificación:</label>
        <input class="input-info" type="text" id="identificacion">
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_nombre">Primer nombre:</label>
        <input class="input-info" type="text" id="nombre_pasajero${index}">
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_apellido">Primer apellido:</label>
        <input class="input-info" type="text" id="apellido_pasajero${index}">
        `}
    morfismo.innerHTML = lista;
}

window.onload = viewtarifas()
var preciotar;
var pre_por;
var tar;
function viewtarifas() {
  let morfismo = document.getElementById('seccion1');

  axios.get('/api/info_tarifa', {
    responseType: 'json'
  })
    .then(function (res) {
      console.log("aqui estan los datos",res.data);
      let datos = res.data; 
      var length = Object.keys(datos).length + 1;
      let listper = '';
      
      for (let index = 1; index < length; index++) {
            preciotar= datos[index].precio;
            console.log(preciotar)
          listper += `
          <div class="card card-tarifa" id="s">
          <h2>Tarifa S</h2>
          <p>${datos[index].tarifaS}</p>
          <h2>Restricciones</h2>
          <p>${datos[index].RestriccionestarifaS}</p>
      </div>
      <div class="card card-tarifa" id="m">
          <h2>Tarifa M</h2>
          <p>${datos[index].tarifaM}</p>
          <h2>Restricciones</h2>
          <p>${datos[index].RestriccionestarifaM}</p>
      </div>
      <div class="card card-tarifa" id="l">
          <h2>Tarifa L</h2>
          <p>${datos[index].tarifaL}</p>
          <h2>Restricciones</h2>
          <p>${datos[index].RestriccionestarifaL}</p>
      </div>  
          `
        
        ;
      }
      morfismo.innerHTML = listper;
      
      document.getElementById('s').addEventListener('click', function() {
    
        premaspor = preciotar*0.12
        precmas=preciotar + premaspor
        pre_por = precmas;

        console.log(pre_por);
        Swal.fire({
            title: "MUY BIEN!",
            text: "Has seleccionado la tarifa S",
            icon: "success"
          });
          tarifa = "S"
          tar = "S"
          document.getElementById("seccion-pasajeros").style.display = "grid"
          document.getElementById("seccion1").style.display = "none"
          currentActive++
          if (currentActive > wraps.length) {
              currentActive = wraps.length
          }
          update()
    });
    
    document.getElementById('m').addEventListener('click', function() {
        premaspor = preciotar*0.24
        precmas=preciotar + premaspor
        pre_por = precmas;

        console.log(pre_por);
        Swal.fire({
            title: "MUY BIEN!",
            text: "Has seleccionado la tarifa M",
            icon: "success"
          });
          tarifa = "M"
          tar = "M"
          document.getElementById("seccion-pasajeros").style.display = "grid"
          document.getElementById("seccion1").style.display = "none"
          currentActive++
          if (currentActive > wraps.length) {
              currentActive = wraps.length
          }
      
          update()
    });
    
    document.getElementById('l').addEventListener('click', function() {
        premaspor = preciotar*0.30
        precmas=preciotar + premaspor
        pre_por = precmas;

        console.log(pre_por);
        Swal.fire({
            title: "MUY BIEN!",
            text: "Has seleccionado la tarifa L",
            icon: "success"
          });
          tarifa = "L"
          tar = "L"
          document.getElementById("seccion1").style.display = "none"
          document.getElementById("seccion-pasajeros").style.display = "grid"
          currentActive++
          if (currentActive > wraps.length) {
              currentActive = wraps.length
          }
      
          update()
    });

    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}

function showLoading(event, button) {
    event.preventDefault(); // Prevent form submission

    button.innerHTML = "Processing Payment...";

    setTimeout(function () {
        button.innerHTML = "Payment completed.";
    }, 3000); // Change to the desired duration in milliseconds
}

function reservacion(tar) {
    id_usuario = document.getElementById('correo').value;
    nombre = document.getElementById('nombre_pasajero1').value;
    apellido = document.getElementById('apellido_pasajero1').value;
    nombre_completo = nombre + "" + apellido;
    estadoReserva = "aprobada";
    asientosReservados = document.getElementById('Pasajeros').value;
    nasientos = "A3, A4, B10"
    tipoboleto = tar;
    axios
      .post(
        "/api/savereservas",
        {
        id_usuario: id_usuario,
        nombre_completo: nombre_completo,
        estadoReserva: estadoReserva,
        asientosReservados: asientosReservados,
        nasientos: nasientos,
        tipoboleto: tipoboleto,
        },
        {
          headers: {
            "Content-Type": "multipart/form",
          },
        }
      )
      .then((res) => {
        console.log(res.data);
        if (res.data.message === "El cliente acargo no está regitrado") {
            Swal.fire({
                title: "Oops!",
                text: "Debe registrarse antes de continuar",
                icon: "error"
            });
        }else{
            console.clear();
        }
     
      })
      .catch((err) => {
        console.log(err);
      });
  
  }
  console.clear();