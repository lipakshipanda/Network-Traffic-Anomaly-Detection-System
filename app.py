import os, pandas as pd, numpy as np, joblib, random, time, threading
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

# --- CONFIG & MODELS ---
MODEL_DIR = 'models'
rf = joblib.load(f'{MODEL_DIR}/rf.pkl')
scaler = joblib.load(f'{MODEL_DIR}/scaler.pkl')
feature_cols = joblib.load(f'{MODEL_DIR}/features.pkl')

live_packets = []
blocked_ips = set()

# --- NEW: DRIVER-FREE DATA GENERATOR ---
def traffic_generator():
    print("🚀 Hybrid Simulation Started (No Driver Needed)")
    protocols = ["TCP", "UDP", "HTTP", "ICMP", "DNS"]
    
    while True:
        # Create realistic-looking IP addresses
        src = f"192.168.1.{random.randint(2, 254)}"
        dst = f"10.0.0.{random.randint(1, 50)}"
        
        # Decide if this packet is a "normal" one or an "attack"
        # 80% chance of being normal traffic
        is_suspicious = random.random() < 0.2
        val_range = (10, 80) if is_suspicious else (0, 5)
        
        # Generate features for the AI model
        sim_features = {col: random.uniform(*val_range) for col in feature_cols}
        df_pkt = pd.DataFrame([sim_features])[feature_cols]
        
        # AI Prediction
        X = scaler.transform(df_pkt)
        prob = float(rf.predict_proba(X)[0][1])
        
        packet_info = {
            "timestamp": time.time(),
            "src_ip": src,
            "dst_ip": dst,
            "protocol": random.choice(protocols),
            "is_attack": prob > 0.5,
            "confidence": round(prob * 100, 2),
            "blocked": src in blocked_ips
        }
        
        # Update feed
        live_packets.insert(0, packet_info)
        if len(live_packets) > 50: live_packets.pop()
        
        # Simulate network delay (1 packet per second)
        time.sleep(1)

# Start the generator thread instead of Scapy
threading.Thread(target=traffic_generator, daemon=True).start()

# --- API ROUTES ---
@app.route('/')
def root(): return send_from_directory('static', 'index.html')

@app.route('/api/live')
def get_live(): return jsonify(live_packets)

@app.route('/api/block', methods=['POST'])
def block_ip():
    ip = request.json.get('ip')
    blocked_ips.add(ip)
    print(f"🚫 [SOFT BLOCK] IP {ip} added to filter list.")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)