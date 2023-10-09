from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

class Reserva(db.Model):
    __tablename__ = "tblreservas"
    
    id = db.Columm(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblsusuarios.id'))
    id_vuelo = db.Column(db.Integer, db.ForeignKey('tblvuelos.id'))
    estadoreserva = db.Column(db.String(200))
    asientosReservados = db.Column(db.Integer)
    fechaReserva = db.Column(db.Date)
    
    
    def __init__(self, id_usuario, id_vuelo, estadoreserva,  asientosReservados, fechaReserva):
        self.id_usuario = id_usuario
        self.id_vuelo = id_vuelo
        self.estadoreserva = estadoreserva
        self.asientosReservados = asientosReservados
        self.fechaReserva = fechaReserva
    
    
    with app.app_context():
            db.create_all()
            
class ReseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario', 'id_vuelo', 'estadoreserva', 'asientosReservados', 'fechaReserva')