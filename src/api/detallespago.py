from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

from Model.Detallespago import DetallesPago, DetallesSchema

routes_detalles =  Blueprint("routes_detalles", __name__)

deta_schema = DetallesSchema()
detalles_Schema = DetallesSchema(many=True)

@routes_detalles.route('/detalles', methods=['GET'])
def obtenerdetalles():
    returnall = DetallesPago.query.all()
    result_deta = DetallesSchema.dump(returnall)
    return jsonify(result_deta)

#-------------------CRUD---------------------------------
@routes_detalles.route('/eliminardetalles/<id>', methods=['GET'] )
def eliminardeta(id):
    detalle = DetallesPago.query.get(id)
    db.session.delete(detalle)
    db.session.commit()
    return jsonify(deta_schema.dump(detalle))

@routes_detalles.route('/actualizardetalle', methods=['POST'] )
def actualizarde():
    id = request.json['id']
    id_vuelo = request.json['id_vuelo']
    id_pago = request.json['id_pago']
    fechapago = request.json['fechapago']

    adetalles = DetallesPago.query.get(id)
    adetalles.DetallesPago = id_vuelo
    adetalles.DetallesPago = id_pago
    adetalles.DetallesPago = fechapago

    db.session.commit()
    return redirect('/detalles')

@routes_detalles.route('/guardardetalles', methods=['POST'] )
def guardar_deta():
    detalle = request.json['id_vuelo','id_pago', 'fechapago']
    new_detalle = DetallesPago(detalle)
    db.session.add(new_detalle)
    db.session.commit()
    return redirect('/detalles')