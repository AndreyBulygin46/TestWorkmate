import pytest
from csv_proc import filter_data, aggregate_data

# Фиктивный набор данных для тестирования
sample_data = [
    {'id': '1', 'brand': 'Samsung', 'model': 'Galaxy S21', 'price': '899'},
    {'id': '2', 'brand': 'Xiaomi', 'model': 'Redmi Note 10', 'price': '299'},
    {'id': '3', 'brand': 'Apple', 'model': 'iPhone 13 Pro Max', 'price': '1299'}
]

# Тестовые функции для filter_data


def test_filter_more_price():
    result = filter_data(sample_data, 'price', '>', '800')
    # Должны остаться Samsung Galaxy S21 и Apple iPhone 13 Pro Max
    assert len(result) == 2
    assert all(float(item['price']) > 800 for item in result)


def test_filter_less_price():
    result = filter_data(sample_data, 'price', '<', '500')
    assert len(result) == 1  # Остался Xiaomi Redmi Note 10
    assert float(result[0]['price']) < 500


def test_filter_equality_price():
    result = filter_data(sample_data, 'price', '=', '899')
    assert len(result) == 1  # Оставлен только Samsung Galaxy S21
    assert float(result[0]['price']) == 899


def test_no_matches():
    result = filter_data(sample_data, 'price', '>', '1500')
    assert len(result) == 0  # Нет устройств дороже 1500$

# Тестовая функция для aggregate_data


def test_avg():
    result = aggregate_data(sample_data, 'price', 'avg')
    expected_average = (899 + 299 + 1299) / 3
    # Среднее значение близко к ожиданию
    assert abs(result - expected_average) < 0.01


def test_min():
    result = aggregate_data(sample_data, 'price', 'min')
    assert result == 299  # Минимальная цена


def test_max():
    result = aggregate_data(sample_data, 'price', 'max')
    assert result == 1299  # Максимальная цена


def test_empty_data():
    empty_data = []
    result = aggregate_data(empty_data, 'price', 'avg')
    assert result is None  # Агрегация пустой выборки не имеет смысла


pytest.main()
