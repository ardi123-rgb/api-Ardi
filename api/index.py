from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API Ardi Online", "message": "jalan bg"})

@app.route('/api/wifi/qr')
def wifi_qr():
    ssid = request.args.get('ssid', '')
    pw = request.args.get('password', '')
    return jsonify({"qr_data": f"WIFI:T:WPA;S:{ssid};P:{pw};;"})

@app.route('/api/exp/stats')
def stats():
    return jsonify({"total_pengeluaran": 185000, "pemasukan": 500000})

@app.route('/api/exp/transactions')
def transactions():
    return jsonify([])
