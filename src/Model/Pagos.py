from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
from common.Toke import *
from config.db import db, app, ma

class Pagos(db.Model):
    __tablename__ = "tblpagos"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    metodopago = db.Column(db.String(200))
    fechaPago = db.Column(db.Date)
    monto = db.Column(db.Double)
    estadopago = db.Column(db.String(200))
    
    
    def __init__(self, metodopago, fechaPago, monto,  estadopago):
        self.metodopago = metodopago
        self.fechaPago = fechaPago
        self.monto = monto
        self.estadopago = estadopago
        
    with app.app_context():
            db.create_all()
            
            
class PagSchema(ma.Schema):
    class Meta:
        fields = ('id', 'metodopago', 'fechaPago', 'monto', 'estadopago')
    
