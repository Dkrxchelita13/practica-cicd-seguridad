from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({
        "estado": "exitoso",
        "mensaje": "¡Bienvenido a la API de nuestra práctica de CI/CD!"
    })

# Un endpoint que luego podremos asegurar en la Parte D
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify({
        "mensaje": f"Hola, {nombre}."
    })

if __name__ == '__main__':
    # debug=True ayuda a ver errores mientras desarrollan, pero luego lo quitaremos por seguridad
    app.run(host='0.0.0.0', port=5000, debug=True)
