const progress = document.getElementById('progress')
const back = document.getElementById('back')
const next = document.getElementById('next')
const wraps = document.querySelectorAll('.text-wrap')
let tarifa = ""
let currentActive = 1

next.addEventListener('click', () => {
    currentActive++
    if(currentActive > wraps.length) {
        currentActive = wraps.length
    }

    update()
})

back.addEventListener('click', () => {
    currentActive--
    if(currentActive < 1) {
        currentActive = 1
    }

    update()
})

function update() {
    wraps.forEach((wrap, index) => {
        if(index < currentActive) {
            wrap.classList.add('active')
        } else {
            wrap.classList.remove('active')
        }
    })

    const actives = document.querySelectorAll('.active')
    progress.style.width = (actives.length - 1) / (wraps.length - 1)* 80 + '%'

    if(currentActive === 1) {
        back.disabled = true
    } else if(currentActive === wraps.length) {
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
        <label style="margin-top: 20px;">Pasajero ${index +1}</label><br>
        <label style="fw-bold text-danger mb-3" for="genero">Género:</label>
        <select class="input-info" id="genero">
            <option value="masculino">Masculino</option>
            <option value="femenino">Femenino</option>
            <option value="otro">Otro</option>
        </select>
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_nombre">Identificación:</label>
        <input class="input-info" type="text" id="identificacion">
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_nombre">Primer nombre:</label>
        <input class="input-info" type="text" id="primer_nombre">
        <br>
        <label style="fw-bold text-danger mb-3" for="primer_apellido">Primer apellido:</label>
        <input class="input-info" type="text" id="primer_apellido">

        `}
    morfismo.innerHTML = lista;
}

window.onload = viewtarifas()
var preciotar;
var pre_por;
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
        document.getElementById("seccion1").style.display = "none"
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
        document.getElementById("seccion1").style.display = "none"
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
        document.getElementById("seccion1").style.display = "none"
    });

    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}



