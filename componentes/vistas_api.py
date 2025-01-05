from flask import jsonify
from app import app
from componentes.modelos import *
@app.route("/api-portafolio/proyectos",methods=['GET'])
def mostrar_proyectos(): 
    unosProyectos = Proyecto.obtener()
    
    if isinstance(unosProyectos, list):  # Si es una lista
        datos = [unProyecto.__dict__ for unProyecto in unosProyectos]
    else:  # Si es un único objeto
        datos = [unosProyectos.__dict__]
    
    return jsonify(datos)
    