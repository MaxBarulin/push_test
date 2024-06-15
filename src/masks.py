def get_mask_card_number(card_number: str) -> str:
    count = 1
    list_cart_number = list(card_number)
    a = []
    for j in range(6, 12):
        list_cart_number[j] = "*"

    for i in list_cart_number:
        a.append(i)
        if count == 4:
            a.append("y")
            count = 0
        count += 1
    card_number_mask = "".join(a).replace("y", " ")
    return card_number_mask


def get_mask_account(account: str) -> str:
    account_mask = f"**{account[:4]}"
    return account_mask


print(get_mask_card_number("1234567812345678"))

print(get_mask_account("73654108430135874305"))
