from flask import Flask, Blueprint, redirect, jsonify, json, session, render_template, request
#from common.Toke import *
from config.db import db, app, ma

class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuertos"
    
    nombre = db.Column(db.String(300))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200), primary_key=True, autoincrement=False)
    serviciosdisponibles = db.Column(db.Text)
    
    
    def __init__(self, nombre, telefono, direccion, serviciosdisponibles):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.serviciosdisponibles = serviciosdisponibles

aeropuertos_nacionales = [
    {
        "Nombre": "Antonio Roldán Betancourt",
        "Teléfono": "6045208543",
        "Dirección": "Antioquia, Colombia"
    },
    {
        "Nombre": "Santiago Pérez Quiroz",
        "Teléfono": "078852297",
        "Dirección": "Arauca, Colombia"
    },
    {
        "Nombre": "Yariguíes",
        "Teléfono": "3175180631",
        "Dirección": "Barrancabermeja, Colombia"
    },
    {
        "Nombre": "Gustavo Artunduaga",
        "Teléfono": "84351495",
        "Dirección": "Florencia, Colombia"
    },
    {
        "Nombre": "Aeropuerto Perales",
        "Teléfono": "6014251000",
        "Dirección": "Ibagué, Colombia"
    },
    {
        "Nombre": "Javier Noreña Valencia",
        "Teléfono": "3102802054",
        "Dirección": "La Macarena, Colombia"
    },
    {
        "Nombre": "La Nubia",
        "Teléfono": "6068745451",
        "Dirección": "Manizales, Colombia"
    },
    {
        "Nombre": "Enrique Olaya Herrera",
        "Teléfono": "6043656100",
        "Dirección": "Medellín, Colombia"
    },
    {
        "Nombre": "Villagarzón",
        "Teléfono": "3112546898",
        "Dirección": "Villagarzón, Colombia"
    },
    {
        "Nombre": "Benito Salas",
        "Teléfono": "7887570",
        "Dirección": "Neiva, Colombia"
    },
    {
        "Nombre": "Antonio Nariño",
        "Teléfono": "3167185787",
        "Dirección": "Pasto, Colombia"
    },
    {
        "Nombre": "Guillermo León Valencia",
        "Teléfono": "28231900",
        "Dirección": "Popayán, Colombia"
    },
    {
        "Nombre": "El Embrujo",
        "Teléfono": "85148176",
        "Dirección": "San Andrés, Colombia"
    },
    {
        "Nombre": "Tres de Mayo",
        "Teléfono": "3202921317",
        "Dirección": "Putumayo, Colombia"
    },
    {
        "Nombre": "Morelia",
        "Teléfono": "",
        "Dirección": "Puerto Gaitán, Colombia"
    },
    {
        "Nombre": "César Gaviria Trujillo",
        "Teléfono": "85656069",
        "Dirección": "Guainía, Colombia"
    },
    {
        "Nombre": "Germán Olano",
        "Teléfono": "3102880476",
        "Dirección": "Puerto Carreño, Colombia"
    },
    {
        "Nombre": "El Caraño",
        "Teléfono": "46711537",
        "Dirección": "Quibdó, Colombia"
    },
    {
        "Nombre": "Jorge Enrique González",
        "Teléfono": "3228546866",
        "Dirección": "Guaviare, Colombia"
    },
    {
        "Nombre": "Las Brujas",
        "Teléfono": "52499735",
        "Dirección": "Sincelejo, Colombia"
    },
    {
        "Nombre": "La Florida",
        "Teléfono": "2272598",
        "Dirección": "Tumaco, Colombia"
    },
    {
        "Nombre": "Puerto Bolívar",
        "Teléfono": "3215431281",
        "Dirección": "La Guajira, Colombia"
    },
    {
        "Nombre": "Alfonso López Pumarejo",
        "Teléfono": "6055582323",
        "Dirección": "Valledupar, Colombia"
    },
    {
        "Nombre": "Vanguardia",
        "Teléfono": "3217622520",
        "Dirección": "Villavicencio,Colombia"
    },
    {
        "Nombre": "El Alcaraván",
        "Teléfono": "86358352",
        "Dirección": "Yopal, Colombia"
    }
]
aeropuertos_extranjeros = [
    {
        "Nombre": "Aeropuerto Internacional John F. Kennedy (JFK)",
        "Dirección": "Nueva York, Estados Unidos"
    },
    {
        "Nombre": "Aeropuerto Heathrow de Londres (LHR)",
        "Dirección": "Reino Unido, Londres"
    },
    {
        "Nombre": "Aeropuerto Internacional de Dubái (DXB)",
        "Dirección": "Dubái, Emiratos Árabes Unidos"
    },
    {
        "Nombre": "Aeropuerto Internacional de Narita (NRT)",
        "Dirección": " Tokio, Japón"
    },
    {
        "Nombre": "Aeropuerto Internacional de Hamad (DOH)",
        "Dirección": "Doha, Catar"
    },
    {
        "Nombre": "Aeropuerto Changi de Singapur (SIN)",
        "Dirección": "Singapur, Singapur"
    },
    {
        "Nombre": "Aeropuerto Suvarnabhumi de Bangkok (BKK)",
        "Dirección": "Bangkok, Tailandia"
    },
    {
        "Nombre": "Aeropuerto Kingsford Smith de Sídney (SYD)",
        "Dirección": "Sídney, Australia"
    },
    {
        "Nombre": "Aeropuerto Internacional de Pekín-Capital (PEK)",
        "Dirección": "Pekín, China"
    }
]


def create_aero():
    if Aeropuerto.query.count() == 0:
        for aeropuerto_data in aeropuertos_nacionales + aeropuertos_extranjeros:
            nombre = aeropuerto_data['Nombre']
            direccion = aeropuerto_data['Dirección']
            telefono = aeropuerto_data.get('Teléfono', '')
            serviciosdisponibles = aeropuerto_data.get('ServiciosDisponibles', '')

            nuevo_aeropuerto = Aeropuerto(
                nombre=nombre,
                telefono=telefono,
                direccion=direccion,
                serviciosdisponibles=serviciosdisponibles
            )

            
            db.session.add(nuevo_aeropuerto)

        
        db.session.commit()

with app.app_context():
    db.create_all()
    create_aero()

            
            
class AirportSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'telefono', 'direccion', 'serviciosdisponibles')