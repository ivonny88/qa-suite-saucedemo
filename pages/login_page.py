from data.users import BASE_URL

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self) -> str:
        return self.page.inner_text(self.error_message)

    def is_error_visible(self) -> bool:
        return self.page.is_visible(self.error_message)