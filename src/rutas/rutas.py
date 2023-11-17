from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_home = Blueprint("routes_home", __name__)


@routes_home.route('/indexvuelos', methods=['GET'] )
def indexvuelos():
    return render_template('/public/vuelos.html')