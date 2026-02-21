import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.users import STANDARD_USER, LOCKED_USER, INVALID_USER


@pytest.mark.smoke
def test_login_standard_user(page):
    """Usuario estándar puede hacer login correctamente"""
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login(STANDARD_USER["username"], STANDARD_USER["password"])

    assert inventory.is_loaded(), "La página de inventario no cargó tras el login"
    assert inventory.get_page_title() == "Products"


@pytest.mark.negative
def test_login_locked_user(page):
    """Usuario bloqueado ve mensaje de error al intentar login"""
    login = LoginPage(page)

    login.open()
    login.login(LOCKED_USER["username"], LOCKED_USER["password"])

    assert login.is_error_visible(), "El mensaje de error no aparece"
    assert "locked out" in login.get_error_message().lower()


@pytest.mark.negative
def test_login_invalid_credentials(page):
    """Credenciales incorrectas muestran mensaje de error"""
    login = LoginPage(page)

    login.open()
    login.login(INVALID_USER["username"], INVALID_USER["password"])

    assert login.is_error_visible(), "El mensaje de error no aparece"
    assert "username and password do not match" in login.get_error_message().lower()


@pytest.mark.negative
def test_login_empty_credentials(page):
    """Login con campos vacíos muestra error"""
    login = LoginPage(page)

    login.open()
    login.login("", "")

    assert login.is_error_visible(), "El mensaje de error no aparece"
    assert "username is required" in login.get_error_message().lower()


@pytest.mark.regression
def test_logout(logged_in_page):
    """Usuario puede hacer logout correctamente"""
    logged_in_page.click("[id='react-burger-menu-btn']")
    logged_in_page.click("[id='logout_sidebar_link']")

    login = LoginPage(logged_in_page)
    assert logged_in_page.is_visible("#login-button"), "El botón de login no aparece tras logout"