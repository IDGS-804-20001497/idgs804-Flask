from flask import Flask, render_template
from flask import request
import math

app = Flask(__name__)

@app.route("/distancia")
def operasbas():

    return render_template("operacionD.html")

@app.route("/resultadoDis", methods=["post"])
def resultadoDis():
    x1=request.form.get("txtNum1")
    x2=request.form.get("txtNum2")
    y1=request.form.get("txtNum3")
    y2=request.form.get("txtNum4")

    operacion = math.sqrt(math.pow(int(x2)-int(x1),2) + math.pow(int(y2)-int(y1),2))

    return render_template("resultadoDis.html", x1=x1, x2=x2, y1=y1, y2=y2, operacion=operacion)

if __name__ == "__main__":
    app.run(debug=True, port=3000) 