from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status":"API Ardi Online", "owner":"ardi123-rgb"})

@app.route('/api/wifi/qr')
def wifi_qr():
    ssid = request.args.get('ssid','NYXORA')
    pw = request.args.get('pass','12345678')
    return jsonify({"qr_data": f"WIFI:T:WPA;S:{ssid};P:{pw};;"})

@app.route('/api/exp/stats')
def stats():
    return jsonify({"total_exp":182, "exp_rate":"513/h", "progress":"8.2% LVL 3-4"})
