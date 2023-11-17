from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

class Aerolinea(db.Model):
    __tablename__ = "tblaerolinea"
    
    nombre = db.Column(db.String(300), primary_key=True, autoincrement=False)
    telefono = db.Column(db.Integer)
    
    
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono


def create_roles():

    if Aerolinea.query.count() == 0:
        avianca = Aerolinea('Avianca', '018000953434')
        airlatam = Aerolinea('Airline Latam', '018000949490')
        wingo = Aerolinea('Wingo', '018000111115')
       
        db.session.add(avianca)
        db.session.add(airlatam)
        db.session.add(wingo)
        db.session.commit()

with app.app_context():
    db.create_all()
    create_roles()
            
            
class AirlineSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'telefono')