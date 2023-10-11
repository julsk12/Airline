from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.algo import algo,algoSchema

routes_algo = Blueprint("routes_algo", __name__)
#Roles
algs_schema = algoSchema()
Aslgo_Schema = algoSchema(many=True)

@routes_algo.route('/indexalgo', methods=['GET'] )
def indextag():
    
    return "Hola Mundo!!"


# #Roles
# #---------SAVE/CREAR------------
# @routes_tag.route('/savetag', methods=['POST'] )
# def guardar_taggs():
#     taggs = request.json['nombre_etiqueta, descripcion']
#     print(taggs)
#     new_tag = tags(taggs)
#     db.session.add(new_tag)
#     db.session.commit()
#     return redirect('/rtags')


# @routes_tag.route('/eliminartags/<id>', methods=['GET'] )
# def eliminarTags(id):
#     rol = tags.query.get(id)
#     db.session.delete(rol)
#     db.session.commit()
#     return jsonify(Tags_schema.dump(rol)) 

# @routes_tag.route('/actualizartags', methods=['POST'] )
# def actualizartags():
#     id = request.json['id']
#     nombre_etiqueta = request.json['nombre_etiqueta']
#     descripcion = request.json['descripcion']
#     rtags = tags.query.get(id)
#     rtags.nombre_etiqueta = nombre_etiqueta
#     rtags.descripcion = descripcion
#     db.session.commit()
#     return redirect('/rtags')
