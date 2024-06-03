from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/connect', methods=['GET'])
def connect_to_database():
    password = "hardcodedpassword"
    # Supongamos que conectamos a la base de datos aquí
    return jsonify({"status": "connected", "password": password})

if __name__ == '__main__':
    app.run(debug=True)
