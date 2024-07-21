import logging

""" создаем логгер для логирования функций и пишем логи в директорию logs"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
logger = logging.getLogger("masks.py")


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
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
    logger.info("Маскировка карты клиента")
    return card_number_mask[:-1]


def get_mask_account(account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    account_mask = f"**{account[-4:]}"
    logger.info("Маскировка номера счёта клиента")
    return account_mask


if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))
    print(get_mask_account("73654108430135874305"))
