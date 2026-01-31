"""
IoT Custom Application - Version 2
Author: mvan-pee
Enhanced Flask web application with additional features
"""

from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Main endpoint - returns application info with timestamp"""
    return jsonify({
        "status": "ok",
        "message": "v2",  # Updated version
        "pod": socket.gethostname(),
        "node": "K3d cluster",
        "timestamp": datetime.datetime.now().isoformat()  # New feature
    })

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({"status": "healthy"}), 200

@app.route('/info')  # New endpoint in v2
def info():
    """Information endpoint - returns version and metadata"""
    return jsonify({
        "version": "2.0",
        "author": "mvan-pee",
        "project": "Inception-of-Things",
        "description": "Custom application for Part 3"
    })

if __name__ == '__main__':
    # Run on all interfaces, port 8888
    app.run(host='0.0.0.0', port=8888)
