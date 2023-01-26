from flask import Flask

app =Flask(__name__)

@app.route("/")

def index():
    return "¡Hola Mundo! jjejejeejjejejejje"

if __name__ == "__main__":
    app.run(debug=True, port=8080) #con esto ya no es necesario reiniciar el server