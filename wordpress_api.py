class WordPressAPI:
    def test_connection(self):
        return {"status": "success", "message": "WordPress API mock connected"}

    def get_existing_pages(self):
        return [{"id": 1, "title": "Sample Page"}]

    def upload_image(self, url, filename):
        return {"url": f"https://mock.wordpress.com/images/{filename}"}

    def create_product_page(self, product, template_structure):
        return {
            "url": f"https://mock.wordpress.com/{product['name'].replace(' ', '-').lower()}"
        }
