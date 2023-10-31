from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

class Aerolinea(db.Model):
    __tablename__ = "tblaerolinea"
    
    id= db.Column(db.Integer, autoincrement=True)
    nombre = db.Column(db.String(300), primary_key=True, autoincrement=False)
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200))
    politicaequipaje = db.Column(db.Text)
    
    
    def __init__(self, id, nombre, telefono, direccion, politicaequipaje):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.politicaequipaje = politicaequipaje
        
    with app.app_context():
            db.create_all()
            
            
class AirlineSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'telefono', 'direccion', 'politicaequipaje')