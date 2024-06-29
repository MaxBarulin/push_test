import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_list, transactions_list_res):
    assert list(filter_by_currency(transactions_list, "USD")) == transactions_list_res


def test_transaction_descriptions(transactions_list):
    assert list(transaction_descriptions(transactions_list)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "x, y, z",
    [
        (1, 3, ["0000000000000001", "0000000000000002", "0000000000000003"]),
        (10, 11, ["0000000000000010", "0000000000000011"]),
        (9999999999999991, 9999999999999993, ["9999999999999991", "9999999999999992", "9999999999999993"]),
        (1568000000000000, 1568000000000002, ["1568000000000000", "1568000000000001", "1568000000000002"]),
    ],
)
def test_card_number_generator(x, y, z):
    assert card_number_generator(x, y) == z
