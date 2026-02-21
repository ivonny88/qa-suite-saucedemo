class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.postal_code_input = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.finish_button = "[data-test='finish']"
        self.confirmation_header = ".complete-header"
        self.confirmation_text = ".complete-text"
        self.error_message = "[data-test='error']"
        self.summary_total = ".summary_total_label"

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)

    def click_continue(self):
        self.page.click(self.continue_button)

    def click_finish(self):
        self.page.click(self.finish_button)

    def get_confirmation_header(self) -> str:
        return self.page.inner_text(self.confirmation_header)

    def get_total(self) -> str:
        return self.page.inner_text(self.summary_total)

    def is_order_complete(self) -> bool:
        return self.page.is_visible(self.confirmation_header)

    def get_error_message(self) -> str:
        return self.page.inner_text(self.error_message)

    def is_error_visible(self) -> bool:
        return self.page.is_visible(self.error_message)