import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_data = [item for item in csv_reader]

    with open(OUTPUT_FILENAME, 'w') as out_json:
        json.dump(csv_data, out_json, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
