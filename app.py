from flask import Flask, jsonify

app = Flask(__name__)

alumnos = [
    {"nombre": "Juan Perez", "matricula": "A01"},
    {"nombre": "Maria Lopez", "matricula": "A02"},
    {"nombre": "Carlos Sanchez", "matricula": "A03"},
    {"nombre": "Ana Garcia", "matricula": "A04"},
    {"nombre": "Luis Ramirez", "matricula": "A05"},
    {"nombre": "Sofia Torres", "matricula": "A06"},
    {"nombre": "Jorge Martinez", "matricula": "A07"},
    {"nombre": "Laura Diaz", "matricula": "A08"},
    {"nombre": "Pedro Ruiz", "matricula": "A09"},
    {"nombre": "Elena Gonzalez", "matricula": "A10"}
]

profesores = [
    {"nombre": "Dr. Alejandro Morales", "numeroEmpleado": "P01"},
    {"nombre": "Dra. Patricia Vargas", "numeroEmpleado": "P02"},
    {"nombre": "Dr. Roberto Jimenez", "numeroEmpleado": "P03"},
    {"nombre": "Dra. Carmen Ortega", "numeroEmpleado": "P04"},
    {"nombre": "Dr. Fernando Castro", "numeroEmpleado": "P05"},
    {"nombre": "Dra. Isabel Mendoza", "numeroEmpleado": "P06"},
    {"nombre": "Dr. Oscar Rios", "numeroEmpleado": "P07"},
    {"nombre": "Dra. Adriana Silva", "numeroEmpleado": "P08"},
    {"nombre": "Dr. Gabriel Rojas", "numeroEmpleado": "P09"},
    {"nombre": "Dra. Monica Paredes", "numeroEmpleado": "P010"}
]

@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    return jsonify(alumnos[:5])

@app.route('/profesores', methods=['GET'])
def obtener_profesores():
    return jsonify(profesores[:5])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)