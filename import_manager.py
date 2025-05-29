class ImportManager:
    def get_status(self):
        return {"status": "idle", "message": "No import running"}

    def start_import(self, batch_size=10, category=''):
        return {"success": True, "message": f"Started importing {batch_size} products from category '{category}'."}

    def stop_import(self):
        return {"success": True, "message": "Import stopped."}

    def get_recent_logs(self):
        return ["[INFO] Import started", "[INFO] Import running", "[INFO] Import finished"]

    def test_api_connections(self):
        return {"canopy": "connected", "wordpress": "connected"}

    def analyze_existing_templates(self):
        return {"templates_found": ["template-1", "template-2"], "count": 2}
