from typing import Generator, Union

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]:
    """Функция возвращает операции в которых указана валюта"""
    res = (i for i in transactions if i["operationAmount"]["currency"]["code"] == currency)
    return res


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, None, None]:
    """Функция возвращает описание каждой операции по очереди"""
    res = (i["description"] for i in transactions)
    return res


def card_number_generator(x: Union[int], y: Union[int]) -> list:
    """Функция гунерирует номер карты в заданном диапозоне"""
    string_zero = "0000000000000000"
    len_string_zero = len(string_zero)
    # print(len_string_zero)
    res = [num_card for num_card in range(x, y + 1)]
    a = []
    for i in res:
        len_gen_num = len(str(i))
        len_zero_adding = len_string_zero - len_gen_num
        card_gen_num = f'{"0" * int(len_zero_adding) + str(i)}'
        four_digit_groups = [card_gen_num[i : i + 4] for i in range(0, len(card_gen_num), 4)]
        a.append("".join(four_digit_groups))
    return a


usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions))

descriptions = transaction_descriptions(transactions)

for _ in range(5):
    print(next(descriptions))

for card_number in card_number_generator(20, 27):
    print(card_number)
