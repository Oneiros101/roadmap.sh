import json
import pathlib

from prettytable import PrettyTable

EXPENSES_JSON = "expenses.json"


def clear_json(json_file_name: str):
    open(json_file_name, "w").close()


def write_to_json(expense: list[dict], json_file_name: str, mode: str):
    with open(json_file_name, mode) as file:
        json.dump(expense, file, indent=4)
        file.write("\n")


def read_json(json_file_name: str):
    if not pathlib.Path(json_file_name):
        raise FileNotFoundError("expenses.json does not exist.")
    else:
        with open(json_file_name, "r") as file:
            return json.load(file)


def display_json(category: str | None, month: str | None):
    json_data = read_json(EXPENSES_JSON)
    if not json_data:
        print("No expenses found.")
    else:
        table = PrettyTable()
        if category:
            # Define field names
            table.field_names = [
                "id",
                "date",
                "description",
                "amount",
                "category",
            ]
            for expense in json_data:
                if expense["category"].lower() == category.lower():
                    table.add_row(
                        [
                            expense["id"],
                            expense["date"],
                            expense["description"],
                            expense["amount"],
                            expense["category"],
                        ],
                        divider=True,
                    )
            if not table.rows:
                print(f"\nNo expenses were found for category '{category}'\n")
            else:
                print(table)

        elif month:
            # Define field names
            table.field_names = [
                "id",
                "date",
                "description",
                "amount",
                "category",
            ]
            for expense in json_data:
                if expense["date"].split("-")[1][-1] == month:
                    table.add_row(
                        [
                            expense["id"],
                            expense["date"],
                            expense["description"],
                            expense["amount"],
                            expense["category"],
                        ],
                        divider=True,
                    )
            if not table.rows:
                print(f"\nNo expenses were found for month '{month}'\n")
            else:
                print(table)

        else:
            # Define field names
            table.field_names = [
                "id",
                "date",
                "description",
                "amount",
                "category",
            ]
            for expense in json_data:
                table.add_row(
                    [
                        expense["id"],
                        expense["date"],
                        expense["description"],
                        expense["amount"],
                        expense["category"],
                    ],
                    divider=True,
                )
            print(table)
