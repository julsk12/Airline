# from common.Toke import *
from config.db import db, app, ma
from flask import (
    Flask,
    Blueprint,
    redirect,
    request,
    jsonify,
    json,
    session,
    render_template,
)
from datetime import datetime, timedelta
import random

from Model.Vuelos import Vuelo, FliesSchema
from Model.info_vuelo import Informacion, InfoSchema
from Model.Aerolineas import Aerolinea

routes_vuelos = Blueprint("routes_vuelos", __name__)

vuelo_schema = FliesSchema()
flies_Schema = FliesSchema(many=True)


@routes_vuelos.route("/vuelo", methods=["GET"])
def obtenervuelos():
    returnall = Vuelo.query.all()
    result_flies = flies_Schema.dump(returnall)
    return jsonify(result_flies)


# -------------------CRUD---------------------------------


@routes_vuelos.route("/eliminarvuelos/<id>", methods=["GET"])
def eliminarvuelos(id):
    fly = Vuelo.query.get(id)
    db.session.delete(fly)
    db.session.commit()
    return jsonify(vuelo_schema.dump(fly))


origen = ""
destino = ""
fecha_vuelta = ""
mascota = ""
# para tarifa S sumale 12%
# para tarifa M sumale 24%
# para tarifa L sumale 30.6%


@routes_vuelos.route("/crear_vuelos", methods=["POST"])
def crear_vuelos():
    global origen, destino, fecha_vuelta, mascota
    origen = request.form["origen"]
    destino = request.form["destino"]
    mascota = request.form["mascota"]
    fecha_vuelta = request.form["fecha_vuelta"]
    mascotas = ""

    resultado = (db.session.query(Informacion).filter(Informacion.origen == origen,Informacion.destino == destino,).all()
    )

    fecha_hora_actual = datetime.now()

    for i in range(6):
        if i < 2:
            if i == 1 and mascota == "si":
                fecha_hora_vuelo = fecha_hora_actual + timedelta(
                    days=i, hours=random.randint(0, 23)
                )
                mascotas = "si"
            else:
                fecha_hora_vuelo = fecha_hora_actual + timedelta(
                    days=i, hours=random.randint(0, 23)
                )
                mascotas = "no"
        else:
            fecha_hora_vuelo = fecha_hora_actual + timedelta(days=i)
            mascotas = "no"

        datos = {}
        idaN_total = 0
        vueltaN_total = 0
        duracion_total = 0
        numero_escalas = 0
        for vuelo in resultado:
            datos = {
                "origen": vuelo.origen,
                "origen_aeropuerto": vuelo.origen_aeropuerto,
                "escala1": vuelo.escala1,
                "escala1_aeropuerto": vuelo.escala1_aeropuerto,
                "escala2": vuelo.escala2,
                "escala2_aeropuerto": vuelo.escala2_aeropuerto,
                "destino": vuelo.destino,
                "destino_aeropuerto": vuelo.destino_aeropuerto,
                "numero_escalas": vuelo.numero_escalas,
                "duracion_total": vuelo.duracion_total,
                "idaN": vuelo.idaN,
                "vueltaN": vuelo.vueltaN,
                "idaF": vuelo.idaF,
                "vueltaF": vuelo.vueltaF,
                "solo_idaN": vuelo.solo_idaN,
                "solo_idaF": vuelo.solo_idaF,
                "tarifaS": vuelo.tarifaS,
                "RestriccionestarifaS": vuelo.RestriccionestarifaS,
                "tarifaM": vuelo.tarifaM,
                "RestriccionestarifaM": vuelo.RestriccionestarifaM,
                "tarifaL": vuelo.tarifaL,
                "RestriccionestarifaL": vuelo.RestriccionestarifaL,
            }
            duracion_total += datos["duracion_total"]
            numero_escalas += datos["numero_escalas"]
            idaN_total += datos["idaN"]
            vueltaN_total += datos["vueltaN"]

        precio = idaN_total + vueltaN_total
        fecha_salida = fecha_hora_vuelo
        duracion_total_horas = duracion_total

        duracion_total_timedelta = timedelta(hours=duracion_total_horas)

        fecha_llegada = fecha_salida + duracion_total_timedelta

        vuelo = Vuelo(
            id_aerolinea="avianca",
            ciudadOrigen=origen,
            ciudadDestino=destino,
            fechaHLlegada=fecha_llegada,
            fechaHSalida=fecha_hora_vuelo,
            mascotas=mascotas,
            duracionVuelo=duracion_total,
            asientosDisponibles="4",
            numeroEscalas=numero_escalas,
            precio=precio,
        )
        db.session.add(vuelo)

    db.session.commit()

    return jsonify({"message": "Se han creado 5 vuelos exitosamente"})


@routes_vuelos.route("/crear_vuelta", methods=["POST"])
def crear_regreso():
    origen
    destino
    fecha_vuelta
    mascota
    mascotas = ""

    resultado = (
        db.session.query(Informacion)
        .filter(
            Informacion.origen == origen,
            Informacion.destino == destino,
        )
        .all()
    )

    fecha_hora_actual = fecha_vuelta + timedelta(days=i, hours=random.randint(0, 23))

    for i in range(6):
        if i < 2:
            if i == 1 and mascota == "si":
                fecha_hora_vuelo = fecha_hora_actual + timedelta(
                    days=i, hours=random.randint(0, 23)
                )
                mascotas = "si"
            else:
                fecha_hora_vuelo = fecha_hora_actual + timedelta(
                    days=i, hours=random.randint(0, 23)
                )
                mascotas = "no"
        else:
            fecha_hora_vuelo = fecha_hora_actual + timedelta(days=i)
            mascotas = "no"

        datos = {}
        idaN_total = 0
        vueltaN_total = 0
        duracion_total = 0
        numero_escalas = 0
        for vuelo in resultado:
            datos = {
                "origen": vuelo.origen,
                "origen_aeropuerto": vuelo.origen_aeropuerto,
                "escala1": vuelo.escala1,
                "escala1_aeropuerto": vuelo.escala1_aeropuerto,
                "escala2": vuelo.escala2,
                "escala2_aeropuerto": vuelo.escala2_aeropuerto,
                "destino": vuelo.destino,
                "destino_aeropuerto": vuelo.destino_aeropuerto,
                "numero_escalas": vuelo.numero_escalas,
                "duracion_total": vuelo.duracion_total,
                "idaN": vuelo.idaN,
                "vueltaN": vuelo.vueltaN,
                "idaF": vuelo.idaF,
                "vueltaF": vuelo.vueltaF,
                "solo_idaN": vuelo.solo_idaN,
                "solo_idaF": vuelo.solo_idaF,
                "tarifaS": vuelo.tarifaS,
                "RestriccionestarifaS": vuelo.RestriccionestarifaS,
                "tarifaM": vuelo.tarifaM,
                "RestriccionestarifaM": vuelo.RestriccionestarifaM,
                "tarifaL": vuelo.tarifaL,
                "RestriccionestarifaL": vuelo.RestriccionestarifaL,
            }
            duracion_total += datos["duracion_total"]
            numero_escalas += datos["numero_escalas"]
            idaN_total += datos["idaN"]
            vueltaN_total += datos["vueltaN"]

        precio = idaN_total + vueltaN_total
        fecha_salida = fecha_hora_vuelo
        duracion_total_horas = duracion_total

        duracion_total_timedelta = timedelta(hours=duracion_total_horas)

        fecha_llegada = fecha_salida + duracion_total_timedelta

        # Crea un objeto Vuelo y guárdalo en la base de datos
        vuelo = Vuelo(
            id_aerolinea="avianca",
            ciudadOrigen=origen,
            ciudadDestino=destino,
            fechaHLlegada=fecha_llegada,
            fechaHSalida=fecha_hora_vuelo,
            mascotas=mascotas,
            duracionVuelo=duracion_total,
            asientosDisponibles="4",
            numeroEscalas=numero_escalas,
            precio=precio,
        )
        db.session.add(vuelo)

    db.session.commit()

    return jsonify({"message": "Se han creado 5 vuelos exitosamente"})


@routes_vuelos.route("/consulvuelos", methods=["GET"])
def consulvuelos():
    datos = {}
    resultado = (db.session.query(Vuelo, Aerolinea).select_from(Vuelo).join(Aerolinea).all())

    i = 0
    for vuelo, aerolinea in resultado:
        i += 1
        datos[i] = {
            "id": vuelo.id,
            "aerolinea": aerolinea.nombre,
            "origen": vuelo.ciudadOrigen,
            "destino": vuelo.ciudadDestino,
            "Fsalida": vuelo.fechaHSalida,
            "Fllegada": vuelo.fechaHLlegada,
            "asientosD": vuelo.asientosDisponibles,
            "precio": vuelo.precio,
            "#escalas": vuelo.numeroEscalas,
            "duracion": vuelo.duracionVuelo,
        }
        corigen = vuelo.ciudadOrigen
        cdestino = vuelo.ciudadDestino
        session['corigen'] = corigen
        session['cdestino'] = cdestino
    return jsonify(datos)


@routes_vuelos.route("/info_tarifa", methods=["GET"])
def info_tarifa():
    
    resultado = (db.session.query(Informacion).all()
    )
    print(resultado)
    datos = {}
    i=0
    for vuelo in resultado:
            print(vuelo.origen)
            print(vuelo.destino)
            i+= 1
            datos[i] = {
                'origen': vuelo.origen,
                'destino': vuelo.destino,
                'tarifaS': vuelo.tarifaS,
                'RestriccionestarifaS': vuelo.RestriccionestarifaS,
                'tarifaM': vuelo.tarifaM,
                'RestriccionestarifaM': vuelo.RestriccionestarifaM,
                'tarifaL': vuelo.tarifaL,
                'RestriccionestarifaL': vuelo.RestriccionestarifaL,
            }

    return jsonify(datos)