from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template

from Model.Pagos import Pagos, PagSchema

routes_pagos =  Blueprint("routes_pagos", __name__)

pago_schema = PagSchema()
pag_Schema = PagSchema(many=True)

@routes_pagos.route('/pagos', methods=['GET'])
def obtenerpago():
    returnall = Pagos.query.all()
    result_pag = pag_Schema.dump(returnall)
    return jsonify(result_pag)

#-------------------CRUD---------------------------------
@routes_pagos.route('/eliminarpago/<id>', methods=['GET'] )
def eliminarpago(id):
    pago = Pagos.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(pago_schema.dump(pago))

@routes_pagos.route('/actualizarpagos', methods=['POST'] )
def actualizarpagos():
    id = request.json['id']
    metodopago = request.json['metodopago']
    fechaPago = request.json['fechaPago']
    monto = request.json['monto']
    estadopago = request.json['estadopago']

    apago = Pagos.query.get(id)
    apago.Pagos = metodopago
    apago.Pagos = fechaPago
    apago.Pagos = monto
    apago.Pagos = estadopago

    db.session.commit()
    return redirect('/pagos')

@routes_pagos.route('/guardarpago', methods=['POST'] )
def guardar_reserva():
    pago = request.json['metodopago','fechaPago', 'monto', 'estadopago']
    new_pago = Pagos(pago)
    db.session.add(new_pago)
    db.session.commit()
    return redirect('/vuelo')