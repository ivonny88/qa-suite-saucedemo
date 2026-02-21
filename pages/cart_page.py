class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = ".cart_item"
        self.checkout_button = "[data-test='checkout']"
        self.continue_shopping_button = "[data-test='continue-shopping']"
        self.item_names = ".inventory_item_name"
        self.item_prices = ".inventory_item_price"
        self.remove_buttons = ".cart_button"

    def get_items_count(self) -> int:
        return self.page.locator(self.cart_items).count()

    def get_item_names(self) -> list:
        items = self.page.locator(self.item_names).all()
        return [item.inner_text() for item in items]

    def get_item_prices(self) -> list:
        prices = self.page.locator(self.item_prices).all()
        return [price.inner_text() for price in prices]

    def remove_first_item(self):
        self.page.locator(self.remove_buttons).first.click()

    def go_to_checkout(self):
        self.page.click(self.checkout_button)

    def continue_shopping(self):
        self.page.click(self.continue_shopping_button)

    def is_empty(self) -> bool:
        return self.page.locator(self.cart_items).count() == 0