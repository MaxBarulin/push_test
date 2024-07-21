from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account(mask_account):
    assert get_mask_account(mask_account) == "**4305"


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"
