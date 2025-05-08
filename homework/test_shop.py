import pytest
from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # Покупка всех доступных товаров
        assert product.check_quantity(1000) == True

        # Покупка большего количества товаров
        assert product.check_quantity(1001) == False

        # Покупка меньшего количества товаров
        assert product.check_quantity(999) == True


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(200)
        assert product.quantity == 800


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as exception:
            product.buy(1001)
        print(exception.value)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_cart_add_products(self, cart, product):
        # Добавление товаров в пустую корзину
        cart.add_product(product, 5)
        assert cart.products[product] == 5

        # Увеличение количества товаров в корзине
        cart.add_product(product=product, buy_count=3)
        assert cart.products[product] == 8

    def test_negative_cart_add_products(self, cart, product):
        # Добавление некорректного количества товаров
        with pytest.raises(ValueError) as exception:
            cart.add_product(product=product, buy_count = -1)

        print(exception.value)

    def test_cart_remove_product(self, cart, product):
        # Удаление части товаров из корзины
        cart.add_product(product, 10)
        cart.remove_product(product, 2)
        assert cart.products[product] == 8

        # Удаление всех товаров из корзины
        cart.add_product(product, 1000)
        cart.remove_product(product)
        assert cart.products == {}

        # Удаление нулевого количества товаров
        cart.add_product(product, 1)
        cart.remove_product(product, 0)
        assert cart.products[product] == 1

        # Удаление большего количества товаров
        cart.add_product(product, 5)
        cart.remove_product(product, 10)
        assert cart.products == {}

        # Удаление такого же количества товаров, как в корзине
        cart.add_product(product, 7)
        cart.remove_product(product, 7)
        assert cart.products == {}

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 25)
        cart.clear()
        assert cart.products == {}

    def test_total_price(self, cart, product):
        cart.add_product(product, 4)
        total_price = cart.get_total_price()
        expected_total = product.price * 4
        assert total_price == expected_total
        print(f"Итоговая цена {total_price}.")

    def test_cart_buy_available_items(self, cart, product):
        #Покупка доступного количества товаров
        cart.add_product(product, 3)
        cart.buy()
        assert cart.products == {}

    def test_cart_buy_unavailable_items(self, cart, product):
        #Покупка недоступного количества товаров
        product.quantity = 800
        cart.add_product(product, 801)
        with pytest.raises(ValueError) as exception:
            cart.buy()
        print(exception.value)
        assert cart.products[product] == 801
        assert product.quantity == 800












