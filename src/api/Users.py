from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
#from common.Toke import *
from config.db import db, app, ma

from Model.Usuarios import Users, UsuariosSchema

routes_users = Blueprint("routes_users", __name__)

user_schema = UsuariosSchema()
usuarios_Schema = UsuariosSchema(many=True)

@routes_users.route('/users', methods=['GET'])
def obtenerusuarios():
    returnall = Users.query.all()
    result_usuarios = usuarios_Schema.dump(returnall)
    return jsonify(result_usuarios)

#-------------------CRUD---------------------------------
@routes_users.route('/eliminarusers/<id>', methods=['GET'] )
def eliminarusers(id):
    user = Users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))

@routes_users.route('/actualizaruser', methods=['POST'] )
def actualizarautores():
    id = request.json['id']
    nombre = request.json['nombre']
    correo = request.json['correo']
    password = request.json['password']
    celular = request.json['celular']
    direccion = request.json['direccion']
    auses = Users.query.get(id)
    auses.Users = nombre
    auses.Users = correo
    auses.Users = password
    auses.Users = celular
    auses.Users = direccion
    db.session.commit()
    return redirect('/users')

@routes_users.route('/guardarusuarios', methods=['POST'] )
def guardar_users():
    uses = request.json['id','nombre', 'correo', 'password', 'celular', 'direccion']
    new_user = Users(uses)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/autores')

@routes_users.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    new_paq = Users(correo=data['correo'],
                    nombre=data['nombre'],
                    cedula=data['cedula'], 
                    password=data['password'], 
                    celular=data['celular'], 
                    direccion=data['direccion'],)
    db.session.add(new_paq)
    db.session.commit()
    return ""

@routes_users.route('/ingresar', methods=['GET'])
def ingresar():
    datos = {}
    usuarios_table = db.Model.metadata.tables['tblsusuarios']
    resultado = db.session.query(Users).select_from(Users).all()
    i = 0
    for correo in resultado:
        i += 1
        datos[i] = {
            'correou': correo.correo,
            'password': correo.password
        }
    print(datos)
    return jsonify(datos)

@routes_users.route('/perfilUS', methods=['GET'])
def perfilUS():
    datos = {}
    usuarios_table = db.Model.metadata.tables['tblsusuarios']
    resultado = db.session.query(Users).select_from(Users).all()
    i = 0
    for correo in resultado:
        i += 1
        datos[i] = {
            'correou': correo.correo,
            'nombreu': correo.nombre,
            'cedulau': correo.cedula,
            'celularu': correo.celular,
            'direccionu': correo.direccion,
        }
    print(datos)
    return jsonify(datos)