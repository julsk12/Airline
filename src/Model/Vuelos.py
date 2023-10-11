from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

class Vuelo(db.Model):
    __tablename__ = "tblvuelos"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aerolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea.id'))
    ciudadOrigen = db.Column(db.Integer, db.ForeignKey('tblaeropuertos.id'))
    ciudadDestino = db.Column(db.Integer, db.ForeignKey('tblaeropuertos.id'))
    fechaHSalida = db.Column(db.DateTime)
    fechaHLlegada = db.Column(db.DateTime)
    asientosDisponibles = db.Column(db.String(300))
    precio = db.Column(db.Double)
    tipoAvion = db.Column(db.String(300))
    numeroEscalas = db.Column(db.Integer)
    duracionVuelo = db.Column(db.String(300))
    
    
    def __init__(self, aerolinea, ciudadOrigen, ciudadDestino, fechaHSalida, fechaHLlegada,
                 asientosDisponibles, precio, tipoAvion, numeroEscalas, duracionVuelo):
        self.aerolinea = aerolinea
        self.ciudadOrigen = ciudadOrigen
        self.ciudadDestino = ciudadDestino
        self.fechaHSalida = fechaHSalida
        self.fechaHLlegada = fechaHLlegada
        self.asientosDisponibles = asientosDisponibles
        self.precio = precio
        self.tipoAvion = tipoAvion
        self.numeroEscalas = numeroEscalas
        self.duracionVuelo = duracionVuelo
        
        
    with app.app_context():
            db.create_all()
    


class FliesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'aerolinea', 'ciudadOrigen', 'ciudadDestino', 'fechaHSalida', 'fechaHLlegada',
                  'asientosDisponibles', 'precio', 'tipoAvion', 'numeroEscalas', 'duracionVuelo')