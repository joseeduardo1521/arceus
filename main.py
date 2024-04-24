from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine
import pandas as pd
# Crear una instancia de la aplicación Flask

app = Flask(__name__)
app.secret_key = "clave_secreta"


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

#conexion tabla priv_user
def liss():
    engine = conector()
    query = "SELECT * FROM priv_user"
    lj = pd.read_sql_query(query,engine)
    return lj

# Función para verificar las credenciales de inicio de sesión
def verificar_credenciales(usuario, contra):
    usuarios = liss()  # Obtener los usuarios y contras de la base de datos
    # Convertir el usuario a entero
    usuario = int(usuario)
    if usuarios[(usuarios['id'] == usuario) & (usuarios['login'] == contra)].shape[0] > 0:
        print("Credenciales válidas")
        return True
    print("Credenciales inválidas")
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)  # Imprimir los datos del formulario para verificar si 'id' está presente
        usuario = request.form.get('id')  # Utilizar get() para evitar KeyError
        contra = request.form.get('login')  # Utilizar get() para evitar KeyError
        if verificar_credenciales(usuario, contra):
            session['usuario'] = usuario
            return redirect(url_for('mostrar_grafico'))  # Redirigir a la página de tickets
        else:
            return render_template('index.html', error=True)  # Renderizar el formulario de inicio de sesión con un mensaje de error
    return render_template('index.html', error=False)  # Renderizar el formulario de inicio de sesión sin mensaje de error

    
@app.route('/tickets')
def mostrar_grafico():
    return render_template('tickets.html')


if __name__ == '__main__':
    # Ejecutar la aplicación en el servidor local en el puerto 5000
     app.run(debug=True)
