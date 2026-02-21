class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = ".title"
        self.inventory_items = ".inventory_item"
        self.sort_dropdown = ".product_sort_container"
        self.add_to_cart_buttons = ".btn_inventory"
        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.title)

    def get_page_title(self) -> str:
        return self.page.inner_text(self.title)

    def get_products_count(self) -> int:
        return self.page.locator(self.inventory_items).count()

    def sort_by(self, option: str):
        self.page.select_option(self.sort_dropdown, option)

    def get_product_names(self) -> list:
        items = self.page.locator(".inventory_item_name").all()
        return [item.inner_text() for item in items]

    def get_product_prices(self) -> list:
        items = self.page.locator(".inventory_item_price").all()
        return [float(item.inner_text().replace("$", "")) for item in items]

    def add_first_product_to_cart(self):
        self.page.locator(self.add_to_cart_buttons).first.click()

    def add_product_by_index(self, index: int):
        self.page.locator(self.add_to_cart_buttons).nth(index).click()

    def get_cart_count(self) -> int:
        if self.page.is_visible(self.cart_badge):
            return int(self.page.inner_text(self.cart_badge))
        return 0

    def go_to_cart(self):
        self.page.click(self.cart_icon)
        