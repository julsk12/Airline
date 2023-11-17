from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

class Vuelo(db.Model):
    __tablename__ = "tblvuelos"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aerolinea = db.Column(db.String(300), db.ForeignKey('tblaerolinea.nombre'))
    ciudadOrigen = db.Column(db.String(300), db.ForeignKey('tblaeropuertos.direccion'))
    ciudadDestino = db.Column(db.String(300), db.ForeignKey('tblaeropuertos.direccion'))
    fechaHSalida = db.Column(db.DateTime)
    fechaHLlegada = db.Column(db.DateTime)
    mascotas = db.Column(db.String(100))
    asientosDisponibles = db.Column(db.String(300))
    precio = db.Column(db.Double)
    numeroEscalas = db.Column(db.Integer)
    duracionVuelo = db.Column(db.String(300))
    
    
    def __init__(self, id_aerolinea, ciudadOrigen, ciudadDestino, fechaHSalida, fechaHLlegada, mascotas, 
                 asientosDisponibles, precio, numeroEscalas, duracionVuelo):
        self.id_aerolinea = id_aerolinea
        self.ciudadOrigen = ciudadOrigen
        self.ciudadDestino = ciudadDestino
        self.fechaHSalida = fechaHSalida
        self.fechaHLlegada = fechaHLlegada
        self.mascotas = mascotas
        self.asientosDisponibles = asientosDisponibles
        self.precio = precio
        self.numeroEscalas = numeroEscalas
        self.duracionVuelo = duracionVuelo
        
        
    with app.app_context():
            db.create_all()
    


class FliesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_aerolinea', 'ciudadOrigen', 'ciudadDestino', 'fechaHSalida', 'fechaHLlegada', 'mascotas'
                  'asientosDisponibles', 'precio', 'numeroEscalas', 'duracionVuelo')