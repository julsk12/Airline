from flask import Flask,  redirect, request, jsonify, json, session, render_template, Blueprint
from config.db import db, app, ma


from api.aeropuerto import routes_aeropuerto
from api.Users import routes_users
from api.aerolinea import routes_aerolinea
from api.vuelos import routes_vuelos
from api.pagos import routes_pagos
from api.reservas import routes_reserva
from api.comentario import routes_comentar
from api.detallespago import routes_detalles
from api.info_vuelos import routes_info
from api.algo import routes_algo
from rutas.rutas import routes_home


app.register_blueprint(routes_users, url_prefix="/api")
app.register_blueprint(routes_aerolinea, url_prefix="/api")
app.register_blueprint(routes_aeropuerto, url_prefix="/api")
app.register_blueprint(routes_vuelos, url_prefix="/api")
app.register_blueprint(routes_pagos, url_prefix="/api")
app.register_blueprint(routes_reserva, url_prefix="/api")
app.register_blueprint(routes_comentar, url_prefix="/api")
app.register_blueprint(routes_detalles, url_prefix="/api")
app.register_blueprint(routes_info, url_prefix="/api")
app.register_blueprint(routes_algo, url_prefix="/api")

app.register_blueprint(routes_home, url_prefix="/fronted")

@app.route("/")
def index():
    titulo = "Pagina Principal"
    return render_template('/index.html', titles=titulo)

@app.route("/algo")
def otr():
    return "hola mundo"

'''@app.before_first_request
def autollenar_aeropuertos():
    guardaraeropuerto()'''

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
