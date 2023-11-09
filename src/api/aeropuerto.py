from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

from Model.Aeropuertos import Aeropuerto, AirportSchema

routes_aeropuerto =  Blueprint("routes_aeropuerto", __name__)

airpor_schema = AirportSchema()
airport_Schema = AirportSchema(many=True)

@routes_aeropuerto.route('/aeropuerto', methods=['GET'])
def obtenerairport():
    returnall = Aeropuerto.query.all()
    result_port = airport_Schema.dump(returnall)
    return jsonify(result_port)

#-------------------CRUD---------------------------------
@routes_aeropuerto.route('/eliminarairport/<id>', methods=['GET'] )
def eliminarport(id):
    port = Aeropuerto.query.get(id)
    db.session.delete(port)
    db.session.commit()
    return jsonify(airpor_schema.dump(port))

@routes_aeropuerto.route('/actualizarairport', methods=['POST'] )
def actualizarport():
    id = request.json['id']
    nombre = request.json['nombre']
    ubicacion = request.json['ubicacion']
    correo = request.json['correo']
    telefono = request.json['telefono']
    direccion = request.json['direccion']    
    serviciosdisponibles = request.json['serviciosdisponibles']

    aport = Aeropuerto.query.get(id)
    aport.Aeropuerto = nombre
    aport.Aeropuerto = ubicacion
    aport.Aeropuerto = correo
    aport.Aeropuerto = telefono
    aport.Aeropuerto = direccion
    aport.Aeropuerto = serviciosdisponibles

    db.session.commit()
    return redirect('/aeropuerto')

@routes_aeropuerto.route('/guardarairport', methods=['POST'] )
def guardar_port():
    port = request.json['nombre','ubicacion', 'correo', 'telefono', 'direccion', 'serviciosdisponibles']
    new_port = Aeropuerto(port)
    db.session.add(new_port)
    db.session.commit()
    return redirect('/aeropuerto')

#---------------Lista aeropuertos---------------------------------
aeropuertos_nacionales = [
    {
        "Nombre": "Antonio Roldán Betancourt",
        "Teléfono": "6045208543",
        "Dirección": "Kilómetro 10, vía Zungo Embarcadero, Apartadó/Carepa, Antioquia"
    },
    {
        "Nombre": "Santiago Pérez Quiroz",
        "Teléfono": "078852297",
        "Dirección": "81001 Arauca/Arauca"
    },
    {
        "Nombre": "José Celestino Mutis",
        "Teléfono": "3184512723",
        "Dirección": "27075 Bahía Solano/Chocó"
    },
    {
        "Nombre": "Yariguíes",
        "Teléfono": "3175180631",
        "Dirección": "Barrancabermeja/Santander"
    },
    {
        "Nombre": "Guaymaral",
        "Teléfono": "14251000",
        "Dirección": "Av. El Dorado #103-15, Bogotá/Distrito Capital"
    },
    {
        "Nombre": "Juan H. White",
        "Teléfono": "3104294246",
        "Dirección": "Carrera 16 #calle 14, Caucasia/Antioquia"
    },
    {
        "Nombre": "Gustavo Artunduaga",
        "Teléfono": "84351495",
        "Dirección": "18001 Florencia/Caquetá"
    },
    {
        "Nombre": "Juan Casiano",
        "Teléfono": "28400188",
        "Dirección": "19318 Guapi/Departamento de Cauca"
    },
    {
        "Nombre": "Perales",
        "Teléfono": "6014251000",
        "Dirección": "Via Aeropuerto Ibagué Km 1, Ibagué/Tolima"
    },
    {
        "Nombre": "San Luis",
        "Teléfono": "6027739714",
        "Dirección": "Aeropuerto de San Luis, Ipiales/Aldana, Nariño"
    },
    {
        "Nombre": "Javier Noreña Valencia",
        "Teléfono": "3102802054",
        "Dirección": "La Macarena/Meta"
    },
    {
        "Nombre": "La Nubia",
        "Teléfono": "6068745451",
        "Dirección": "Nubia, Manizales/Caldas"
    },
    {
        "Nombre": "Enrique Olaya Herrera",
        "Teléfono": "6043656100",
        "Dirección": "Cra. 65 #13-157, Guayabal, Medellín/Antioquia"
    },
    {
        "Nombre": "Villagarzón",
        "Teléfono": "3112546898",
        "Dirección": "Mocoa/Villagarzón, Putumayo"
    },
    {
        "Nombre": "Jorge Isaacs",
        "Teléfono": "53505145",
        "Dirección": "Maicao/Albania, La Guajira"
    },
    {
        "Nombre": "Fabio Alberto León Bentley",
        "Teléfono": "3162716002",
        "Dirección": "Mitú/Vaupés"
    },
    {
        "Nombre": "Benito Salas",
        "Teléfono": "7887570",
        "Dirección": "Neiva/Huila"
    },
    {
        "Nombre": "Reyes Murillo",
        "Teléfono": "3229447375",
        "Dirección": "Nuquí/Chocó"
    },
    {
        "Nombre": "Antonio Nariño",
        "Teléfono": "3167185787",
        "Dirección": "Pasto/Chachagüí, Nariño"
    },
    {
        "Nombre": "Contador",
        "Teléfono": "3155529858",
        "Dirección": "Pitalito/Huila"
    },
    {
        "Nombre": "Guillermo León Valencia",
        "Teléfono": "28231900",
        "Dirección": "Cl. 4 Nte., Comuna 1, Popayán/Cauca"
    },
    {
        "Nombre": "El Embrujo",
        "Teléfono": "85148176",
        "Dirección": "88564 Providencia/San Andrés y Providencia"
    },
    {
        "Nombre": "Tres de Mayo",
        "Teléfono": "3202921317",
        "Dirección": "Cra. 20, Puerto Asís/Putumayo"
    },
    {
        "Nombre": "Morelia",
        "Teléfono": "",
        "Dirección": "Puerto Gaitán/Meta"
    },
    {
        "Nombre": "César Gaviria Trujillo",
        "Teléfono": "85656069",
        "Dirección": "Puerto Inírida/Guainía"
    },
    {
        "Nombre": "Caucaya",
        "Teléfono": "3115610628",
        "Dirección": "86573 Puerto Leguízamo/Putumayo"
    },
    {
        "Nombre": "Germán Olano",
        "Teléfono": "3102880476",
        "Dirección": "Puerto Carreño/Vichada"
    },
    {
        "Nombre": "El Caraño",
        "Teléfono": "46711537",
        "Dirección": "Quibdó/Chocó"
    },
    {
        "Nombre": "Jorge Enrique González",
        "Teléfono": "3228546866",
        "Dirección": "San José del Guaviare"
    },
    {
        "Nombre": "Los Colonizadores",
        "Teléfono": "3193909388",
        "Dirección": "Saravena/Arauca"
    },
    {
        "Nombre": "Las Brujas",
        "Teléfono": "52499735",
        "Dirección": "25, Corozal, Sincelejo/Corozal, Sucre"
    },
    {
        "Nombre": "La Florida",
        "Teléfono": "2272598",
        "Dirección": "Tumaco, San Andres de Tumaco/Nariño"
    },
    {
        "Nombre": "Puerto Bolívar",
        "Teléfono": "3215431281",
        "Dirección": "Puerto Bolivar/Uribia/La Guajira"
    },
    {
        "Nombre": "Alfonso López Pumarejo",
        "Teléfono": "6055582323",
        "Dirección": "km 5 de, Valledupar/Cesar"
    },
    {
        "Nombre": "Vanguardia",
        "Teléfono": "3217622520",
        "Dirección": "Villavicencio/Meta"
    },
    {
        "Nombre": "El Alcaraván",
        "Teléfono": "86358352",
        "Dirección": "Yopal/Casanare"
    }
]
#---------------Lista aeropuertos Fin-----------------------------
@routes_aeropuerto.route('/guardaraeropuerto', methods=['POST'])
def guardaraeropuerto():
    for aeropuerto_data in aeropuertos_nacionales:
        nombre = aeropuerto_data['Nombre']
        direccion = aeropuerto_data['Dirección']

        aeropuerto_existente = Aeropuerto.query.filter_by(nombre=nombre, direccion=direccion).first()

        if aeropuerto_existente is None:
            nuevo_aeropuerto = Aeropuerto(
                nombre=nombre,
                telefono=aeropuerto_data.get('Teléfono', ''),
                direccion=direccion,
                serviciosdisponibles=''
            )
            db.session.add(nuevo_aeropuerto)

    db.session.commit()
    return redirect('/aeropuerto')

