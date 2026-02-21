import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_add_one_product_to_cart(logged_in_page):
    """Añadir un producto al carrito actualiza el contador del carrito"""
    inventory = InventoryPage(logged_in_page)
    
    inventory.add_first_product_to_cart()
    
    assert inventory.get_cart_count() == 1, "El contador del carrito no es 1"


@pytest.mark.regression
def test_add_multiple_products_to_cart(logged_in_page):
    """Añadir varios productos actualiza el contador correctamente"""
    inventory = InventoryPage(logged_in_page)
    
    inventory.add_product_by_index(0)
    inventory.add_product_by_index(1)
    inventory.add_product_by_index(2)
    
    assert inventory.get_cart_count() == 3, "El contador del carrito no es 3"


@pytest.mark.regression
def test_cart_shows_correct_product(logged_in_page):
    """El producto añadido aparece correctamente en el carrito"""
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    
    product_names = inventory.get_product_names()
    first_product = product_names[0]
    
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()
    
    cart_items = cart.get_item_names()
    assert first_product in cart_items, f"El producto '{first_product}' no aparece en el carrito"


@pytest.mark.regression
def test_remove_product_from_cart(logged_in_page):
    """Eliminar un producto del carrito lo quita correctamente"""
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()
    
    assert cart.get_items_count() == 1, "El carrito debería tener 1 producto"
    
    cart.remove_first_item()
    
    assert cart.is_empty(), "El carrito debería estar vacío tras eliminar el producto"


@pytest.mark.negative
def test_cart_empty_by_default(logged_in_page):
    """El carrito está vacío al entrar sin añadir productos"""
    inventory = InventoryPage(logged_in_page)
    
    inventory.go_to_cart()
    
    cart = CartPage(logged_in_page)
    assert cart.is_empty(), "El carrito debería estar vacío por defecto"