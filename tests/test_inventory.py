import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_inventory_page_loads(logged_in_page):
    """La página de inventario carga correctamente con productos"""
    inventory = InventoryPage(logged_in_page)

    assert inventory.is_loaded(), "La página de inventario no cargó"
    assert inventory.get_products_count() == 6, "Deberían mostrarse 6 productos"


@pytest.mark.regression
def test_sort_by_name_ascending(logged_in_page):
    """Ordenar por nombre A-Z ordena los productos correctamente"""
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("az")
    names = inventory.get_product_names()

    assert names == sorted(names), "Los productos no están ordenados de A a Z"


@pytest.mark.regression
def test_sort_by_name_descending(logged_in_page):
    """Ordenar por nombre Z-A ordena los productos correctamente"""
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("za")
    names = inventory.get_product_names()

    assert names == sorted(names, reverse=True), "Los productos no están ordenados de Z a A"


@pytest.mark.regression
def test_sort_by_price_ascending(logged_in_page):
    """Ordenar por precio de menor a mayor funciona correctamente"""
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("lohi")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices), "Los productos no están ordenados por precio ascendente"


@pytest.mark.regression
def test_sort_by_price_descending(logged_in_page):
    """Ordenar por precio de mayor a menor funciona correctamente"""
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("hilo")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices, reverse=True), "Los productos no están ordenados por precio descendente"

    