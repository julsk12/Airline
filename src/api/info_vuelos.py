# from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from datetime import datetime, timedelta
import random

from Model.info_vuelo import Informacion, InfoSchema

routes_info= Blueprint("routes_info", __name__)

infor_schema = InfoSchema()
info_Schema = InfoSchema(many=True)


@routes_info.route("/infor", methods=["GET"])
def obtenerinfo():
    returnall = Informacion.query.all()
    result_flies = info_Schema.dump(returnall)
    return jsonify(result_flies)


# -------------------CRUD---------------------------------
