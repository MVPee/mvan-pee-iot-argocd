"""
IoT Custom Application - Version 1
Author: mvan-pee
Simple Flask web application that returns JSON responses
"""

from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def home():
    """Main endpoint - returns application info"""
    return jsonify({
        "status": "ok",
        "message": "v1",
        "pod": socket.gethostname(),
        "node": "K3d cluster"
    })

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Run on all interfaces, port 8888
    app.run(host='0.0.0.0', port=8888)
