from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

class Users(db.Model):
    __tablename__ = "tblsusuarios"
    
    correo = db.Column(db.String(200), primary_key=True)
    nombre = db.Column(db.String(200))
    password = db.Column(db.String(200))
    celular = db.Column(db.Integer)
    direccion = db.Column(db.String(200))
    
    def __init__(self,  correo, nombre, password, celular, direccion):
        self.correo = correo
        self.nombre = nombre
        self.password = password
        self.celular = celular
        self.direccion = direccion
        
    with app.app_context():
            db.create_all()
            
            
class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('correo', 'nombre', 'password', 'celular', 'direccion')
    