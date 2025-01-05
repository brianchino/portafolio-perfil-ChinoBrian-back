from base_db.conexion import conexion
from base_db.tabla import Tabla

class Proyecto(Tabla):
    
    tabla = 'proyecto'
    conexion = conexion
    campos = ('id', 'titulo', 'descripcion', 'link')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)  