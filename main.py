from flask import Flask, render_template
from sqlalchemy import create_engine
import pandas as pd
# Crear una instancia de la aplicación Flask
app = Flask(__name__)


#Restructura de la conexión a base de datos
def conector():
    engine = create_engine("mysql+mysqlconnector://limacinv:D%j9Uf?B*@tuticketlimac.com/limac_prod")
    return engine

#conexion tabla ticket
def obtener_general():
    engine = conector()
    query = "SELECT * FROM ticket"
    df = pd.read_sql_query(query, engine)
    return df

# Definir una ruta y una función para manejar esa ruta
@app.route('/')
def hello():
    obtener_general()
    return render_template('index.html')



if __name__ == '__main__':
    # Ejecutar la aplicación en el servidor local en el puerto 5000
     app.run(debug=True)
