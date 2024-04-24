from flask import Flask, render_template

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta y una función para manejar esa ruta
@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    # Ejecutar la aplicación en el servidor local en el puerto 5000
     app.run(debug=True)
