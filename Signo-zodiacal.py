from flask import Flask, render_template
from flask import request 
from datetime import date


app = Flask(__name__)

@app.route("/examen")
def datos():
    return render_template("datosPersonales.html")

@app.route("/resultadosExamen", methods=["POST", "GET"])

def edad(dia, mes, anio):
    dia = request.form.get("txtDia")
    mes = request.form.get("txtMes")
    anio = request.form.get("txtAnio")
    hoy = date.hoy()
    return hoy.year - anio.year - ((hoy.month, hoy.day) < mes.month, dia.day)


def examen():
    respuesta = request.form.get("respuesta1", "respuesta2", "respuesta3", "respuesta4", "respuesta5")
    if respuesta1 == "b" and respuesta2 == "d" and respuesta3 == "d" and respuesta4 == "a" and respuesta5 == "a":
        res == 5    
    else:
        return render_template("resultadosExamen.html")

def resultadoExamen():
    nombre = request.form.get("txtNom")
    aPaterno = request.form.get("txtApaterno")
    aMaterno = request.form.get("txtAmaterno")
   # dia = request.form.get("txtDia")
    #mes = request.form.get("txtMes")
    #anio = request.form.get("txtAnio")
    
    if int (anio) == 1912 or int (anio) == 1924 or int (anio) == 1936 or int (anio) ==1948 or int (anio) == 1960 or int (anio) == 1972 or int (anio) == 1984 or int (anio) == 1960 or int (anio) == 1972 or int (anio) == 1984 or int (anio) == 1996 or int (anio) == 2008 or int (anio) == 2022:
        return res == "Tu signo zodiacal en el calendario Chino es RATA"

    elif int (anio) == 1913 or int (anio) == 1925 or int (anio) == 1937 or int (anio) == 1949 or int (anio) == 1961 or int (anio) == 1973 or int (anio) == 1985 or int (anio) == 1997 or int (anio) == 2009 or int (anio) == 2021:
        return res == "Tu signo zodiazal en el calendario Chino es BUEY"
    
    elif int (anio) == 1914 or int (anio) == 1926 or int (anio) == 1938 or int (anio) == 1950 or int (anio) == 1962 or int (anio) == 1974 or int (anio) == 1986 or int (anio) == 1998 or int (anio) == 2010 or int (anio) == 2022:
        return res == "Tu signo zodiazal en el calendario Chino es TIGRE"    
    
    elif int (anio) == 1915 or int (anio) == 1927 or int (anio) == 1939 or int (anio) == 1951 or int (anio) == 1963 or int (anio) == 1975 or int (anio) == 1987 or int (anio) == 1999 or int (anio) == 2011: 
        return res == "Tu signo zodiazal en el calendario Chino es CONEJO"
    
    elif int (anio) == 1916 or int (anio) == 1928 or int (anio) == 1940 or int (anio) == 1952 or int (anio) == 1964 or int (anio) == 1976 or int (anio) == 1988 or int (anio) == 2000 or int (anio) == 2012: 
        return res == "Tu signo zodiazal en el calendario Chino es DRAGÓN"

    elif int (anio) == 1917 or int (anio) == 1929 or int (anio) == 1941 or int (anio) == 1953 or int (anio) == 1965 or int (anio) == 1977 or int (anio) == 1989 or int (anio) == 2001 or int (anio) == 2013:
        return res == "Tu signo zodiazal en el calendario Chino es SERPIENTE"

    elif int (anio) == 1918 or int (anio) == 1930 or int (anio) == 1942 or int (anio) == 1954 or int (anio) == 1966 or int (anio) == 1978 or int (anio) == 1990 or int (anio) == 2002 or int (anio) == 2014:
        return res == "Tu signo zodiazal en el calendario Chino es CABALLO"

    elif int (anio) == 1919 or int (anio) == 1931 or int (anio) == 1943 or int (anio) == 1955 or int (anio) == 1967 or int (anio) == 1979 or int (anio) == 1991 or int (anio) == 2003 or int (anio) == 2015:
        return res == "Tu signo zodiazal en el calendario Chino es OVEJA"

    elif int (anio) == 1920 or int (anio) == 1932 or int (anio) == 1944 or int (anio) == 1956 or int (anio) == 1968 or int (anio) == 1980 or int (anio) == 1992 or int (anio) == 2004 or int (anio) == 2016:
        return res == "Tu signo zodiacal en el calendario Chino es MONO"

    elif int (anio) == 1921 or int (anio) == 1933 or int (anio) == 1945 or int (anio) == 1957 or int (anio) == 1969 or int (anio) == 1981 or int (anio) == 1993 or int (anio) == 2005 or int (anio) == 2017:
        return res == "Tu signo zodiacal en el calendario Chino es GALLO"

    elif int (anio) == 1922 or int (anio) == 1933 or int (anio) == 1945 or int (anio) == 1958 or int (anio) == 1970 or int (anio) == 1981 or int (anio) == 1993 or int (anio) == 2005 or int (anio) == 2018:
        return res == "Tu signo zodiacal en el calendario Chino es PERRO"

    elif int (anio) == 1923 or int (anio) == 1934 or int (anio) == 1946 or int (anio) == 1959 or int (anio) == 1971 or int (anio) == 1981 or int (anio) == 1994 or int (anio) == 2006 or int (anio) == 2019:
        return res == "Tu signo zodiacal en el calendario Chino es JABALÍ"

    else:
        return "NO TIENES SIGNO EN EL CALENDARIO CHINO :("



if __name__ == "__main__":  
    app.run(debug=True, port=3000) 
