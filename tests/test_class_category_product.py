import pytest

from src.class_category_product import Category, Product


@pytest.fixture
def product():
    return [Product("Яблоко", "Россия", 49.90, 400),
            Product("Мандарин", "Азербайджан", 90.85, 5300)]


@pytest.fixture
def category(product):
    return Category("Фрукты", "Производитель", product)


def test__init(category, product):
    assert category.name == "Фрукты"
    assert category.description == "Производитель"
    assert category.product == product


def test_category(category, product):
    assert Category.total_category == 2


def test_product(category, product):
    assert Category.total_unique_products == 6


@pytest.fixture
def product_1():
    return Product("Арбуз", "Грузия", 300.0, 50)


def test_product_init(product_1):
    assert product_1.name == "Арбуз"
    assert product_1.description == "Грузия"
    assert product_1.price == 300.0
    assert product_1.quantity == 50
