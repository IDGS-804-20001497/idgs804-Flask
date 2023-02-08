from flask import Flask, render_template
from flask import request 
import math


app = Flask(__name__)

@app.route("/Cinepolis")
def datos():
    return render_template("cinepolisFlask.html")


@app.route("/resultadoCine", methods=["POST", "GET"])

def resultadoCine():
    nombre = request.form.get("txtNom")
compradores = request.form.get("txtCompradores") 
tarjeta = request.form.get("tarjeta")
boletas = request.form.get("txtBoletas") 

if int(boletas) > int(compradores)*7:
         res="NO SE PUEDEN COMPRAR MÁS DE 7 BOLETAS POR PRRSONA"
else:
        res=int(boletas)*12
        if int(boletas) > 5:
            res=res*.85
        elif int(boletas) == 3 or int(boletas) == 4 or int(boletas) == 5:
            res=res*.90
        else:
            res = res 
        
        if tarjeta == "si":
            res=res*.90

return render_template("resultadoCine.html",nombre=nombre, 
    compradores=compradores, boletas=boletas, res=res)


if __name__ == "__main__":
    app.run(debug=True, port=3000) 