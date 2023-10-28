#from common.Toke import *
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

@routes_reserva.route('/actualizarreservas', methods=['POST'] )
def actualizarreservas():
    id = request.json['id']
    id_usuario = request.json['id_usuario']
    id_vuelo = request.json['id_vuelo']
    estadoreserva = request.json['estadoreserva']
    asientosReservados = request.json['asientosReservados']
    fechaReserva = request.json['fechaReserva']

    areser = Reserva.query.get(id)
    areser.Reserva = id_usuario
    areser.Reserva = id_vuelo
    areser.Reserva = estadoreserva
    areser.Reserva = asientosReservados
    areser.Reserva = fechaReserva

    db.session.commit()
    return redirect('/reserva')

@routes_reserva.route('/guardarreserva', methods=['POST'] )
def guardar_reserva():
    rese = request.json['id_usuario','id_vuelo', 'estadoreserva', 'asientosReservados', 'fechaReserva']
    new_reser = Reserva(rese)
    db.session.add(new_reser)
    db.session.commit()
    return redirect('/vuelo')