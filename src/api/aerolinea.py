from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

from Model.Aerolineas import Aerolinea, AirlineSchema

routes_aerolinea =  Blueprint("routes_aerolinea", __name__)

areo_schema = AirlineSchema()
air_Schema = AirlineSchema(many=True)

@routes_aerolinea.route('/aerolinea', methods=['GET'])
def obtenerairline():
    returnall = Aerolinea.query.all()
    result_air = air_Schema.dump(returnall)
    return jsonify(result_air)

#-------------------CRUD---------------------------------
@routes_aerolinea.route('/eliminarairline/<id>', methods=['GET'] )
def eliminarair(id):
    air = Aerolinea.query.get(id)
    db.session.delete(air)
    db.session.commit()
    return jsonify(areo_schema.dump(air))

@routes_aerolinea.route('/actualizarairline', methods=['POST'] )
def actualizarair():
    id = request.json['id']
    nombre = request.json['nombre']
    ubicacion = request.json['ubicacion']
    correo = request.json['correo']
    telefono = request.json['telefono']
    direccion = request.json['direccion']    
    politicaequipaje = request.json['politicaequipaje']

    aeline = Aerolinea.query.get(id)
    aeline.Aerolinea = nombre
    aeline.Aerolinea = ubicacion
    aeline.Aerolinea = correo
    aeline.Aerolinea = telefono
    aeline.Aerolinea = direccion
    aeline.Aerolinea = politicaequipaje

    db.session.commit()
    return redirect('/aerolinea')

@routes_aerolinea.route('/guardarairline', methods=['POST'] )
def guardar_air():
    air = request.json['nombre','ubicacion', 'correo', 'telefono', 'direccion', 'politicaequipaje']
    new_air = Aerolinea(air)
    db.session.add(new_air)
    db.session.commit()
    return redirect('/aerolinea')