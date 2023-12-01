window.onload = viewtarifas()

function viewtarifas() {
  let morfismo = document.getElementById('tarifas');
  let Origen = document.getElementById('origen').value;
  let Destino = document.getElementById('destino').value;

  axios.get('/api/info_tarifa', {
    responseType: 'json'
  })
    .then(function (res) {
      console.log("aqui estan los datos",res.data);
      let datos = res.data; 
      var length = Object.keys(datos).length + 1;
      let listper = '';
      
      for (let index = 1; index < length; index++) {
          listper += `
          <div class="cards__card card">
            <p class="card__price">Tarifa S</p>
            <h2 class="card__heading">Viaje ligero</h2>
            <ul role="list" class="card__bullets flow">
                <li style="color: black;">${datos[index].tarifaS}</li>
            </ul>
            <h2 class="card__heading">Restricciones</h2>
            <ul role="list" class="card__bullets flow">
                <li style="color: black;">${datos[index].RestriccionestarifaS}</li>
            </ul>
                </div>
          
                <div class="cards__card card">
                  <p class="card__price">Tarifa M</p>
                  <h2 class="card__heading">Mas confort</h2>
                  <ul role="list" class="card__bullets flow">
                    <li style="color: black;">${datos[index].tarifaM}</li>
                  </ul>
                  <h2 class="card__heading">Restricciones</h2>
                  <ul role="list" class="card__bullets flow">
                      <li style="color: black;">${datos[index].RestriccionestarifaM}</li>
                  </ul>
                </div>
          
                <div class="cards__card card">
                  <p class="card__price">Tarifa L</p>
                  <h2 class="card__heading">Mas flexible</h2>
                  <ul role="list" class="card__bullets flow">
                    <li style="color: black;">${datos[index].tarifaL}</li>
                  </ul>
                  <h2 class="card__heading">Restricciones</h2>
                  <ul role="list" class="card__bullets flow">
                      <li style="color: black;">${datos[index].RestriccionestarifaL}</li>
                  </ul>
                </div>
              
          `
        
        ;
      }
      morfismo.innerHTML = listper;
      
      

    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
console.clear();

const cardsContainer = document.querySelector(".cards");
const cardsContainerInner = document.querySelector(".cards__inner");
const cards = Array.from(document.querySelectorAll(".card"));
const overlay = document.querySelector(".overlay");

const applyOverlayMask = (e) => {
  const overlayEl = e.currentTarget;
  const x = e.pageX - cardsContainer.offsetLeft;
  const y = e.pageY - cardsContainer.offsetTop;

  overlayEl.style = `--opacity: 1; --x: ${x}px; --y:${y}px;`;
};

const createOverlayCta = (overlayCard, ctaEl) => {
  const overlayCta = document.createElement("div");
  overlayCta.classList.add("cta");
  overlayCta.textContent = ctaEl.textContent;
  overlayCta.setAttribute("aria-hidden", true);
  overlayCard.append(overlayCta);
};

const observer = new ResizeObserver((entries) => {
  entries.forEach((entry) => {
    const cardIndex = cards.indexOf(entry.target);
    let width = entry.borderBoxSize[0].inlineSize;
    let height = entry.borderBoxSize[0].blockSize;

    if (cardIndex >= 0) {
      overlay.children[cardIndex].style.width = `${width}px`;
      overlay.children[cardIndex].style.height = `${height}px`;
    }
  });
});

const initOverlayCard = (cardEl) => {
  const overlayCard = document.createElement("div");
  overlayCard.classList.add("card");
  createOverlayCta(overlayCard, cardEl.lastElementChild);
  overlay.append(overlayCard);
  observer.observe(cardEl);
};

cards.forEach(initOverlayCard);
document.body.addEventListener("pointermove", applyOverlayMask);