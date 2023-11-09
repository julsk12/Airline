# from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from datetime import datetime, timedelta
import random

from Model.Vuelos import Vuelo, FliesSchema
from Model.Aerolineas import Aerolinea

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


# para tarifa S sumale 60
# para tarifa M sumale 100
# para tarifa L sumale 140
vuelos_nacionales = [
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Medellín, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional José María Córdova (MDE), Medellín, Colombia",
        "duracion_total": "1",
        "idaN": "205.080",
        "vueltaN": "155.500",
        "idaF": "361.080",
        "vueltaF": "227.555",
        "solo_idaN": "205.080",
        "solo_idaF": "361.080",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Cali, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Alfonso Bonilla Aragón (CLO), Cali, Colombia",
        "duracion_total": "1",
        "idaN": "186.605",
        "vueltaN": "189.605",
        "idaF": "269.385",
        "vueltaF": "213.355",
        "solo_idaN": "186.605",
        "solo_idaF": "269.385",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Barranquilla, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Ernesto Cortissoz (BAQ), Barranquilla, Colombia",
        "duracion_total": "1",
        "idaN": "220.670",
        "vueltaN": "231.770",
        "idaF": "197.555",
        "vueltaF": "197.555",
        "solo_idaN": "176.555",
        "solo_idaF": "197.555",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Pereira, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Matecaña (PEI), Pereira, Colombia",
        "duracion_total": "1",
        "idaN": "176.555",
        "vueltaN": "176.555",
        "idaF": "197.555",
        "vueltaF": "197.555",
        "solo_idaN": "176.555",
        "solo_idaF": "197.555",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Cúcuta, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Camilo Daza (CUC), Cúcuta, Colombia",
        "duracion_total": "1",
        "idaN": "317.580",
        "vueltaN": "334.580",
        "idaF": "491.420",
        "vueltaF": "304.580",
        "solo_idaN": "317.580",
        "solo_idaF": "410.600",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Santa Marta, Colombia",
        "destino_aeropuerto": "Aeropuerto Internacional Simón Bolívar (SMR), Santa Marta, Colombia",
        "duracion_total": "1",
        "idaN": "317.580",
        "vueltaN": "334.580",
        "idaF": "491.420",
        "vueltaF": "304.580",
        "solo_idaN": "317.580",
        "solo_idaF": "410.600",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Pasto, Colombia",
        "destino_aeropuerto": "Aeropuerto Antonio Nariño (PSO), Pasto, Colombia",
        "duracion_total": "1",
        "idaN": "213.060",
        "vueltaN": "219.480",
        "idaF": "315.580",
        "vueltaF": "324.580",
        "solo_idaN": "213.060",
        "solo_idaF": "309.330",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Leticia, Colombia",
        "destino_aeropuerto": "Aeropuerto Alfredo Vásquez Cobo (LET), Leticia, Colombia",
        "duracion_total": "2",
        "idaN": "289.700",
        "vueltaN": "290.480",
        "idaF": "489.700",
        "vueltaF": "324.580",
        "solo_idaN": "289.700",
        "solo_idaF": "290.900",
    },
]
vuelos_directos = [
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Miami, EE. UU.",
        "destino-aeropuerto": "Aeropuerto Internacional de Miami (MIA), Miami, EE. UU.",
        "duracion_total": "4 horas",
        "idaN": "1.084.590",
        "vueltaN": "831.770", 
        "idaF": "197.555",
        "vueltaF": "197.555",
        "solo_idaN": "176.555",
        "solo_idaF": "197.555",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Madrid, España",
        "destino_aeropuerto": "Aeropuerto Adolfo Suárez Madrid-Barajas (MAD), Madrid, España",
        "duracion_total": "10 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Nueva York, EE. UU.",
        "destino-aeropuerto": "Aeropuerto Internacional John F. Kennedy (JFK), Nueva York, EE. UU.",
        "duracion_total": "6 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Sao Paulo, Brasil",
        "destino_aeropuerto": "Aeropuerto Internacional de Guarulhos (GRU), Sao Paulo, Brasil",
        "duracion_total": "8 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Ciudad de México, México",
        "destino_aeropuerto": "Aeropuerto Internacional de la Ciudad de México (MEX), Ciudad de México, México",
        "duracion_total": "5 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "París, Francia",
        "destino_aeropuerto": "Aeropuerto Charles de Gaulle (CDG), París, Francia",
        "duracion_total": "11 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Buenos Aires, Argentina",
        "destino_aeropuerto": "Aeropuerto Internacional Ministro Pistarini (EZE), Buenos Aires, Argentina",
        "duracion_total": "9 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Lima, Perú",
        "destino_aeropuerto": "Aeropuerto Internacional Jorge Chávez (LIM), Lima, Perú",
        "duracion_total": "6 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Roma, Italia",
        "destino_aeropuerto": "Aeropuerto de Roma-Fiumicino (FCO), Roma, Italia",
        "duracion_total": "12 horas",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "destino": "Toronto, Canadá",
        "destino_aeropuerto": "Aeropuerto Internacional Toronto Pearson (YYZ), Toronto, Canadá",
        "duracion_total": "8 horas",
    },
]
vuelos_dos_escalas = [
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "Londres, Reino Unido",
        "escala1_aeropuerto": "Aeropuerto Heathrow de Londres (LHR), Londres, Reino Unido",
        "escala2": "París, Francia",
        "escala2_aeropuerto": "Aeropuerto Charles de Gaulle (CDG), París, Francia",
        "destino": "Sídney, Australia",
        "destino_aeropuerto": "Aeropuerto Kingsford Smith de Sídney (SYD), Sídney, Australia",
        "duracion_total": "26",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "Miami, EE. UU.",
        "escala1_aeropuerto": "Aeropuerto Internacional de Miami (MIA), Miami, EE. UU.",
        "escala2": "Madrid, España",
        "escala2_aeropuerto": "Aeropuerto Adolfo Suárez Madrid-Barajas (MAD), Madrid, España",
        "destino": "Brisbane, Australia",
        "destino_aeropuerto": "Aeropuerto de Brisbane (BNE), Brisbane, Australia",
        "duracion_total": "30",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "Lima, Perú",
        "escala1_aeropuerto": "Aeropuerto Internacional Jorge Chávez (LIM), Lima, Perú",
        "escala2": "Los Ángeles, EE. UU.",
        "escala2_aeropuerto": "Aeropuerto Internacional de Los Ángeles (LAX), Los Ángeles, EE. UU.",
        "destino": "Nueva Delhi, India",
        "destino_aeropuerto": "Aeropuerto Internacional Indira Gandhi (DEL), Nueva Delhi, India",
        "duracion_total": "28",
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "Miami, EE. UU.",
        "escala1_aeropuerto": "Aeropuerto Internacional de Miami (MIA), Miami, EE. UU.",
        "escala2": "Atlanta, EE. UU.",
        "escala2_aeropuerto": "Aeropuerto Internacional Hartsfield-Jackson (ATL), Atlanta, EE. UU.",
        "destino": "Nueva Orleans, EE. UU.",
        "destino_aeropuerto": "Aeropuerto Internacional Louis Armstrong (MSY), Nueva Orleans, EE. UU.",
        "duracion_total": "16"
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "Caracas, Venezuela",
        "escala1_aeropuerto": "Aeropuerto Internacional Simón Bolívar (CCS), Caracas, Venezuela",
        "escala2": "San Juan, Puerto Rico",
        "escala2_aeropuerto": "Aeropuerto Internacional Luis Muñoz Marín (SJU), San Juan, Puerto Rico",
        "destino": "La Habana, Cuba",
        "destino_aeropuerto": "Aeropuerto Internacional José Martí (HAV), La Habana, Cuba",
        "duracion_total": "14"
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "Buenos Aires, Argentina",
        "escala1_aeropuerto": "Aeropuerto Internacional Ministro Pistarini (EZE), Buenos Aires, Argentina",
        "escala2": "Lisboa, Portugal",
        "escala2_aeropuerto": "Aeropuerto Humberto Delgado (LIS), Lisboa, Portugal",
        "destino": "Moscú, Rusia",
        "destino_aeropuerto": "Aeropuerto Internacional de Sheremétievo (SVO), Moscú, Rusia",
        "duracion_total": "28"
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "Londres, Reino Unido",
        "escala1_aeropuerto": "Aeropuerto Heathrow de Londres (LHR), Londres, Reino Unido",
        "escala2": "París, Francia",
        "escala2_aeropuerto": "Aeropuerto Charles de Gaulle (CDG), París, Francia",
        "destino": "Roma, Italia",
        "destino_aeropuerto": "Aeropuerto Leonardo da Vinci-Fiumicino (FCO), Roma, Italia",
        "duracion_total": "26"
    },
    {
        "origen": "Bogotá, Colombia",
        "escala1": "Los Ángeles, EE. UU.",
        "escala1_aeropuerto": "Aeropuerto Internacional de Los Ángeles (LAX), Los Ángeles, EE. UU.",
        "escala2": "Tokio, Japón",
        "escala2_aeropuerto": "Aeropuerto Internacional de Narita (NRT), Tokio, Japón",
        "destino": "Pekín, China",
        "destino_aeropuerto": "Aeropuerto Internacional de Pekín-Capital (PEK), Pekín, China",
        "duracion_total": "32"
    },
    {
        "origen": "Bogotá, Colombia",
        "origen_aeropuerto": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "escala1": "San Francisco, EE. UU.",
        "escala1_aeropuerto": "Aeropuerto Internacional de San Francisco (SFO), San Francisco, EE. UU.",
        "escala2": "Toronto, Canadá",
        "escala2_aeropuerto": "Aeropuerto Internacional de Toronto Pearson (YYZ), Toronto, Canadá",
        "destino": "Londres, Reino Unido",
        "destino_aeropuerto": "Aeropuerto Heathrow de Londres (LHR), Londres, Reino Unido",
        "duracion_total": "26"
    }
]


@routes_vuelos.route('/crear_vuelos', methods=['POST'])
def crear_vuelos():
    # Obtener los datos del formulario
    origen = request.form['origen']
    destino = request.form['destino']

    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()

    # Crear 5 vuelos y guardarlos en la base de datos
    for i in range(5):
        # Calcular la fecha y hora del vuelo
        if i < 2:
            fecha_hora_vuelo = fecha_hora_actual + \
                timedelta(days=i, hours=random.randint(0, 23))
        else:
            fecha_hora_vuelo = fecha_hora_actual + timedelta(days=i)

        duracion_total = "2"
        numero_escalas = 0

        # Verificar si los datos de origen y destino están contenidos en vuelos_nacionales
        for vuelo in vuelos_nacionales:
            if origen == vuelo['origen'] and destino == vuelo['destino']:
                duracion_total = vuelo['duracion_total']
                numero_escalas = 0
                break

        # Verificar si los datos de origen y destino están contenidos en vuelos_directos
        for vuelo in vuelos_directos:
            if origen == vuelo['origen'] and destino == vuelo['destino']:
                duracion_total = vuelo['duracion_total']
                numero_escalas = 0
                break

        # Verificar si los datos de origen y destino están contenidos en vuelos_dos_escalas
        for vuelo in vuelos_dos_escalas:
            if origen == vuelo['origen'] and destino == vuelo['destino']:
                duracion_total = vuelo['duracion_total']
                numero_escalas = 2
                break

        fecha_salida = fecha_hora_vuelo
        duracion_total_horas = int(duracion_total)

        duracion_total_timedelta = timedelta(hours=duracion_total_horas)

        fecha_llegada = fecha_salida + duracion_total_timedelta

        # Crea un objeto Vuelo y guárdalo en la base de datos
        vuelo = Vuelo(id_aerolinea="avianca", ciudadOrigen=origen, ciudadDestino=destino, duracionVuelo=duracion_total, asientosDisponibles="4",
                      fechaHLlegada=fecha_llegada, fechaHSalida=fecha_hora_vuelo, numeroEscalas=numero_escalas, precio="4000000")
        db.session.add(vuelo)

    db.session.commit()

    return jsonify({'message': 'Se han creado 5 vuelos exitosamente'})

# consultar los vuelos guardados en la tabla


@routes_vuelos.route('/consulvuelos', methods=['GET'])
def consulvuelos():
    datos = {}
    vuelos_table = db.Model.metadata.tables['tblvuelos']
    aerolinia_table = db.Model.metadata.tables['tblaerolinea']
    resultado = db.session.query(Vuelo, Aerolinea).select_from(
        vuelos_table).join(aerolinia_table).all()
    i = 0
    for Vuelo, Aerolinea in resultado:
        i += 1
        datos[i] = {
            'id': Vuelo.id,
            'aerolinea': Aerolinea.nombre,
            'origen': Vuelo.ciudadOrigen,
            'destino': Vuelo.ciudadDestino,
            'Fsalida': Vuelo.fechaHSalida,
            'Fllegada': Vuelo.fechaHLlegada,
            'asientosD': Vuelo.asientosDisponibles,
            'precio': Vuelo.precio,
            '#escalas': Vuelo.numeroEscalas,
            'duracion': Vuelo.duracionVuelo
        }
    return jsonify(datos)
