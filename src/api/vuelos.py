from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template

from Model.Vuelos import Vuelo, FliesSchema

routes_vuelos = Blueprint("routes_vuelos",  __name__)

vuelo_schema = FliesSchema()
flies_Schema = FliesSchema(many=True)

@routes_vuelos.route('/vuelo', methods=['GET'])
def obtenervuelos():
    returnall = Vuelo.query.all()
    result_flies = flies_Schema.dump(returnall)
    return jsonify(result_flies)

#-------------------CRUD---------------------------------
@routes_vuelos.route('/eliminarvuelos/<id>', methods=['GET'] )
def eliminarvuelos(id):
    fly = Vuelo.query.get(id)
    db.session.delete(fly)
    db.session.commit()
    return jsonify(vuelo_schema.dump(fly))

@routes_vuelos.route('/actualizarvuelos', methods=['POST'] )
def actualizarvuelos():
    id = request.json['id']
    aerolinea = request.json['aerolinea']
    ciudadOrigen = request.json['ciudadOrigen']
    ciudadDestino = request.json['ciudadDestino']
    fechaHSalida = request.json['fechaHSalida']
    fechaHLlegada = request.json['fechaHLlegada']
    asientosDisponibles = request.json['asientosDisponibles']    
    precio = request.json['precio']
    tipoAvion = request.json['tipoAvion']    
    numeroEscalas = request.json['numeroEscalas']
    duracionVuelo = request.json['duracionVuelo']

    avuelos = Vuelo.query.get(id)
    avuelos.Vuelo = aerolinea
    avuelos.Vuelo = ciudadOrigen
    avuelos.Vuelo = ciudadDestino
    avuelos.Vuelo = fechaHSalida
    avuelos.Vuelo = fechaHLlegada
    avuelos.Vuelo = asientosDisponibles
    avuelos.Vuelo = precio
    avuelos.Vuelo = tipoAvion
    avuelos.Vuelo = numeroEscalas
    avuelos.Vuelo = duracionVuelo

    db.session.commit()
    return redirect('/vuelo')

@routes_vuelos.route('/guardarvuelos', methods=['POST'] )
def guardar_vuelos():
    fly = request.json['aerolinea','ciudadOrigen', 'ciudadDestino', 'fechaHSalida', 
'fechaHLlegada', 'asientosDisponibles', 'precio', 'tipoAvion', 'numeroEscalas', 'duracionVuelo']
    new_vuelo = Vuelo(fly)
    db.session.add(new_vuelo)
    db.session.commit()
    return redirect('/vuelo')