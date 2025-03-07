import json


def print_json(data, indent=0):
    """
    Рекурсивно выводит содержимое JSON в формате "ключ - значение".
    Вложенные структуры выводятся с отступом в виде табуляции.

    :param data: Данные JSON (словарь, список или значение).
    :param indent: Уровень отступа (по умолчанию 0).
    """
    if isinstance(data, dict):
        for key, value in data.items():
            print("\t" * indent + f"{key}: ", end="")
            if isinstance(value, (dict, list)):
                print()
                print_json(value, indent + 1)
            else:
                print(value)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print("\t" * indent + f"[{index}]: ", end="")
            if isinstance(item, (dict, list)):
                print()
                print_json(item, indent + 1)
            else:
                print(item)
    else:
        print("\t" * indent + str(data))


def load_and_print_json(file_path):
    """
    Загружает JSON из файла и выводит его содержимое.

    :param file_path: Путь к файлу JSON.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            print_json(data)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{file_path}' содержит некорректный JSON.")


if __name__ == "__main__":
    file_path = "example.json"

    example_data = {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zip": "10001"
        },
        "hobbies": ["reading", "traveling", "coding"]
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(example_data, file, indent=4)

    load_and_print_json(file_path)
