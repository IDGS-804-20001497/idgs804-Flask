from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
        return render_template("index.html")

@app.route("/alumnos")
def alumnos():
        return render_template("alumnos.html")

@app.route("/usuarios")
def usuarios():
        return render_template("usuarios.html")

def index():
    return "¡Hola Mundo!"

if __name__ == "__main__":
    app.run(debug=True, port=3000) 