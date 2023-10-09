from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template

from Model.Reservas import Reserva, ReseSchema

routes_reserva = Blueprint("routes_reserva", __name__)

rese_schema = ReseSchema()
reser_Schema = ReseSchema(many=True)

@routes_reserva.route('/reserva', methods=['GET'])
def obtenerreser():
    returnall = Reserva.query.all()
    result_reser = reser_Schema.dump(returnall)
    return jsonify(result_reser)

#-------------------CRUD---------------------------------
@routes_reserva.route('/eliminarreserva/<id>', methods=['GET'] )
def eliminarreserva(id):
    rese = Reserva.query.get(id)
    db.session.delete(rese)
    db.session.commit()
    return jsonify(rese_schema.dump(rese))

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