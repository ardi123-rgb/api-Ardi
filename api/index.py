from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "aktif", "message": "API Ardi jalan!", "creator": "ardi123-rgb"})

@app.route('/api/halo')
def halo():
    return jsonify({"pesan": "Halo dari api-Ardi"})
