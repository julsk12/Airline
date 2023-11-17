const origenInputId = 'origen';
const origenPanelId = 'sugerencias-panel';

const destinoInputId = 'destino';
const destinoPanelId = 'sugerencias-modal';

configurarAutocompletado(origenInputId, origenPanelId);
configurarAutocompletado(destinoInputId, destinoPanelId);
destino = "";
origen = "";
function configurarAutocompletado(inputId, panelId) {
    const input = document.getElementById(inputId);
    const sugerenciasPanel = document.getElementById(panelId);

    input.addEventListener('input', function () {
        const query = input.value.toLowerCase();

        axios.get(`/api/select?query=${query}`)
            .then(response => {
                const sugerencias = Object.values(response.data);
                if (sugerencias.length > 0) {
                    mostrarSugerencias(sugerencias);
                } else {
                    ocultarSugerencias();
                }
            })
            .catch(error => {
                console.error('Error al obtener sugerencias:', error);
            });
    });

    function mostrarSugerencias(sugerencias) {
        sugerenciasPanel.innerHTML = '';

        sugerencias.forEach(sugerencia => {
            const sugerenciaItem = document.createElement('div');
            sugerenciaItem.classList.add('sugerencia-item');
            sugerenciaItem.innerHTML = `<strong>${sugerencia.nombre}</strong><br>${sugerencia.direccion}`;
            sugerenciaItem.addEventListener('click', function () {
                input.value = sugerencia.nombre;
                origen = sugerencia.direccion;
                destino = sugerencia.direccion;
                console.log(origen, destino);
                ocultarSugerencias();
            });
            sugerenciasPanel.appendChild(sugerenciaItem);
        });

        sugerenciasPanel.style.display = 'block';
    }

    function ocultarSugerencias() {
        sugerenciasPanel.style.display = 'none';
    }

    document.addEventListener('click', function (event) {
        if (!input.contains(event.target) && !sugerenciasPanel.contains(event.target)) {
            ocultarSugerencias();
        }
    });
}

function crear_vuelo(){
    axios.post('/api/crear_vuelos', {
        origen: origen,
        destino: destino,
        mascota: "si"
        
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'
    
        }
    }
    ).then((res) => {
        console.log(res.data)
    })
    .catch((err) => {
        console.log(err);
    })
    
    
}