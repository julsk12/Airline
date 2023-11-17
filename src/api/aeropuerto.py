from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

from Model.Aeropuertos import Aeropuerto, AirportSchema

routes_aeropuerto =  Blueprint("routes_aeropuerto", __name__)

airpor_schema = AirportSchema()
airport_Schema = AirportSchema(many=True)

@routes_aeropuerto.route('/aeropuerto', methods=['GET'])
def obtenerairport():
    returnall = Aeropuerto.query.all()
    result_port = airport_Schema.dump(returnall)
    return jsonify(result_port)

#-------------------CRUD---------------------------------
@routes_aeropuerto.route('/eliminarairport/<id>', methods=['GET'] )
def eliminarport(id):
    port = Aeropuerto.query.get(id)
    db.session.delete(port)
    db.session.commit()
    return jsonify(airpor_schema.dump(port))

@routes_aeropuerto.route('/actualizarairport', methods=['POST'] )
def actualizarport():
    id = request.json['id']
    nombre = request.json['nombre']
    ubicacion = request.json['ubicacion']
    correo = request.json['correo']
    telefono = request.json['telefono']
    direccion = request.json['direccion']    
    serviciosdisponibles = request.json['serviciosdisponibles']

    aport = Aeropuerto.query.get(id)
    aport.Aeropuerto = nombre
    aport.Aeropuerto = ubicacion
    aport.Aeropuerto = correo
    aport.Aeropuerto = telefono
    aport.Aeropuerto = direccion
    aport.Aeropuerto = serviciosdisponibles

    db.session.commit()
    return redirect('/aeropuerto')

@routes_aeropuerto.route('/guardarairport', methods=['POST'] )
def guardar_port():
    port = request.json['nombre','ubicacion', 'correo', 'telefono', 'direccion', 'serviciosdisponibles']
    new_port = Aeropuerto(port)
    db.session.add(new_port)
    db.session.commit()
    return redirect('/aeropuerto')

#---------------Lista aeropuertos---------------------------------
@routes_aeropuerto.route('/select', methods=['GET'])
def obteneropciones():
    query = request.args.get('query', '').lower()
    returnall = Aeropuerto.query.filter(Aeropuerto.nombre.ilike(f"%{query}%")).all()
    
    datos = {}
    i = 0
    for vuelo in returnall:
        i += 1
        datos[i] = {
            'nombre': vuelo.nombre,
            'direccion': vuelo.direccion,            
        }

    return jsonify(datos)

@routes_aeropuerto.route('obtener_sugerencias', methods=['GET'])
def obtener_sugerencias():
    query = request.args.get('query', '').lower()

    # Filtrar aeropuertos basándose en la consulta
    sugerencias_base = Aeropuerto.query.filter(Aeropuerto.nombre.ilike(f"%{query}%")).all()

    # Obtener nombres de aeropuertos como sugerencias
    sugerencias = [aeropuerto.nombre for aeropuerto in sugerencias_base]

    return jsonify(sugerencias)

