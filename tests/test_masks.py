from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_card_number():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"