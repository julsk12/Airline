const progress = document.getElementById("progress");
const back = document.getElementById("back");
const next = document.getElementById("next");
const wraps = document.querySelectorAll(".text-wrap");
let tarifa = "";
let currentActive = 1;
var info_pasajeros = {};

next.addEventListener("click", () => {
  if (currentActive === 1) {
    if (tarifa === "") {
      Swal.fire({
        title: "Oops!",
        text: "Por favor seleciona una tarifa",
        icon: "error",
      });
    } else {
      document.getElementById("seccion-pasajeros").style.display = "grid";
      document.getElementById("seccion1").style.display = "none";
      currentActive++;
      if (currentActive > wraps.length) {
        currentActive = wraps.length;
      }
      update();
    }
  }
  if (currentActive === 2) {
    let pasajeros = document.getElementById("Pasajeros").value;
    for (let index = 1; index <= pasajeros; index++) {
      console.log(pasajeros);
      let primer_nombre = document.getElementById(
        `nombre_pasajero${index}`
      ).value;
      let genero = document.getElementById(`genero_pasajero${index}`).value;
      let primer_apellido = document.getElementById(
        `apellido_pasajero${index}`
      ).value;
      let pasajero = primer_nombre + primer_apellido + genero;
      info_pasajeros["nombre"] = primer_nombre;
      info_pasajeros["apellido"] = primer_apellido;
      info_pasajeros["gener"] = genero;
      console.log(primer_apellido, primer_nombre, genero);
      if (primer_nombre === "" || primer_apellido === "" || genero === "") {
        Swal.fire({
          title: "Oops!",
          text: "Por favor llena todos los campos",
          icon: "error",
        });
      } else {
        currentActive++;
        if (currentActive > wraps.length) {
          currentActive = wraps.length;
        }
        update();
      }
    }
  }
  if (currentActive === 3) {
    let pago = document.getElementById("pago");
    document.getElementById("seccion-pasajeros").style.display = "none";
    pago.style.display = "block";
  }
});

function validar_datos() {}

back.addEventListener("click", () => {
  if (currentActive === 2) {
    document.getElementById("seccion1").style.display = "flex";
    document.getElementById("seccion-pasajeros").style.display = "none";
  }
  if (currentActive === 3) {
    document.getElementById("seccion-pasajeros").style.display = "block";
    document.getElementById("pago").style.display = "none";
  }
  currentActive--;
  if (currentActive < 1) {
    currentActive = 1;
  }

  update();
});

function update() {
  wraps.forEach((wrap, index) => {
    if (index < currentActive) {
      wrap.classList.add("active");
    } else {
      wrap.classList.remove("active");
    }
  });

  const actives = document.querySelectorAll(".active");
  progress.style.width = ((actives.length - 1) / (wraps.length - 1)) * 80 + "%";

  if (currentActive === 1) {
    back.disabled = true;
  } else if (currentActive === wraps.length) {
    next.disabled = true;
  } else {
    back.disabled = false;
    next.disabled = false;
  }
}

function npasajeros() {
  let pasajeros = document.getElementById("Pasajeros").value;
  morfismo = document.getElementById("seccion2");
  console.log(pasajeros);
  lista = "";
  for (let index = 1; index < pasajeros; index++) {
    lista += `
        <label id="pasajero${index + 1}" style="margin-top: 20px;">Pasajero ${
      index + 1
    }</label><br>
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
        `;
  }
  morfismo.innerHTML = lista;
}

window.onload = viewtarifas();
var preciotar;
var pre_por;
var tar;
function viewtarifas() {
  let morfismo = document.getElementById("seccion1");

  axios
    .get("/api/info_tarifa", {
      responseType: "json",
    })
    .then(function (res) {
      console.log("aqui estan los datos", res.data);
      let datos = res.data;
      var length = Object.keys(datos).length + 1;
      let listper = "";

      for (let index = 1; index < length; index++) {
        preciotar = datos[index].precio;
        console.log(preciotar);
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
          `;
      }
      morfismo.innerHTML = listper;

      document.getElementById("s").addEventListener("click", function () {
        premaspor = preciotar * 0.12;
        precmas = preciotar + premaspor;
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
.catch((err) => {
  console.log(err);
});

}


function carga() {
  let numero_tarjeta = document.getElementById("card-number").value;
  let cvv = document.getElementById("cvv").value;
  let nombre = document.getElementById("card-holder").value;
  let fecha_expiracion = document.getElementById("expiry-date").value;

  const regexcard = new RegExp("^[0-9]{13,16}$");
  const numero_isValid = regexcard.test(numero_tarjeta);

  const regex_expiracion = new RegExp("^(0[1-9]|1[0-2])\\/[0-9]{2}$");
  const fe_isValid = regex_expiracion.test(fecha_expiracion);

  const regex_nombre = new RegExp("^[A-Za-z]{2,48}$");
  const nombre_isValid = regex_nombre.test(nombre);

  const regex = new RegExp("^[0-9]{3,4}$");
  const isValid = regex.test(cvv);

  if (
    numero_isValid === true &&
    fe_isValid === true &&
    nombre_isValid === true &&
    isValid === true
  ) {
    setTimeout(function () {
        Swal.fire({
            title: "MUY BIEN!",
            text: "Has seleccionado la tarifa L",
            icon: "success",
          });
    }, 3000); // Change to the desired duration in milliseconds
  }else{
    Swal.fire({
        title: "Oops!",
        text: "Por favor llena todos los campos",
        icon: "error",
      });
  }
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