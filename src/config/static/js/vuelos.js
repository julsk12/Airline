const origenInputId = "origen";
const origenPanelId = "sugerencias-panel";

const destinoInputId = "destino";
const destinoPanelId = "sugerencias-modal";

configurarAutocompletado(origenInputId, origenPanelId);
configurarAutocompletado(destinoInputId, destinoPanelId);
destino = "";
origen = "";
function configurarAutocompletado(inputId, panelId) {
  const input = document.getElementById(inputId);
  const sugerenciasPanel = document.getElementById(panelId);

  input.addEventListener("input", function () {
    const query = input.value.toLowerCase();

    axios
      .get(`/api/select?query=${query}`)
      .then((response) => {
        const sugerencias = Object.values(response.data);
        if (sugerencias.length > 0) {
          mostrarSugerencias(sugerencias);
        } else {
          ocultarSugerencias();
        }
      })
      .catch((error) => {
        console.error("Error al obtener sugerencias:", error);
      });
  });

  function mostrarSugerencias(sugerencias) {
    sugerenciasPanel.innerHTML = "";

    sugerencias.forEach((sugerencia) => {
      const sugerenciaItem = document.createElement("div");
      sugerenciaItem.classList.add("sugerencia-item");
      sugerenciaItem.innerHTML = `<strong>${sugerencia.nombre}</strong><br>${sugerencia.direccion}`;
      sugerenciaItem.addEventListener("click", function () {
        input.value = sugerencia.direccion;

        ocultarSugerencias();
      });
      sugerenciasPanel.appendChild(sugerenciaItem);
    });

    sugerenciasPanel.style.display = "block";
  }

  function ocultarSugerencias() {
    sugerenciasPanel.style.display = "none";
  }

  document.addEventListener("click", function (event) {
    if (
      !input.contains(event.target) &&
      !sugerenciasPanel.contains(event.target)
    ) {
      ocultarSugerencias();
    }
  });
}

function crear_vuelo() {
  origen = document.getElementById("origen").value;
  destino = document.getElementById("destino").value;
  console.log(origen, destino);
  axios
    .post(
      "/api/crear_vuelos",
      {
        origen: origen,
        destino: destino,
        mascota: "no",
      },
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    )
    .then((res) => {
      console.log(res.data);
      window.onload = buscarvuelos();
    })
    .catch((err) => {
      console.log(err);
    });
}

function buscarvuelos() {
  morfismo = document.getElementById("vuelos");
  axios
    .get("/api/crear_vuelos", {
      responseType: "json",
    })
    .then(function (res) {
      console.log(res.data);
      let datos = res.data;
      var length = Object.keys(datos).length + 1;
      let listper = "";

      for (let index = 1; index < length; index++) {
        if (datos[index].origen === origen && datos[index].destino === destino) {
          listper += `
              <div class="cards-vuelos col-md-4 mb-4">
              <div class="card overflow-hidden shadow">
                <div class="card-body py-4 px-3">
                  <div class="d-flex flex-column flex-lg-row justify-content-between mb-3">
                    <h6 class="text-secondary fw-medium"><a class="link-900 text-decoration-none stretched-link"
                        href="#!">${datos[index].ciudadOrigen}</a>
                    </h5>
                    <h6 class="text-secondary fw-medium">${datos[index].ciudadDestino}
                    </h6>
                    <span style="color: black;" class="fs-1 fw-medium">${datos[index].precio}</span>
                  </div>
                  <div class="d-flex align-items-center"> <img src="../../static/img/dest/navigation.svg"
                      style="margin-right: 14px" width="20" alt="navigation" /><span style="color: black;" class="fs-0 fw-medium">${datos[index].duracion}</span></div>
                </div>
              </div>
            </div>
              `;
        }
      }

      morfismo.innerHTML = listper;
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
console.clear();

function retorno2(){
    var fechaVueltaInput = document.getElementById("fechaVuelta");
    fechaVueltaInput.style.display = "none";
  };

  function retorno(){
    var fechaVueltaInput = document.getElementById("fechaVuelta");
    fechaVueltaInput.style.display = "block";
  };
