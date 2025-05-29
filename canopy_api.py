class CanopyAPI:
    def test_connection(self):
        return {"status": "success", "message": "Canopy API mock connected"}

    def get_products(self, category="", limit=10):
        return [
            {
                "name": f"Mock Product {i+1}",
                "original_price": 19.99 + i,
                "currency": "USD",
                "image_url": "https://via.placeholder.com/300",
            }
            for i in range(limit)
        ]
