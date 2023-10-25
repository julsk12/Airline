# from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from datetime import datetime, timedelta
import random

from Model.Vuelos import Vuelo, FliesSchema

routes_vuelos = Blueprint("routes_vuelos",  __name__)

vuelo_schema = FliesSchema()
flies_Schema = FliesSchema(many=True)


@routes_vuelos.route('/vuelo', methods=['GET'])
def obtenervuelos():
    returnall = Vuelo.query.all()
    result_flies = flies_Schema.dump(returnall)
    return jsonify(result_flies)

# -------------------CRUD---------------------------------


@routes_vuelos.route('/eliminarvuelos/<id>', methods=['GET'])
def eliminarvuelos(id):
    fly = Vuelo.query.get(id)
    db.session.delete(fly)
    db.session.commit()
    return jsonify(vuelo_schema.dump(fly))


@routes_vuelos.route('/actualizarvuelos', methods=['POST'])
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


@routes_vuelos.route('/guardarvuelos', methods=['POST'])
def guardar_vuelos():
    fly = request.json['aerolinea', 'ciudadOrigen', 'ciudadDestino', 'fechaHSalida',
                       'fechaHLlegada', 'asientosDisponibles', 'precio', 'tipoAvion', 'numeroEscalas', 'duracionVuelo']
    new_vuelo = Vuelo(fly)
    db.session.add(new_vuelo)
    db.session.commit()
    return redirect('/vuelo')


vuelos_nacionales = [
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Medellín, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional José María Córdova (MDE), Medellín, Colombia",
        "duracion_total": "1 hora",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Cali, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Alfonso Bonilla Aragón (CLO), Cali, Colombia",
        "duracion_total": "1 hora",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Barranquilla, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Ernesto Cortissoz (BAQ), Barranquilla, Colombia",
        "duracion_total": "1 hora",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Pereira, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Matecaña (PEI), Pereira, Colombia",
        "duracion_total": "1 hora",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Cúcuta, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Camilo Daza (CUC), Cúcuta, Colombia",
        "duracion_total": "1 hora",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Santa Marta, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Simón Bolívar (SMR), Santa Marta, Colombia",
        "duracion_total": "1 hora",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Pasto, Colombia",
        "destino_aeropuerto": "Aeropuerto Antonio Nariño (PSO), Pasto, Colombia",
        "duracion_total": "1 hora",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Leticia, Colombia",
        "destino_aeropuerto": "Aeropuerto Alfredo Vásquez Cobo (LET), Leticia, Colombia",
        "duracion_total": "2 horas",
    },
]


@routes_vuelos.route('/crear_vuelos', methods=['POST'])
def crear_vuelos():
    # Obtener los datos del formulario
    origen = request.form['origen']
    destino = request.form['destino']

    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Crear 5 vuelos
    for i in range(5):
        # Calcular la fecha del vuelo (puede ser el mismo día o días después)
        fecha_vuelo = fecha_actual + timedelta(days=i)

        # Generar una hora de salida aleatoria en formato "HH:MM"
        hora_salida = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"

        # Crear un diccionario para representar el vuelo
        vuelo = Vuelo(id_aerolinea="1", ciudadOrigen=origen, ciudadDestino=destino, duracionVuelo="2", asientosDisponibles="4",
                      fechaHLlegada="2023-10-30 00:00", fechaHSalida=hora_salida, numeroEscalas="0", precio="4000000", tipoAvion="RXD112")
        db.session.add(vuelo)
    db.session.commit()
       # Vuelo.append(vuelo)

    return jsonify({'message': 'Se han creado 5 vuelos exitosamente'})
