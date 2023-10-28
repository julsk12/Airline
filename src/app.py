from flask import Flask,  redirect, request, jsonify, json, session, render_template, Blueprint
from config.db import db, app, ma
from flask_cors import CORS

from api.Users import routes_users
from api.aerolinea import routes_aerolinea
from api.aeropuerto import routes_aeropuerto
from api.vuelos import routes_vuelos
from api.pagos import routes_pagos
from api.reservas import routes_reserva
from api.comentario import routes_comentar
from api.detallespago import routes_detalles
from api.algo import routes_algo


app.register_blueprint(routes_users, url_prefix="/api")
app.register_blueprint(routes_aerolinea, url_prefix="/api")
app.register_blueprint(routes_aeropuerto, url_prefix="/api")
app.register_blueprint(routes_vuelos, url_prefix="/api")
app.register_blueprint(routes_pagos, url_prefix="/api")
app.register_blueprint(routes_reserva, url_prefix="/api")
app.register_blueprint(routes_comentar, url_prefix="/api")
app.register_blueprint(routes_detalles, url_prefix="/api")

CORS(app)

@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return  render_template('index.html', titles=titulo)

@app.route("/algo")
def otr():
    return "hola mundo"


if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
