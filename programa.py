#Importar las bibliotecas

from flask import *
from flask_sqlalchemy import *
#Crear un objeto de la clase flask

app=Flask(__name__)
#Configurar ela cceso a la DB
#URL de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///estudiantes.sqlite3"

#Crear la DB
db=SQLAlchemy(app)

#Definir las tablas de la base de datos

class Estudiantes(db.Model):
#Definir una llave primaria:Campo cuyo valor nunca se repite
    id=db.Column('id_estudiante', db.Integer, primary_key=True)

#Definir las columnas de las tablas 

    nombre=db.Column(db.String(50))
    codigo=db.Column(db.String(12))

#Crear metodo constructor

    def __init__(self, nombre, codigo):
        
        self.nombre=nombre
        self.codigo=codigo

with app.app_context():

    db.create_all()