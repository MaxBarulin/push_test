import json


def get_info_transactions(path_file):
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    if type(path_file) is not str:
        return []

    try:
        with open(path_file, encoding="utf-8") as file:
            try:
                file_dict = json.load(file)

                if type(file_dict) is not list:
                    return []

                return file_dict

            except json.JSONDecodeError:
                return []

    except FileNotFoundError:
        return []


#print(get_info_transactions(1))
#print(get_info_transactions(""))
#print(get_info_transactions("../data/test.operations.json"))
