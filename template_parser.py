class TemplateParser:
    def analyze_page_templates(self, pages):
        return {
            "template_structure": {
                "title": "<h1>{product_name}</h1>",
                "price": "<p>${price}</p>"
            },
            "sample_count": len(pages)
        }
