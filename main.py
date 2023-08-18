from flask import Flask, render_template, url_for

#flask --app main.py run

app = Flask(__name__)

@app.route("/")
def index():
    edad = 18
    #return "<h1>Bienvenidos a Flask</h1>"
    return render_template('index.html', edad = edad)

@app.route("/contacto")
def contactos():
    total = 1000
    
    return "<h1>Bienvenidos a Flask</h1>"

@app.route("/proyectos/")
@app.route("/proyectos/<string:nombre>/<int:edad>")
def proyectos(nombre = None,edad = None):
    if nombre is None:
        return render_template('proyectos.html')
    else:
        return render_template('proyectos.html',nombre = nombre, edad = edad)