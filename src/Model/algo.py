from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template 


class algo(db.Model):
    __tablename__ = "tblalgo"

    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(200))
    descripcion = db.Column(db.Text)

    def __init__(self, nombre, descripcion):
        self.nombre= nombre
        self.descripcion = descripcion
    
    
    with app.app_context():
            db.create_all()
  

class algoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'descripcion')