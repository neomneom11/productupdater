from flask import Flask, jsonify, request
from import_manager import ImportManager
from utils.logger import setup_logger

app = Flask(__name__)
logger = setup_logger()
import_manager = ImportManager()

@app.route('/')
def home():
    return "Product Importer API is running."

@app.route('/api/status')
def status():
    return jsonify(import_manager.get_status())

@app.route('/api/start-import', methods=['POST'])
def start_import():
    data = request.get_json()
    batch_size = data.get('batch_size', 10)
    category = data.get('category', '')
    return jsonify(import_manager.start_import(batch_size, category))

@app.route('/api/stop-import', methods=['POST'])
def stop_import():
    return jsonify(import_manager.stop_import())

@app.route('/api/logs')
def logs():
    return jsonify({"logs": import_manager.get_recent_logs()})

@app.route('/api/test-connections')
def test_connections():
    return jsonify(import_manager.test_api_connections())

@app.route('/api/template-analysis')
def template_analysis():
    return jsonify(import_manager.analyze_existing_templates())

if __name__ == '__main__':
    logger.info("Starting Product Import System")
    app.run(host='0.0.0.0', port=5000)
