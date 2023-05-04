from mypro.details.models import Users
from config import app_config
from flask import Blueprint,jsonify,request,render_template
mod=Blueprint("details",__name__,url_prefix='/name')

@mod.route("/",methods=["GET"])
def Demo():
    return "tables are cretaed"

@mod.route("/home",methods=["GET"])
def home():
    return render_template("mypro/home.html")

