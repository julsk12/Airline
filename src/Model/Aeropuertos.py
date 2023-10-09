from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuertos"
    
    id= db.Columm(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(300))
    ubicacion = db.Column(db.String(300))
    correo = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200))
    serviciosdisponibles = db.Column(db.Text)
    
    
    def __init__(self, id, nombre,ubicacion, correo, telefono, direccion, serviciosdisponibles):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.serviciosdisponibles = serviciosdisponibles
        
    with app.app_context():
            db.create_all()
            
            
class AirportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'ubicacion', 'correo', 'telefono', 'direccion', 'serviciosdisponibles')