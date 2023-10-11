from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

class Reserva(db.Model):
    __tablename__ = "tblreservas"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblsusuarios.id'))
    estadoreserva = db.Column(db.String(200))
    asientosReservados = db.Column(db.Integer)
    fechaReserva = db.Column(db.Date)
    nasiento = db.Column(db.String(200))
    tipoBoleto = db.Column(db.String(200))
    id_vuelo = db.Column(db.Integer, db.ForeignKey('tblvuelos.id'))
    
    
    
    def __init__(self, id_usuario, estadoreserva,  asientosReservados, fechaReserva, nasiento, tipoBoleto, id_vuelo):
        self.id_usuario = id_usuario
        self.estadoreserva = estadoreserva
        self.asientosReservados = asientosReservados
        self.fechaReserva = fechaReserva
        self.nasiento = nasiento
        self.tipoBoleto = tipoBoleto
        self.id_vuelo = id_vuelo
    
    
    with app.app_context():
            db.create_all()
            
class ReseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario', 'estadoreserva', 'asientosReservados', 'fechaReserva', 'nasiento', 'tipoBoleto', 'id_vuelo')