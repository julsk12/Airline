#from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from datetime import datetime
from Model.Reservas import Reserva, ReseSchema
from Model.Vuelos import Vuelo, FliesSchema
from Model.Usuarios import Users, UsuariosSchema



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
    id = request.form['id']
    id_usuario = request.form['id_usuario']
    id_vuelo = request.form['id_vuelo']
    estadoreserva = request.form['estadoreserva']
    asientosReservados = request.form['asientosReservados']
    fechaReserva = request.form['fechaReserva']

    areser = Reserva.query.get(id)
    areser.Reserva = id_usuario
    areser.Reserva = id_vuelo
    areser.Reserva = estadoreserva
    areser.Reserva = asientosReservados
    areser.Reserva = fechaReserva

    db.session.commit()
    return redirect('/reserva')
id_vuelo=0
@routes_reserva.route('/guardarglobales', methods=['POST'] )
def guardar_globe():
    global id_vuelo
    origen = request.form["origen"]
    destino = request.form["destino"]
    fecha_salida_str = request.form["fechaSalida"]
    fecha_llegada_str = request.form["fechaLlegada"]

    # Parsear las fechas
    fecha_salida_obj = datetime.strptime(fecha_salida_str, '%a, %d %b %Y %H:%M:%S GMT')
    fecha_llegada_obj = datetime.strptime(fecha_llegada_str, '%a, %d %b %Y %H:%M:%S GMT')
    print(origen, destino, fecha_salida_obj, fecha_llegada_obj)
    consulta = Vuelo.query.filter(
    Vuelo.fechaHSalida.between(fecha_salida_str, fecha_llegada_obj),
    Vuelo.fechaHLlegada.between(fecha_salida_str, fecha_llegada_obj),
    Vuelo.ciudadOrigen == origen,
    Vuelo.ciudadDestino == destino).all()
    block={}
    trry = []
    for lie in consulta:    
        block= {
            'id': lie.id,
            'id_aerolinea': lie.id_aerolinea,
            'ciudadOrigen': lie.ciudadOrigen,
            'ciudadDestino': lie.ciudadDestino,
            'fechaHSalida': lie.fechaHSalida,
            'fechaHLlegada': lie.fechaHLlegada,
            'numeroEscalas': lie.numeroEscalas,
        }
        id_vuelo = block['id']
    print(id_vuelo)
    trry.append(block)
    print(trry)
    return "nada"

@routes_reserva.route('/savereservas', methods=['POST'] )
def savereservas():
    id_vuelo
    id_usuario = request.json.get('idusuario')
    print(id_usuario)
    estadoreserva = request.json.get('estadoreserva')
    asientosReservados = request.json.get('asientosReservados')
    fechaReserva = datetime.now()
    nasientos = request.json.get('nasientos')
    tipoboleto = request.json.get('tipoboleto')
    print(nasientos, tipoboleto)
    

    resultado = db.session.query(Users).filter(
        Users.correo == id_usuario,
    ).all()
    
    if not resultado:
        message= "El cliente acargo no está regitrado"
        return message
    else:
        reser = Reserva(
            id_usuario = id_usuario,
            estadoreserva= estadoreserva,
            asientosReservados= asientosReservados,
            fechaReserva=fechaReserva,
            nasiento=nasientos,
            tipoBoleto=tipoboleto,
            id_vuelo = id_vuelo,
            
        )
        db.session.add(reser)

    db.session.commit()
    return "algo"
