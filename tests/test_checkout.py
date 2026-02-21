import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_complete_purchase(logged_in_page):
    """Flujo completo de compra desde añadir producto hasta confirmación"""
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    # Añadir producto al carrito
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    # Ir a checkout
    cart.go_to_checkout()

    # Rellenar datos del cliente
    checkout.fill_customer_info("Fatima", "Ocaña", "28001")
    checkout.click_continue()

    # Confirmar pedido
    checkout.click_finish()

    assert checkout.is_order_complete(), "La confirmación de pedido no aparece"
    assert "Thank you" in checkout.get_confirmation_header()


@pytest.mark.regression
def test_checkout_shows_correct_total(logged_in_page):
    """El resumen de checkout muestra el total del pedido"""
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()
    cart.go_to_checkout()

    checkout.fill_customer_info("Fatima", "Ocaña", "28001")
    checkout.click_continue()

    total = checkout.get_total()
    assert "Total:" in total, "El total del pedido no aparece en el resumen"


@pytest.mark.negative
def test_checkout_empty_first_name(logged_in_page):
    """Checkout sin nombre muestra error de validación"""
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()
    cart.go_to_checkout()

    checkout.fill_customer_info("", "Ocaña", "28001")
    checkout.click_continue()

    assert checkout.is_error_visible(), "El error de validación no aparece"
    assert "First Name is required" in checkout.get_error_message()


@pytest.mark.negative
def test_checkout_empty_postal_code(logged_in_page):
    """Checkout sin código postal muestra error de validación"""
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()
    cart.go_to_checkout()

    checkout.fill_customer_info("Fatima", "Ocaña", "")
    checkout.click_continue()

    assert checkout.is_error_visible(), "El error de validación no aparece"
    assert "Postal Code is required" in checkout.get_error_message()


@pytest.mark.regression
def test_checkout_multiple_products(logged_in_page):
    """Checkout con varios productos completa la compra correctamente"""
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_product_by_index(0)
    inventory.add_product_by_index(1)
    inventory.go_to_cart()

    assert cart.get_items_count() == 2, "El carrito debería tener 2 productos"

    cart.go_to_checkout()
    checkout.fill_customer_info("Fatima", "Ocaña", "28001")
    checkout.click_continue()
    checkout.click_finish()

    assert checkout.is_order_complete(), "La confirmación de pedido no aparece"