from config import Config

class PriceCalculator:
    def calculate_marked_up_price(self, original_price, currency="USD"):
        try:
            marked_up = round(original_price * (1 + Config.MARKUP_PERCENTAGE / 100), 2)
            return {"marked_up_price": marked_up}
        except Exception as e:
            return {"error": str(e)}
