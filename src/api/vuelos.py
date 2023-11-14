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


@routes_vuelos.route("/actualizarvuelos", methods=["POST"])
def actualizarvuelos():
    id = request.json["id"]
    aerolinea = request.json["aerolinea"]
    ciudadOrigen = request.json["ciudadOrigen"]
    ciudadDestino = request.json["ciudadDestino"]
    fechaHSalida = request.json["fechaHSalida"]
    fechaHLlegada = request.json["fechaHLlegada"]
    asientosDisponibles = request.json["asientosDisponibles"]
    precio = request.json["precio"]
    tipoAvion = request.json["tipoAvion"]
    numeroEscalas = request.json["numeroEscalas"]
    duracionVuelo = request.json["duracionVuelo"]

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
    return redirect("/vuelo")


@routes_vuelos.route("/guardarvuelos", methods=["POST"])
def guardar_vuelos():
    fly = request.json[
        "aerolinea",
        "ciudadOrigen",
        "ciudadDestino",
        "fechaHSalida",
        "fechaHLlegada",
        "asientosDisponibles",
        "precio",
        "tipoAvion",
        "numeroEscalas",
        "duracionVuelo",
    ]
    new_vuelo = Vuelo(fly)
    db.session.add(new_vuelo)
    db.session.commit()
    return redirect("/vuelo")


# para tarifa S sumale 12%
# para tarifa M sumale 24%
# para tarifa L sumale 30.6%
# vuelos_nacionales = [
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Medellín, Colombia",
#         "destino_aeropuerto": "Aeropuerto Internacional José María Córdova (MDE), Medellín, Colombia",
#         "duracion_total": "1",
#         "idaN": "205.080",
#         "vueltaN": "155.500",
#         "idaF": "361.080",
#         "vueltaF": "227.555",
#         "solo_idaN": "205.080",
#         "solo_idaF": "361.080",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Cali, Colombia",
#         "destino_aeropuerto": "Aeropuerto Internacional Alfonso Bonilla Aragón (CLO), Cali, Colombia",
#         "duracion_total": "1",
#         "idaN": "186.605",
#         "vueltaN": "189.605",
#         "idaF": "269.385",
#         "vueltaF": "213.355",
#         "solo_idaN": "186.605",
#         "solo_idaF": "269.385",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Barranquilla, Colombia",
#         "destino_aeropuerto": "Aeropuerto Internacional Ernesto Cortissoz (BAQ), Barranquilla, Colombia",
#         "duracion_total": "1",
#         "idaN": "220.670",
#         "vueltaN": "231.770",
#         "idaF": "197.555",
#         "vueltaF": "197.555",
#         "solo_idaN": "176.555",
#         "solo_idaF": "197.555",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Pereira, Colombia",
#         "destino_aeropuerto": "Aeropuerto Internacional Matecaña (PEI), Pereira, Colombia",
#         "duracion_total": "1",
#         "idaN": "176.555",
#         "vueltaN": "176.555",
#         "idaF": "197.555",
#         "vueltaF": "197.555",
#         "solo_idaN": "176.555",
#         "solo_idaF": "197.555",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Cúcuta, Colombia",
#         "destino_aeropuerto": "Aeropuerto Internacional Camilo Daza (CUC), Cúcuta, Colombia",
#         "duracion_total": "1",
#         "idaN": "317.580",
#         "vueltaN": "334.580",
#         "idaF": "491.420",
#         "vueltaF": "304.580",
#         "solo_idaN": "317.580",
#         "solo_idaF": "410.600",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Santa Marta, Colombia",
#         "destino_aeropuerto": "Aeropuerto Internacional Simón Bolívar (SMR), Santa Marta, Colombia",
#         "duracion_total": "1",
#         "idaN": "317.580",
#         "vueltaN": "334.580",
#         "idaF": "491.420",
#         "vueltaF": "304.580",
#         "solo_idaN": "317.580",
#         "solo_idaF": "410.600",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Pasto, Colombia",
#         "destino_aeropuerto": "Aeropuerto Antonio Nariño (PSO), Pasto, Colombia",
#         "duracion_total": "1",
#         "idaN": "213.060",
#         "vueltaN": "219.480",
#         "idaF": "315.580",
#         "vueltaF": "324.580",
#         "solo_idaN": "213.060",
#         "solo_idaF": "309.330",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Leticia, Colombia",
#         "destino_aeropuerto": "Aeropuerto Alfredo Vásquez Cobo (LET), Leticia, Colombia",
#         "duracion_total": "2",
#         "idaN": "289.700",
#         "vueltaN": "290.480",
#         "idaF": "489.700",
#         "vueltaF": "324.580",
#         "solo_idaN": "289.700",
#         "solo_idaF": "290.900",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
# ]
# vuelos_directos = [
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Miami, EE. UU.",
#         "destino-aeropuerto": "Aeropuerto Internacional de Miami (MIA), Miami, EE. UU.",
#         "duracion_total": "4 horas",
#         "idaN": "1.084.590",
#         "vueltaN": "831.770",
#         "idaF": "1.584.590",
#         "vueltaF": "999.555",
#         "solo_idaN": "1.084.590",
#         "solo_idaF": "1.584.590",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Madrid, España",
#         "destino_aeropuerto": "Aeropuerto Adolfo Suárez Madrid-Barajas (MAD), Madrid, España",
#         "duracion_total": "10 horas",
#         "idaN": "2.290.170",
#         "vueltaN": "1.451.770",
#         "idaF": "2.662.290",
#         "vueltaF": "1.551.770",
#         "solo_idaN": "2.290.170",
#         "solo_idaF": "2.662.290",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Nueva York, EE. UU.",
#         "destino-aeropuerto": "Aeropuerto Internacional John F. Kennedy (JFK), Nueva York, EE. UU.",
#         "duracion_total": "6 horas",
#         "idaN": "1.128.565",
#         "vueltaN": "1.390.050",
#         "idaF": "1.662.290",
#         "vueltaF": "1.551.770",
#         "solo_idaN": "1.128.565",
#         "solo_idaF": "1.662.290",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Sao Paulo, Brasil",
#         "destino_aeropuerto": "Aeropuerto Internacional de Guarulhos (GRU), Sao Paulo, Brasil",
#         "duracion_total": "8 horas",
#         "idaN": "1.979.785",
#         "vueltaN": "1.479.275",
#         "idaF": "2.345.995",
#         "vueltaF": "2.418.565",
#         "solo_idaN": "1.979.785",
#         "solo_idaF": "2.345.995",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Ciudad de México, México",
#         "destino_aeropuerto": "Aeropuerto Internacional de la Ciudad de México (MEX), Ciudad de México, México",
#         "duracion_total": "5 horas",
#         "idaN": "1.858.445",
#         "vueltaN": "1.390.050",
#         "idaF": "2.162.290",
#         "vueltaF": "1.551.770",
#         "solo_idaN": "1.128.565",
#         "solo_idaF": "1.662.290",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "París, Francia",
#         "destino_aeropuerto": "Aeropuerto Charles de Gaulle (CDG), París, Francia",
#         "duracion_total": "11 horas",
#         "idaN": "2.855.615",
#         "vueltaN": "2.159.445",
#         "idaF": "8.153.660",
#         "vueltaF": "7.551.770",
#         "solo_idaN": "2.855.615",
#         "solo_idaF": "8.153.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Buenos Aires, Argentina",
#         "destino_aeropuerto": "Aeropuerto Internacional Ministro Pistarini (EZE), Buenos Aires, Argentina",
#         "duracion_total": "9 horas",
#         "idaN": "1.755.615",
#         "vueltaN": "1.438.455",
#         "idaF": "2.126.660",
#         "vueltaF": "1.755.615",
#         "solo_idaN": "1.755.615",
#         "solo_idaF": "2.126.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Lima, Perú",
#         "destino_aeropuerto": "Aeropuerto Internacional Jorge Chávez (LIM), Lima, Perú",
#         "duracion_total": "6 horas",
#         "idaN": "2.855.615",
#         "vueltaN": "2.159.445",
#         "idaF": "8.153.660",
#         "vueltaF": "7.551.770",
#         "solo_idaN": "2.855.615",
#         "solo_idaF": "8.153.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Roma, Italia",
#         "destino_aeropuerto": "Aeropuerto de Roma-Fiumicino (FCO), Roma, Italia",
#         "duracion_total": "12 horas",
#         "idaN": "2.951.670",
#         "vueltaN": "2.159.445",
#         "idaF": "8.232.110",
#         "vueltaF": "7.551.770",
#         "solo_idaN": "2.951.670",
#         "solo_idaF": "8.232.110",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "destino": "Toronto, Canadá",
#         "destino_aeropuerto": "Aeropuerto Internacional Toronto Pearson (YYZ), Toronto, Canadá",
#         "duracion_total": "8 horas",
#         "idaN": "1.503.525",
#         "vueltaN": "1.029.930",
#         "idaF": "1.709.660",
#         "vueltaF": "1.551.770",
#         "solo_idaN": "1.503.525",
#         "solo_idaF": "1.709.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
# ]
# vuelos_dos_escalas = [
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "Londres, Reino Unido",
#         "escala1_aeropuerto": "Aeropuerto Heathrow de Londres (LHR), Londres, Reino Unido",
#         "escala2": "París, Francia",
#         "escala2_aeropuerto": "Aeropuerto Charles de Gaulle (CDG), París, Francia",
#         "destino": "Sídney, Australia",
#         "destino_aeropuerto": "Aeropuerto Kingsford Smith de Sídney (SYD), Sídney, Australia",
#         "duracion_total": "26",
#         "idaN": "5.855.615",
#         "vueltaN": "4.159.445",
#         "idaF": "8.153.660",
#         "vueltaF": "7.551.770",
#         "solo_idaN": "5.855.615",
#         "solo_idaF": "8.153.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "Miami, EE. UU.",
#         "escala1_aeropuerto": "Aeropuerto Internacional de Miami (MIA), Miami, EE. UU.",
#         "escala2": "Madrid, España",
#         "escala2_aeropuerto": "Aeropuerto Adolfo Suárez Madrid-Barajas (MAD), Madrid, España",
#         "destino": "Melbourne, Australia",
#         "destino_aeropuerto": "Aeropuerto de Brisbane (BNE), Brisbane, Australia",
#         "duracion_total": "30",
#         "idaN": "6.855.615",
#         "vueltaN": "4.159.445",
#         "idaF": "8.153.660",
#         "vueltaF": "6.551.770",
#         "solo_idaN": "5.855.615",
#         "solo_idaF": "8.153.660",
#         "tarifaS": "- 1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "- 1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "- 1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "Lima, Perú",
#         "escala1_aeropuerto": "Aeropuerto Internacional Jorge Chávez (LIM), Lima, Perú",
#         "escala2": "Los Ángeles, EE. UU.",
#         "escala2_aeropuerto": "Aeropuerto Internacional de Los Ángeles (LAX), Los Ángeles, EE. UU.",
#         "destino": "Nueva Delhi, India",
#         "destino_aeropuerto": "Aeropuerto Internacional Indira Gandhi (DEL), Nueva Delhi, India",
#         "duracion_total": "28",
#         "idaN": "7.255.445",
#         "vueltaN": "7.055.335",
#         "idaF": "8.153.660",
#         "vueltaF": "7.551.770",
#         "solo_idaN": "7.255.445",
#         "solo_idaF": "8.153.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "Miami, EE. UU.",
#         "escala1_aeropuerto": "Aeropuerto Internacional de Miami (MIA), Miami, EE. UU.",
#         "escala2": "Atlanta, EE. UU.",
#         "escala2_aeropuerto": "Aeropuerto Internacional Hartsfield-Jackson (ATL), Atlanta, EE. UU.",
#         "destino": "Nueva Orleans, EE. UU.",
#         "destino_aeropuerto": "Aeropuerto Internacional Louis Armstrong (MSY), Nueva Orleans, EE. UU.",
#         "duracion_total": "16",
#         "idaN": "5.855.615",
#         "vueltaN": "4.159.445",
#         "idaF": "8.153.660",
#         "vueltaF": "7.551.770",
#         "solo_idaN": "5.855.615",
#         "solo_idaF": "8.153.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "Caracas, Venezuela",
#         "escala1_aeropuerto": "Aeropuerto Internacional Simón Bolívar (CCS), Caracas, Venezuela",
#         "escala2": "San Juan, Puerto Rico",
#         "escala2_aeropuerto": "Aeropuerto Internacional Luis Muñoz Marín (SJU), San Juan, Puerto Rico",
#         "destino": "La Habana, Cuba",
#         "destino_aeropuerto": "Aeropuerto Internacional José Martí (HAV), La Habana, Cuba",
#         "duracion_total": "14",
#         "idaN": "3.205.615",
#         "vueltaN": "2.159.445",
#         "idaF": "5.153.660",
#         "vueltaF": "4.551.770",
#         "solo_idaN": "3.205.615",
#         "solo_idaF": "5.153.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "Buenos Aires, Argentina",
#         "escala1_aeropuerto": "Aeropuerto Internacional Ministro Pistarini (EZE), Buenos Aires, Argentina",
#         "escala2": "Lisboa, Portugal",
#         "escala2_aeropuerto": "Aeropuerto Humberto Delgado (LIS), Lisboa, Portugal",
#         "destino": "Moscú, Rusia",
#         "destino_aeropuerto": "Aeropuerto Internacional de Sheremétievo (SVO), Moscú, Rusia",
#         "duracion_total": "28",
#         "idaN": "8.855.615",
#         "vueltaN": "8.159.445",
#         "idaF": "9.153.660",
#         "vueltaF": "9.551.770",
#         "solo_idaN": "8.855.615",
#         "solo_idaF": "9.153.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "Londres, Reino Unido",
#         "escala1_aeropuerto": "Aeropuerto Heathrow de Londres (LHR), Londres, Reino Unido",
#         "escala2": "París, Francia",
#         "escala2_aeropuerto": "Aeropuerto Charles de Gaulle (CDG), París, Francia",
#         "destino": "Roma, Italia",
#         "destino_aeropuerto": "Aeropuerto Leonardo da Vinci-Fiumicino (FCO), Roma, Italia",
#         "duracion_total": "26",
#         "idaN": "4.240.595",
#         "vueltaN": "3.240.445",
#         "idaF": "9.134.660",
#         "vueltaF": "8.551.770",
#         "solo_idaN": "4.240.595",
#         "solo_idaF": "9.134.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "escala1": "Los Ángeles, EE. UU.",
#         "escala1_aeropuerto": "Aeropuerto Internacional de Los Ángeles (LAX), Los Ángeles, EE. UU.",
#         "escala2": "Tokio, Japón",
#         "escala2_aeropuerto": "Aeropuerto Internacional de Narita (NRT), Tokio, Japón",
#         "destino": "Pekín, China",
#         "destino_aeropuerto": "Aeropuerto Internacional de Pekín-Capital (PEK), Pekín, China",
#         "duracion_total": "32",
#         "idaN": "4.240.595",
#         "vueltaN": "3.240.445",
#         "idaF": "9.134.660",
#         "vueltaF": "8.551.770",
#         "solo_idaN": "4.240.595",
#         "solo_idaF": "9.134.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
#     {
#         "origen": "Bogotá, Colombia",
#         "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
#         "escala1": "San Francisco, EE. UU.",
#         "escala1_aeropuerto": "Aeropuerto Internacional de San Francisco (SFO), San Francisco, EE. UU.",
#         "escala2": "Toronto, Canadá",
#         "escala2_aeropuerto": "Aeropuerto Internacional de Toronto Pearson (YYZ), Toronto, Canadá",
#         "destino": "Londres, Reino Unido",
#         "destino_aeropuerto": "Aeropuerto Heathrow de Londres (LHR), Londres, Reino Unido",
#         "duracion_total": "26",
#         "idaN": "3.589.415",
#         "vueltaN": "3.589.415",
#         "idaF": "6.134.660",
#         "vueltaF": "6.551.770",
#         "solo_idaN": "6.134.660",
#         "solo_idaF": "9.134.660",
#         "tarifaS": "-1 equipaje de mano(10kg) + bolso - Acumula 3LM por cada USD",
#         "RestriccionestarifaS": "- Equipaje de bodega(23 kg) - Check-in en aeropuerto (Servicio con cargo adicional) - Asiento Economy (Servicio con cargo adicional) - Seleccion de asientos (Servicio con cargo adicional) - Cambios de vuelo (Servicio con cargo adicional) - Abordaje prioritario (Servicio con cargo adicional)",
#         "tarifaM": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Economy",
#         "RestriccionestarifaM": "- Cambios de vuelo (Servicio con cargo adicional antes del vuelo) - Abordaje prioritario (Compralo al hacer check-in)",
#         "tarifaL": "-1 equipaje de mano(10kg) + bolso - Acumula LifeMiles - 1 Equipaje de bodega(23 kg) - Check-in gratis en aeropuerto - Asiento Plus - Cambios de vuelo - Reembolso",
#         "RestriccionestarifaL": "- Abordaje prioritario (Servicio con cargo adicional)",
#     },
# ]


@routes_vuelos.route("/crear_vuelos", methods=["POST"])
def crear_vuelos():
    # Obtener los datos del formulario
    origen = request.form["origen"]
    destino = request.form["destino"]

    resultado = db.session.query(Informacion).filter(
        Informacion.origen == origen,
        Informacion.destino == destino,
    ).all()

    fecha_hora_actual = datetime.now()

    for i in range(5):
        if i < 2:
            fecha_hora_vuelo = fecha_hora_actual + timedelta(
                days=i, hours=random.randint(0, 23)
            )
        else:
            fecha_hora_vuelo = fecha_hora_actual + timedelta(days=i)

        datos = {}
        idaN_total = 0  
        vueltaN_total = 0
        duracion_total = 0
        numero_escalas = 0
        for vuelo in resultado:
            datos = {
                'origen': vuelo.origen,
                'origen_aeropuerto': vuelo.origen_aeropuerto,
                'escala1': vuelo.escala1,
                'escala1_aeropuerto': vuelo.escala1_aeropuerto,
                'escala2': vuelo.escala2,
                'escala2_aeropuerto': vuelo.escala2_aeropuerto,
                'destino': vuelo.destino,
                'destino_aeropuerto': vuelo.destino_aeropuerto,
                'numero_escalas': vuelo.numero_escalas,
                'duracion_total': vuelo.duracion_total,
                'idaN': vuelo.idaN,
                'vueltaN': vuelo.vueltaN,
                'idaF': vuelo.idaF,
                'vueltaF': vuelo.vueltaF,
                'solo_idaN': vuelo.solo_idaN,
                'solo_idaF': vuelo.solo_idaF,
                'tarifaS': vuelo.tarifaS,
                'RestriccionestarifaS': vuelo.RestriccionestarifaS,
                'tarifaM': vuelo.tarifaM,
                'RestriccionestarifaM': vuelo.RestriccionestarifaM,
                'tarifaL': vuelo.tarifaL,
                'RestriccionestarifaL': vuelo.RestriccionestarifaL,
            }
            duracion_total += datos['duracion_total']
            numero_escalas += datos['numero_escalas']
            idaN_total += datos['idaN']
            vueltaN_total += datos['vueltaN']

        print(idaN_total, "numero 1", duracion_total)
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
            duracionVuelo=duracion_total,
            asientosDisponibles="4",
            fechaHLlegada=fecha_llegada,
            fechaHSalida=fecha_hora_vuelo,
            numeroEscalas=numero_escalas,
            precio=precio,
        )
        db.session.add(vuelo)

    db.session.commit()

    return jsonify({"message": "Se han creado 5 vuelos exitosamente"})


# consultar los vuelos guardados en la tabla


@routes_vuelos.route("/consulvuelos", methods=["GET"])
def consulvuelos():
    datos = {}
    vuelos_table = db.Model.metadata.tables["tblvuelos"]
    aerolinia_table = db.Model.metadata.tables["tblaerolinea"]
    resultado = (
        db.session.query(Vuelo, Aerolinea)
        .select_from(vuelos_table)
        .join(aerolinia_table)
        .all()
    )
    
    i = 0
    for Vuelo, Aerolinea in resultado:
        i += 1
        datos[i] = {
            "id": Vuelo.id,
            "aerolinea": Aerolinea.nombre,
            "origen": Vuelo.ciudadOrigen,
            "destino": Vuelo.ciudadDestino,
            "Fsalida": Vuelo.fechaHSalida,
            "Fllegada": Vuelo.fechaHLlegada,
            "asientosD": Vuelo.asientosDisponibles,
            "precio": Vuelo.precio,
            "#escalas": Vuelo.numeroEscalas,
            "duracion": Vuelo.duracionVuelo,
        }
    return jsonify(datos)
