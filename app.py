from flask import Flask, jsonify, abort
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({
        "estado": "exitoso",
        "mensaje": "¡Bienvenido a la API de nuestra práctica de CI/CD!"
    })

@app.route('/saludo/<nombre>')
def saludo(nombre):
    # 1. Validación de entrada (control de tamaño)
    if len(nombre) > 20:
        abort(400, description="El nombre ingresado es demasiado largo.")
    
    # 2. Sanitización de datos (evita inyección de scripts HTML/JS)
    nombre_seguro = escape(nombre)
    
    return jsonify({
        "mensaje": f"Adios, {nombre_seguro}."
    })

if __name__ == '__main__':
    # Apagamos el modo debug por seguridad en un entorno real
    app.run(host='0.0.0.0', port=5000, debug=False)
