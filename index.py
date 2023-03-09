from flask import Flask, render_template

app = Flask(__name__) #Para crear urls, puede ser app o cualq otro nombre, es una variable para guardar el objeto que devuelve Flask

@app.route("/") #Ruta para la pag principal
def home():
    return render_template("home.html") #Devuelve la plantilla

@app.route("/about") #Ruta para about
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True) #Para no tener que reiniciar el servidor a cada rato, se pone debug=True(significa que es de prueba)


#Para ejecutarlo: 
#1- Abrir consola de W. Poner cdm
#2- cd desktop (C:\Users\romin>cd desktop)
#3- cd Python Website (C:\Users\romin\Desktop>cd Python Website)
#4- python index.py (C:\Users\romin\Desktop\Python Website>python index.py)

