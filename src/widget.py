from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_num_or_acc: str) -> str:
    digit = []
    if "Счет" in card_num_or_acc:
        for i in card_num_or_acc:
            if i.isdigit():
                digit.append(i)
            else:
                continue

        accuont_digit = "".join(digit)
        res = get_mask_account(accuont_digit)
        full_res = f"Счет {res}"

    else:
        card_name = card_num_or_acc[:-16].replace(" ", "")
        card_digit = card_num_or_acc[-16:]
        res = get_mask_card_number(card_digit)
        full_res = f"{card_name} {res}"

    return full_res


print(mask_account_card("Maestro 1596837868705199"))
