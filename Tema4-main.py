from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/calculadora', methods=["GET","POST"])

def calculadora():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        ope = request.form.get("operacion")
        
        if ope == "suma":
            resultado = int(num1) + int(num2)
        elif ope == "resta":
            resultado = int(num1) - int(num2)
        elif ope == "multiplicacion":
            resultado = int(num1) * int(num2)
        elif ope == "division":
            if int(num2) != 0:
                resultado = int(num1) / int(num2)
        
        return "<h1>El resultado es: {}</h1>".format(resultado)
    else:
        return'''
            <form action="/calculadora" method="POST">
            <label>N1:</label>
            <input type="text" name="num1"/></br></br>
            <label>N2:</label>
            <input type="text" name="num2"/></br></br>
            <input type="radio" name="operacion" value="suma"> SUMA <br>
            <input type="radio" name="operacion" 
            value="resta"> RESTA <br>
            <input type="radio" name="operacion" value="multiplicacion"> MULTIPLICACIÓN <br>
            <input type="radio" name="operacion" value="division"> DIVISION <br>
            <input type="submit" value="Calcular"/>
            </form>
            '''

    
if __name__=="__main_":
    app.run(debug=True,port=8080)
