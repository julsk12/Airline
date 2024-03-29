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
  fecha_vuelta = document.getElementById("fecha_vuelta").value;
  morfismo = document.getElementById("cvuelos");
  modalvuelo = document.getElementById("miModal");

  var fecha_vuel;
  if (fecha_vuelta === "") {
    fecha_vuel = "2023-12-30";
  } else {
    fecha_vuel = fecha_vuelta;
  }

  axios
    .post(
      "/api/crear_vuelos",
      {
        origen: origen,
        destino: destino,
        mascota: "si",
        fecha_vuelta: fecha_vuelta,
      },
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    )
    .then((res) => {
      console.log(res.data);
      let datos = res.data;
      var length = Object.keys(datos).length + 1;
      let listper = "";
      let vuelo_modal = "";

      for (let index = 1; index < length; index++) {
        listper += `
        <div class="cards-vuelos col-md-4 mb-4">
        <div style="background-image: url(../../static/img/steps/bg.png);

        background-repeat: no-repeat; border: none; min-width: fit-content; margin: 10px;" class="card overflow-hidden shadow" onclick="mostrarDetalles(
        '${datos[index].ciudadOrigen}',
        '${datos[index].ciudadDestino}',
        '${datos[index].fechaHSalida}',
        '${datos[index].fechaHLlegada}')">
          <div class="card-body py-4 px-3">
            <div class="d-flex flex-column flex-lg-row justify-content-between mb-3">
              <h6 class="text-secondary fw-medium"><button data-bs-toggle="modal" data-bs-target="#miModal"
                  class="btn-mio link-900 text-decoration-none stretched-link">${datos[index].ciudadOrigen}</button>
              </h6>
              <h6 class="text-secondary fw-medium">${datos[index].ciudadDestino}
              </h6>
              <span style="color: black;" class="fs-1 fw-medium">$ ${datos[index].precio}</span>
            </div>
            <div class="d-flex align-items-center"style="color: black; font-size: 20px !important;  min-width: fit-content;" > <img src="../../static/img/dest/navigation.svg"
                style=" margin-right: 14px" width="20" alt="navigation" />N° Escalas:  <span style="color: black; font-size: 30px !important;"
                class="fs-0 fw-medium">${datos[index].duracion}</span>
              </div>
              </div>
            </div>
          </div>
                `;
        vuelo_modal += `
          <div style="height: 110vh;max-height: fit-content;width: 90%;max-width: fit-content;min-width: fit-content;min-height: fit-content;" class="modal-dialog">
                          <div style="border-radius: 129px 20px 129px 20px;" class="modal-content">
                          <button type="button" class="btn-close" data-bs-dismiss="modal"aria-label="Cerrar"></button>
                          <div class="modal-body">
                            <div class="articule">
                              <h1 class="fs-xl-10 fs-lg-8 fs-7 fw-bold font-cursive text-capitalize">${datos[index].ciudadOrigen}</h1>
                              <h1 class="fs-xl-10 fs-lg-8 fs-7 fw-bold font-cursive text-capitalize">${datos[index].ciudadDestino}</h1>
                              <p class="ppp mb-0 fw-medium">Fecha Salida: ${datos[index].fechaHSalida}</p>
                              <p class="ppp mb-0 fw-medium">Fecha Llegada: ${datos[index].fechaHLlegada}</p>
                              <p class="ppp mb-0 fw-medium">Mascotas: ${datos[index].mascotas}</p>
                              <p class="ppp mb-0 fw-medium">Puestos disponibles: ${datos[index].puestos}</p>
                              <p class="ppp mb-0 fw-medium">$ ${datos[index].precio}</p>
                              <p class="ppp mb-0 fw-medium">Escalas:${datos[index].numeroEscalas}</p>
                              <p class="ppp mb-0 fw-medium">${datos[index].duracion} hora(s)</p>
                            </div>
                          </div>
                        <div style="
                        justify-content: center !important;
                    " class="modal-footer">
                        <a type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</a>
                        <a href="/fronted/indexreserva" type="button" class="btn btn-primary" style="
                        background-color: #3352ff;">Comprar Ticket</a>
                        </div>
                        </div>
                      </div>
                      `;
      }
      morfismo.innerHTML = listper;
      modalvuelo.innerHTML = vuelo_modal;
    })
    .catch((err) => {
      console.log(err);
    });
}

function mostrarDetalles(
  ciudadOrigen,
  ciudadDestino,
  fechaSalida,
  fechaLlegada
) {
  console.log("Ciudad Origen:", ciudadOrigen);
  console.log("Ciudad Destino:", ciudadDestino);
  console.log("Fecha Salida:", fechaSalida);
  console.log("Fecha Llegada:", fechaLlegada);
  axios
    .post(
      "/api/guardarglobales",
      {
        origen: ciudadOrigen,
        destino: ciudadDestino,
        fechaSalida: fechaSalida,
        fechaLlegada: fechaLlegada,
      },
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    )
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
}
console.clear();

function retorno2() {
  var fechaVueltaInput = document.getElementById("fechaVuelta");
  fechaVueltaInput.style.display = "none";
  vuelo_ida_vuelta((estado = 1));
}

function retorno() {
  var fechaVueltaInput = document.getElementById("fechaVuelta");
  fechaVueltaInput.style.display = "block";
  vuelo_ida_vuelta((estado = 2));
}

const modalTriggerButtons = document.querySelectorAll("[data-modal-target]");
const modals = document.querySelectorAll(".modal");
const modalCloseButtons = document.querySelectorAll(".modal-close");

modalTriggerButtons.forEach((elem) => {
  elem.addEventListener("click", (event) =>
    toggleModal(event.currentTarget.getAttribute("data-modal-target"))
  );
});
modalCloseButtons.forEach((elem) => {
  elem.addEventListener("click", (event) =>
    toggleModal(event.currentTarget.closest(".modal").id)
  );
});
modals.forEach((elem) => {
  elem.addEventListener("click", (event) => {
    if (event.currentTarget === event.target)
      toggleModal(event.currentTarget.id);
  });
});

document.addEventListener("keydown", (event) => {
  if (event.keyCode === 27 && document.querySelector(".modal.modal-show")) {
    toggleModal(document.querySelector(".modal.modal-show").id);
  }
});

function toggleModal(modalId) {
  const modal = document.getElementById(modalId);

  if (getComputedStyle(modal).display === "flex") {
    // alternatively: if(modal.classList.contains("modal-show"))
    modal.classList.add("modal-hide");
    setTimeout(() => {
      document.body.style.overflow = "initial";
      modal.classList.remove("modal-show", "modal-hide");
      modal.style.display = "none";
    }, 200);
  } else {
    document.body.style.overflow = "hidden";
    modal.style.display = "flex";
    modal.classList.add("modal-show");
  }
}
