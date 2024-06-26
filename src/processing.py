def filter_by_state(items: list, state: str = "EXECUTED") -> list:
    """Фильтрует список словарей по ключу 'state'."""

    return [item for item in items if item["state"] == state]


def sort_by_date(items: list, reverse: bool = True) -> list:
    """Сортирует список словарей по ключу 'date'."""

    return sorted(items, key=lambda x: x["date"], reverse=reverse)


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    filtered_executed = filter_by_state(input_data)
    print(filtered_executed)

    sorted_descending = sort_by_date(input_data, True)
    print(sorted_descending)
