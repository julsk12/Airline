const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Configura un proxy para redirigir las solicitudes a la API de Amadeus
const apiProxy = createProxyMiddleware('/api', {
  target: 'https://test.api.amadeus.com', // URL de la API de Amadeus
  changeOrigin: true,
  pathRewrite: {
    '^/api': '', // Elimina '/api' de la URL de destino
  },
});

app.use('/api', apiProxy);

// Configura el servidor para escuchar en tu puerto local (por ejemplo, 5000)
app.listen(5000, () => {
  console.log('Servidor proxy en ejecución en el puerto 5000');
});