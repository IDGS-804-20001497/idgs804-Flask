from flask import Flask

app =Flask(__name__)

@app.route("/")

def index():
    return "¡Hola Mundo! jjejejeejjejejejje"

#pasamos un  string
@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user

#pasamos parametros int
@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {} ".format(n)

#pasamos mas de un parametro
@app.route("/user/<int:id>/<string:username>")
def usern(id, username):
    return "ID: {} Nombre: {}".format(id, username)

if __name__ == "__main__":
    app.run(debug=True, port=8080)