from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

class DetallesPago(db.Model):
    __tablename__ = "tbldetallespago"
    
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_vuelo = db.Column(db.Integer, db.ForeignKey('tblreservas.id'))
    id_pago = db.Column(db.Integer, db.ForeignKey('tblpagos.id'))
    fechapago= db.Column(db.DateTime)
    
    def __init__(self, id_vuelo, id_pago, fechapago):
        self.id_vuelo = id_vuelo
        self.id_pago = id_pago
        self.fechapago = fechapago
        
    with app.app_context():
            db.create_all()
            
class DetallesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_vuelo', 'id_pago', 'fechapago')