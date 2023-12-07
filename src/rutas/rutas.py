from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_home = Blueprint("routes_home", __name__)


@routes_home.route('/indexvuelos', methods=['GET'] )
def indexvuelos():
    return render_template('/public/vuelos.html')


@routes_home.route('/indexlogin', methods=['GET'] )
def indexlogin():
    return render_template('/public/login.html')


@routes_home.route('/indexregistro', methods=['GET'] )
def indexregistro():
    return render_template('/public/registro.html')

@routes_home.route('/indexhome', methods=['GET'] )
def indexhome():
    return render_template('/index.html')

@routes_home.route('/indexreserva', methods=['GET'] )
def indexreserva():
    return render_template('/public/reservacion.html')


@routes_home.route('/indexreserva2', methods=['GET'] )
def indexreserva2():
    return render_template('/public/reservacion2.html')

@routes_home.route('/indexperfil', methods=['GET'] )
def indexperfil():
    return render_template('/public/perfil.html')

@routes_home.route('/indexpoliticam', methods=['GET'] )
def indexpoliticam():
    return render_template('/public/politicam.html')