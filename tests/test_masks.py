import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card


def test_get_mask_account(mask_account):
    assert get_mask_account(mask_account) == "**4305"


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"


@pytest.mark.parametrize("x, y", [("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                  ("Mastercard 8990922113665229", "Mastercard 8990 92** **** 5229"),
                                  ("Счет 73654108430135874305", "Счет **4305"),
                                  ("Счет 73654108430135874416", "Счет **4416")])
def test_mask_account_card(x, y):
    assert mask_account_card(x) == y
