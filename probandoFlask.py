from flask import Flask, render_template #render_template, plantilla de Flask para ejecutar código HTML.

app = Flask(__name__) #"app" es una variable para guardar el objeto que devuelve Flask (para iniciar Flask). Para crear urls, puede ser app o cualq otro nombre.

@app.route("/") #Ruta para la pag principal, "/" solo.
def index():
    return ("Hola Mundo") 

@app.route("/hola")
def holaSpanish():
    return "Hola perro"

@app.route("/nombre")
def romina():
    nombre = "Romina"
    return render_template("nombre.html", nombre = nombre) #El primer "nombre" hace referencia a la variable que esta entre "{{}}" en la plantilla html. El segundo hace referencia a nombre = "Romina"

@app.route("/about") #Ruta para about
def about():
    return render_template("about.html") #Dentro de una carpeta llamada "templates", va a buscar y a devolver la plantilla o template, en este caso "about"

if __name__ == "__main__":
    app.run(debug=True) #Para no tener que reiniciar el servidor a cada rato, se pone debug=True(significa que es de prueba)


#Para ejecutarlo: 
#1- Abrir consola de W. Poner cdm
#2- cd <desktop> (C:\Users\romin>cd desktop)
#3- cd <Python Website> (C:\Users\romin\Desktop>cd Python Website)
#4- flask run o python <index.py> (C:\Users\romin\Desktop\Python Website>python index.py)

