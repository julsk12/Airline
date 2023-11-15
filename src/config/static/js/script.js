window.addEventListener('load', function() {
  viewtarifas();
});

function viewtarifas() {
  let morfismo = document.getElementById('tarifas');

  axios.get('/api/crear_vuelos', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 1;
      let listper = '';
      
      for (let index = 1; index < length; index++) {
        listper += `<h2 class="card__heading">Tarifa S</h2>
        <p class="card__price">Viaje ligero</p>
        <ul role="list" class="card__bullets flow">
          <li>${datos[index].tarifaS}</li>
          <li>Email support</li>
        </ul>`;
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
