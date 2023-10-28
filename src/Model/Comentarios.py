from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

class Comentario(db.Model):
    __tablename__ = "tblcomentarios"
    
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblsusuarios.id'))
    id_reserva = db.Column(db.Integer, db.ForeignKey('tblreservas.id'))
    calificacion = db.Column(db.Integer)
    comentario = db.Column(db.Text)
    fechacomen = db.Column(db.Date)
    
    
    def __init__(self, id, id_usuario,id_reserva, calificacion, comentario, fechacomen):
        self.id = id
        self.id_usuario = id_usuario
        self.id_reserva = id_reserva
        self.calificacion = calificacion
        self.comentario = comentario
        self.fechacomen = fechacomen
        
    with app.app_context():
            db.create_all()
            
            
class ComentarSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario', 'id_reserva', 'calificacion', 'comentario', 'fechacomen')