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


def get_data(time_data_str: str ) -> str:
    time_data_list = time_data_str.split('T')
    data_list = str(time_data_list[0]).split("-")
    data_str = f"{data_list[2]}.{data_list[1]}.{data_list[0]}"
    return data_str

print(mask_account_card("Maestro 1596837868705199"))
print(get_data("2018-07-11T02:26:18.671407"))
