from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

from Model.Comentarios import Comentario, ComentarSchema

routes_comentar =  Blueprint("routes_comentar", __name__)

comen_schema = ComentarSchema()
comentar_Schema = ComentarSchema(many=True)

@routes_comentar.route('/comentar', methods=['GET'])
def obtenercomen():
    returnall = Comentario.query.all()
    result_ment = ComentarSchema.dump(returnall)
    return jsonify(result_ment)

#-------------------CRUD---------------------------------
@routes_comentar.route('/eliminarcomen/<id>', methods=['GET'] )
def eliminarcoment(id):
    comen = Comentario.query.get(id)
    db.session.delete(comen)
    db.session.commit()
    return jsonify(comen_schema.dump(comen))

@routes_comentar.route('/actualizarcomen', methods=['POST'] )
def actualizarcoment():
    id = request.json['id']
    id_usuario = request.json['id_usuario']
    id_vuelo = request.json['id_vuelo']
    calificacion = request.json['calificacion']
    comentario = request.json['comentario']
    fechacomen = request.json['fechacomen']    

    acomentario = Comentario.query.get(id)
    acomentario.Comentario = id_usuario
    acomentario.Comentario = id_vuelo
    acomentario.Comentario = calificacion
    acomentario.Comentario = comentario
    acomentario.Comentario = fechacomen

    db.session.commit()
    return redirect('/comentar')

@routes_comentar.route('/guardarcomen', methods=['POST'] )
def guardar_coment():
    coment = request.json['id_usuario','id_vuelo', 'calificacion', 'comentario', 'fechacomen']
    new_comen = Comentario(coment)
    db.session.add(new_comen)
    db.session.commit()
    return redirect('/comentar')