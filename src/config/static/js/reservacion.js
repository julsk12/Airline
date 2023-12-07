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
    console.log(currentActive)
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
        document.getElementById("puestos").style.display = "block";
        document.getElementById("seccion-pasajeros").style.display = "none";
        currentActive++;
        if (currentActive > wraps.length) {
          currentActive = wraps.length;
        }
        update();
      console.log(currentActive)

      }
    }
  }else if (currentActive === 3) {
    const selectedSeatInfo = document.getElementById('selected-seat-info').innerText;

    if (selectedSeatInfo) {
      reservacion(tar, selectedSeats);
      
      currentActive++;
      if (currentActive > wraps.length) {
        currentActive = wraps.length;
      }
      update();
    } else {
      Swal.fire({
        title: "Oops!",
        text: "Por favor Selecciona un asiento",
        icon: "error",
      });
    }
    selectedSeats = [];
    document.getElementById('selected-seat-info').innerText = '';
  }

});

back.addEventListener("click", () => {
  if (currentActive === 2) {
    document.getElementById("seccion1").style.display = "flex";
    document.getElementById("seccion-pasajeros").style.display = "none";
    currentActive--;
    if (currentActive < 1) {
      currentActive = 1;
    }
  
    update();
  }
  if (currentActive === 3) {
    document.getElementById("seccion-pasajeros").style.display = "block";
    document.getElementById("puestos").style.display = "none";
    currentActive--;
    if (currentActive < 1) {
      currentActive = 1;
    }
  
    update();
  }
  if (currentActive === 4) {
    document.getElementById("puestos").style.display = "block";
    document.getElementById("pago").style.display = "none";
    currentActive--;
    if (currentActive < 1) {
      currentActive = 1;
    }
  
    update();
  }

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
          icon: "success",
        });
        tarifa = "S";
        tar = "S";
        document.getElementById("seccion-pasajeros").style.display = "grid";
        document.getElementById("seccion1").style.display = "none";
        currentActive++;
        if (currentActive > wraps.length) {
          currentActive = wraps.length;
        }
        update();
      });

      document.getElementById("m").addEventListener("click", function () {
        premaspor = preciotar * 0.24;
        precmas = preciotar + premaspor;
        pre_por = precmas;
        console.log(pre_por);
        Swal.fire({
          title: "MUY BIEN!",
          text: "Has seleccionado la tarifa M",
          icon: "success",
        });
        tarifa = "M";
        tar = "M";
        document.getElementById("seccion-pasajeros").style.display = "grid";
        document.getElementById("seccion1").style.display = "none";
        currentActive++;
        if (currentActive > wraps.length) {
          currentActive = wraps.length;
        }

        update();
      });
      document.getElementById("l").addEventListener("click", function () {
        premaspor = preciotar * 0.3;
        precmas = preciotar + premaspor;
        pre_por = precmas;

        console.log(pre_por);
        Swal.fire({
          title: "MUY BIEN!",
          text: "Has seleccionado la tarifa L",
          icon: "success",
        });
        tarifa = "L";
        tar = "L";
        document.getElementById("seccion-pasajeros").style.display = "grid";
        document.getElementById("seccion1").style.display = "none";
        currentActive++;
        if (currentActive > wraps.length) {
          currentActive = wraps.length;
        }

        update();
      });
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}

function carga() {
  let numero_tarjeta = document.getElementById("card-number").value;
  let cvv = document.getElementById("cvv").value;
  let fecha_expiracion = document.getElementById("expiry-date").value;

  const regexcard = new RegExp("^[0-9]{13,16}$");
  const numero_isValid = regexcard.test(numero_tarjeta);

  const regex_expiracion = new RegExp("^(0[1-9]|1[0-2])\\/[0-9]{2}$");
  const fe_isValid = regex_expiracion.test(fecha_expiracion);

  const regex = new RegExp("^[0-9]{3,4}$");
  const isValid = regex.test(cvv);

  if (
    numero_isValid === true &&
    fe_isValid === true &&
    isValid === true
  ) {
    setTimeout(function () {
      Swal.fire({
        title: "MUY BIEN!",
        text: "Su pago ha sido exitoso",
        icon: "success",
      });
    }, 1000);

    setTimeout(function () {
      window.location.href = "/"
    },3000)


  } else {
    Swal.fire({
      title: "Oops!",
      text: "Por favor llena todos los campos",
      icon: "error",
    });
  }
}


console.clear();

const rows = 6;
const cols = 7;
let selectedSeats = [];
let pasajeros = document.getElementById("Pasajeros").value;

// Número de asientos que se pueden seleccionar, seleccionados aleatorio y espacio para el mapa
const seatsToSelect = pasajeros;
const seatsToSelectaleator = 25;
const seatMapContainer = document.getElementById("seat-map");
const columnLetters = ["A", "B", "C", "D", "E", "F", "G"];

// generara el mapa de asientos y demas
function generateSeatMap(rows, cols) {
  for (let row = 1; row <= rows; row++) {
    for (let col = 1; col <= cols; col++) {
      const seat = document.createElement("div");
      seat.className = "seat";
      seat.dataset.row = row;
      seat.dataset.col = col;
      if (columnLetters[col - 1] === "D") {
        seat.classList.add("pasillo");
        seat.removeEventListener("click", toggleSeat);
      } else {
        seat.addEventListener("click", toggleSeat);
      }

      seatMapContainer.appendChild(seat);
    }
    seatMapContainer.appendChild(document.createElement("br"));
  }
}

//selección del asiento
function toggleSeat() {
  const row = this.dataset.row;
  const col = this.dataset.col;
  const columnLetter = columnLetters[col - 1];
  const seatReference = `${columnLetter}-${row}`;

  if (this.classList.contains("auto-selected")) {
    return;
  }

  if (this.classList.contains("selected")) {
    this.classList.remove("selected");
    selectedSeats = selectedSeats.filter((seat) => seat !== seatReference);
  } else if (selectedSeats.length < seatsToSelect) {
    this.classList.add("selected");
    selectedSeats.push(seatReference);
  }
  document.getElementById(
    "selected-seat-info"
  ).innerText = `${selectedSeats.join(", ")}`;
}


//ocupar automáticamente algunos asientos al azar al cargar la página
function autoSelectSeats() {
  const allSeats = document.querySelectorAll(".seat");
  const totalSeats = allSeats.length;

  const randomSeatIndices = Array.from({ length: seatsToSelectaleator }, () =>
    Math.floor(Math.random() * totalSeats)
  );

  randomSeatIndices.forEach((index) => {
    const seat = allSeats[index];
    seat.classList.add("auto-selected");
    selectedSeats.push(
      `${columnLetters[seat.dataset.col - 1]}-${seat.dataset.row}`
    );
  });
}

// cargar automaticamente las funciones anteriores al iniciarpre_
window.onload = function () {
  generateSeatMap(rows, cols);
  autoSelectSeats();
  selectedSeats = [];
};

function reservacion(tar, selectedSeats) {
  id_usuario = document.getElementById("correo");
  nombre = document.getElementById("nombre_pasajero1");
  apellido = document.getElementById("apellido_pasajero1");
  nombre_completo = nombre + "" + apellido;
  // estadoReserva = "aprobada";
  asientosReservados = document.getElementById("Pasajeros").value;
  nasientos = selectedSeats;
  tipoboleto = tar;
  console.log(id_usuario, nombre_completo, asientosReservados, nasientos, tipoboleto);
  axios
    .post(
      "/api/savereservas",
      {
        idusuario: id_usuario.value,
        asientosReservados: asientosReservados,
        nasientos: nasientos,
        tipoboleto: tipoboleto,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
    .then((res) => {
      if (res.data === "El cliente acargo no está regitrado") {
        Swal.fire({
          title: "Oops!",
          text: "Debe registrarse antes de continuar",
          icon: "error",
        });
      } else {
          document.getElementById("pago").style.display = "block";
          document.getElementById("puestos").style.display = "none";
      }
    })
    .catch((err) => {
      console.log(err);
    });
}

function validateInput(event) {
  var input = event.target.value;
  var regex = /^[a-zA-Z\s]+$/;
  if (!regex.test(input)) {
    event.target.value = input.replace(/[^a-zA-Z\s]/g, "");
  }
}

function validateInputnumber(event) {
  var input = event.target.value;
  var regex = /^[0-9]+$/;
  if (!regex.test(input)) {
    event.target.value = input.replace(/[^0-9\s]/g, "");
  }
}

function totalpagar(){
   let total_pagar = document.getElementById("total_pagar")
   total_pagar.innerText = pre_por
}