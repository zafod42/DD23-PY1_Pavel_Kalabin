import json


def task() -> float:
    filename = "input.json"
    with open(filename) as json_file:
        data = json.load(json_file)

    products_sum = sum([item["score"]*item["weight"] for item in data])
    return round(products_sum, 3)


print(task())
