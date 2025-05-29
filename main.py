import os
import subprocess
import sys
from flask import Flask, render_template, jsonify, request
from import_manager import ImportManager
from utils.logger import setup_logger

app = Flask(__name__)
logger = setup_logger()
import_manager = ImportManager()

@app.route('/')
def dashboard():
    return "Product Import System is running."

@app.route('/api/status')
def get_status():
    try:
        status = import_manager.get_status()
        return jsonify(status)
    except Exception as e:
        logger.error(f"Error getting status: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/start-import', methods=['POST'])
def start_import():
    try:
        data = request.get_json()
        batch_size = data.get('batch_size', 10)
        category = data.get('category', '')
        result = import_manager.start_import(batch_size=batch_size, category=category)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error starting import: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/stop-import', methods=['POST'])
def stop_import():
    try:
        result = import_manager.stop_import()
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error stopping import: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/logs')
def get_logs():
    try:
        logs = import_manager.get_recent_logs()
        return jsonify({"logs": logs})
    except Exception as e:
        logger.error(f"Error getting logs: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/test-connections')
def test_connections():
    try:
        results = import_manager.test_api_connections()
        return jsonify(results)
    except Exception as e:
        logger.error(f"Error testing connections: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/template-analysis')
def analyze_templates():
    try:
        analysis = import_manager.analyze_existing_templates()
        return jsonify(analysis)
    except Exception as e:
        logger.error(f"Error analyzing templates: {str(e)}")
        return jsonify({"error": str(e)}), 500

def ensure_dependencies():
    try:
        import flask, requests, PIL, bs4, trafilatura
    except ImportError:
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet",
                               "flask", "requests", "pillow", "beautifulsoup4", "trafilatura"])

if __name__ == '__main__':
    ensure_dependencies()
    logger.info("Starting Product Import System")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
