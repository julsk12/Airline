from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuertos"
    
    nombre = db.Column(db.String(300))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200), primary_key=True, autoincrement=False)
    serviciosdisponibles = db.Column(db.Text)
    
    
    def __init__(self, nombre, telefono, direccion, serviciosdisponibles):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.serviciosdisponibles = serviciosdisponibles
        
    with app.app_context():
            db.create_all()
            
            
class AirportSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'telefono', 'direccion', 'serviciosdisponibles')