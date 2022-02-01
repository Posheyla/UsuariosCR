from inspect import isdatadescriptor
from usuarios_app.config.mysqlconnection import MySQLConnection,connectToMySQL

class Usuario:
    def __init__(self,id,nombre,apellido,email,created_at,update_at):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.created_at = created_at
        self.update_at = update_at

    @classmethod
    def agregarUsuario(cls,nuevoUsuario):
        query = "INSERT INTO usuarios(nombre,apellido,email,created_at,update_at) VALUES(%(nombre)s,%(apellido)s,%(email)s,CURRENT_DATE(),CURRENT_DATE());"
        resultado = connectToMySQL("esquema_usuario").query_db(query,nuevoUsuario)
        return resultado

    @classmethod
    def obtenerListaUsarios(cls):
        query = "SELECT * FROM usuarios"
        resultado = connectToMySQL("esquema_usuario").query_db(query)
        listaDeUsuarios=[]
        for usuario in resultado:
            listaDeUsuarios.append(cls(usuario["id"],usuario["nombre"],usuario["apellido"],usuario["email"],usuario["created_at"],usuario["update_at"]))
        return listaDeUsuarios