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
        "Nombre": "El Edén",
        "Teléfono": "67479400",
        "Dirección": "Quindío, Colombia"
    },
    {
        "Nombre": "Palonegro",
        "Teléfono": "(607) 6910140",
        "Dirección": "Santander, Colombia"
    },
    {
        "Nombre": "Rafael Núñez",
        "Teléfono": "(5) 6931351",
        "Dirección": "Cartagena, Colombia"
    },
    {
        "Nombre": "Gustavo Rojas Pinilla",
        "Teléfono": "+57 8 512 6112",
        "Dirección": "San Andrés, Colombia"
    },
    {
        "Nombre": "Los Garzones",
        "Teléfono": "(+57) 604 7911476",
        "Dirección": "Montería, Colombia"
    },
    {
        "Nombre": "Almirante Padilla",
        "Teléfono": "301 3445618",
        "Dirección": "Riohacha, Colombia"
    },
    {
        "Nombre": "Aeropuerto Internacional Ernesto Cortissoz (BAQ), Barranquilla, Colombia",
        "Teléfono": "6053160900",
        "Dirección": "Barranquilla, Colombia"
    },
    {
        "Nombre": "Aeropuerto Internacional El Dorado (BOG), Bogotá, Colombia",
        "Teléfono": "6012662000",
        "Dirección": "Bogotá, Colombia"
    },
    {
        "Nombre": "Aeropuerto Internacional Alfonso Bonilla Aragón (CLO), Cali, Colombia",
        "Teléfono": "6663026",
        "Dirección": "Cali, Colombia"
    },
    {
        "Nombre": "Aeropuerto Internacional Camilo Daza (CUC), Cúcuta, Colombia",
        "Teléfono": "7433073",
        "Dirección": "Cúcuta, Colombia"
    },
    {
        "Nombre": "Aeropuerto Alfredo Vásquez Cobo (LET), Leticia, Colombia",
        "Teléfono": "14251000",
        "Dirección": "Leticia, Colombia"
    },
    {
        "Nombre": "Aeropuerto Internacional José María Córdova (MDE), Medellín, Colombia",
        "Teléfono": "604 402 5110",
        "Dirección": "Medellín, Colombia"
    },
    {
        "Nombre": "Aeropuerto Internacional Matecaña (PEI), Pereira, Colombia",
        "Teléfono": "3148151",
        "Dirección": "Pereira, Colombia"
    },
    {
        "Nombre": "Aeropuerto Internacional Simón Bolívar (SMR), Santa Marta, Colombia",
        "Teléfono": "54381360",
        "Dirección": "Santa Marta, Colombia"
    },
    {
        "Nombre": "Aeropuerto Antonio Nariño (PSO), Pasto, Colombia",
        "Teléfono": "3167185787",
        "Dirección": "Pasto, Colombia"
    }
]
aeropuertos_extranjeros = [
    {
        "Nombre": "Aeropuerto Internacional de Dubái (DXB), Dubái, Emiratos Árabes Unidos",
        "Dirección": "Dubái, Emiratos Árabes Unidos"
    },
    {
        "Nombre": "Aeropuerto Internacional de Hamad (DOH), Doha, Catar",
        "Dirección": "Doha, Catar"
    },
    {
        "Nombre": "Aeropuerto Changi de Singapur (SIN), Singapur, Singapur",
        "Dirección": "Singapur, Singapur"
    },
    {
        "Nombre": "Aeropuerto Suvarnabhumi de Bangkok (BKK), Bangkok, Tailandia",
        "Dirección": "Bangkok, Tailandia"
    },
    {
        "Nombre": "Aeropuerto Internacional John F. Kennedy (JFK), Nueva York, EE. UU.",
        "Dirección": "Nueva York, EE. UU."
    },
    {
        "Nombre": "Aeropuerto Heathrow de Londres (LHR), Londres, Reino Unido",
        "Dirección": "Londres, Reino Unido"
    },
    {
        "Nombre": "Aeropuerto Internacional de Narita (NRT), Tokio, Japón",
        "Dirección": " Tokio, Japón"
    },
    {
        "Nombre": "Aeropuerto Kingsford Smith de Sídney (SYD), Sídney, Australia",
        "Dirección": "Sídney, Australia"
    },
    {
        "Nombre": "Aeropuerto Internacional de Pekín-Capital (PEK), Pekín, China",
        "Dirección": "Pekín, China"
    },
    {
        "Nombre": "Aeropuerto Internacional de Miami (MIA), Miami, EE. UU.",
        "Dirección": "Miami, EE. UU."
    },
    {
        "Nombre": "Aeropuerto Adolfo Suárez Madrid-Barajas (MAD), Madrid, España",
        "Dirección": "Madrid, España"
    },
    {
        "Nombre": "Aeropuerto Internacional de Guarulhos (GRU), Sao Paulo, Brasil",
        "Dirección": "Sao Paulo, Brasil"
    },
    {
        "Nombre": "Aeropuerto Internacional de la Ciudad de México (MEX), Ciudad de México, México",
        "Dirección": "Ciudad de México, México"
    },
    {
        "Nombre": "Aeropuerto Charles de Gaulle (CDG), París, Francia",
        "Dirección": "París, Francia"
    },
    {
        "Nombre": "Aeropuerto Internacional Ministro Pistarini (EZE), Buenos Aires, Argentina",
        "Dirección": "Buenos Aires, Argentina"
    },
    {
        "Nombre": "Aeropuerto Internacional Jorge Chávez (LIM), Lima, Perú",
        "Dirección": "Lima, Perú"
    },
    {
        "Nombre": "Aeropuerto de Roma-Fiumicino (FCO), Roma, Italia",
        "Dirección": "Roma, Italia"
    },
    {
        "Nombre": "Aeropuerto Internacional Toronto Pearson (YYZ), Toronto, Canadá",
        "Dirección": "Toronto, Canadá"
    },
    {
        "Nombre": "Aeropuerto de Brisbane (BNE), Brisbane, Australia",
        "Dirección": "Melbourne, Australia"
    },
    {
        "Nombre": "Aeropuerto Internacional de Los Ángeles (LAX), Los Ángeles, EE. UU.",
        "Dirección": "Los Ángeles, EE. UU."
    },
    {
        "Nombre": "Aeropuerto Internacional Indira Gandhi (DEL), Nueva Delhi, India",
        "Dirección": "Nueva Delhi, India"
    },
    {
        "Nombre": "Aeropuerto Internacional Hartsfield-Jackson (ATL), Atlanta, EE. UU.",
        "Dirección": "Atlanta, EE. UU."
    },
    {
        "Nombre": "Aeropuerto Internacional Louis Armstrong (MSY), Nueva Orleans, EE. UU.",
        "Dirección": "Nueva Orleans, EE. UU."
    },
    {
        "Nombre": "Aeropuerto Internacional Simón Bolívar (CCS), Caracas, Venezuela",
        "Dirección": "Caracas, Venezuela"
    },
    {
        "Nombre": "Aeropuerto Internacional Luis Muñoz Marín (SJU), San Juan, Puerto Rico",
        "Dirección": "San Juan, Puerto Rico"
    },
    {
        "Nombre": "Aeropuerto Internacional José Martí (HAV), La Habana, Cuba",
        "Dirección": "La Habana, Cuba"
    },
    {
        "Nombre": "Aeropuerto Humberto Delgado (LIS), Lisboa, Portugal",
        "Dirección": "Lisboa, Portugal"
    },
    {
        "Nombre": "Aeropuerto Internacional de Sheremétievo (SVO), Moscú, Rusia",
        "Dirección": "Moscú, Rusia"
    },
    {
        "Nombre": "Aeropuerto Internacional de San Francisco (SFO), San Francisco, EE. UU.",
        "Dirección": "San Francisco, EE. UU."
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