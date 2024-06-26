import pytest
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "x, y",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Mastercard 8990922113665229", "Mastercard 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 73654108430135874416", "Счет **4416"),
    ],
)
def test_mask_account_card(x, y):
    assert mask_account_card(x) == y


def test_get_data():
    assert get_data("2018-07-11T02:26:18.671407") == "11.07.2018"
