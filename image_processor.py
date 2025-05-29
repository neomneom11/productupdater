class ImageProcessor:
    def validate_image_url(self, url):
        return url.startswith("http")

    def download_image(self, url):
        return {"status": "success", "filename": url.split("/")[-1]}
