import pathlib
import pandas

from datetime import datetime
from expense_management.json_manager import (
    clear_json,
    write_to_json,
    read_json,
    display_json,
)

EXPENSES_JSON = "expenses.json"
time_now = datetime.today().strftime("%Y-%m-%d")


def add_expense(expense_description: str, amount: str, category: str):
    expense_id = 1
    expense = [
        {
            "id": expense_id,
            "date": time_now,
            "description": expense_description,
            "amount": f"${amount}",
            "category": category,
        }
    ]
    if not pathlib.Path(EXPENSES_JSON).exists():
        write_to_json(expense, EXPENSES_JSON, "w")
        print(
            f'Expense {expense_id} "{expense_description}" with amount {amount} has been added successfully.'
        )
    else:
        expenses_data: list[dict] = read_json(EXPENSES_JSON)

        # Clearing json file
        clear_json(EXPENSES_JSON)

        last_id = (
            max(expense["id"] for expense in expenses_data) if expenses_data else 0
        ) + 1

        new_expense = {
            "id": last_id,
            "date": time_now,
            "description": expense_description,
            "amount": f"${amount}",
            "category": category,
        }
        expenses_data.append(new_expense)
        write_to_json(expenses_data, EXPENSES_JSON, "a")
        print(
            f'Expense {last_id} "{expense_description}" with amount {amount} has been added successfully.'
        )


def update_expense(
    expense_id: int,
    new_expense_description: str,
    new_expense_amount: str,
    category: str | None,
):
    if not pathlib.Path(EXPENSES_JSON):
        raise FileNotFoundError(f"{EXPENSES_JSON} does not exist.")
    else:
        expenses_data: list[dict] = read_json(EXPENSES_JSON)
        expense_found = False
        for expense in expenses_data:
            if expense["id"] == expense_id:
                expense_found = True
                if not category:
                    expense["description"] = new_expense_description
                    expense["amount"] = f"${new_expense_amount}"
                else:
                    expense["category"] = category

        if expense_found:
            # Clearing json file
            clear_json(EXPENSES_JSON)
            write_to_json(expenses_data, EXPENSES_JSON, "w")
            print(f"\nExpense {expense_id} has been updated successfully.\n")
        else:
            print(f"\nExpense {expense_id} not found.\n")


def delete_expense(expense_id: int):
    if not pathlib.Path(EXPENSES_JSON):
        raise FileNotFoundError(f"{EXPENSES_JSON} does not exist.")
    else:
        expenses_data: list[dict] = read_json(EXPENSES_JSON)
        expense_found = False
        for expense in expenses_data:
            if expense["id"] == expense_id:
                expense_found = True
                expenses_data.remove(expense)

        if expense_found:
            # Clearing json file
            clear_json(EXPENSES_JSON)
            write_to_json(expenses_data, EXPENSES_JSON, "w")
            print(f"\nExpense {expense_id} has been deleted successfully.\n")
        else:
            print(f"\nExpense {expense_id} not found.\n")


def sum_expense_values(month: str | None):
    if not pathlib.Path(EXPENSES_JSON):
        raise FileNotFoundError(f"{EXPENSES_JSON} does not exist.")
    else:
        if month is None:
            expenses_data: list[dict] = read_json(EXPENSES_JSON)
            month_amount_list = []
            for expense in expenses_data:
                month_amount_list.append(int(expense["amount"][1:]))

            if not month_amount_list:
                print(f"\nNo expenses found for month '{month}'\n")
            else:
                print(
                    f"\nTotal expenses of month {month}: ${sum(month_amount_list):,}\n"
                )
        else:
            expense_data: list[dict] = read_json(EXPENSES_JSON)
            month_amount_list = []
            for expense in expense_data:
                if int(expense["date"].split("-")[1]) == int(month):
                    month_amount_list.append(int(expense["amount"][1:]))   # Skipping the '$' in the string

            if not month_amount_list:
                print(f"\nNo expenses found for month '{month}'.\n")
            else:
                print(
                    f"\nTotal expenses of month {month}: ${sum(month_amount_list):,}\n"
                )


def list_expenses(category: str | None, month: str | None):
    display_json(category, month)


def export_to_csv(json_file: str, csv_file: str):
    with open(EXPENSES_JSON, encoding="utf-8") as file:
        data_file = pandas.read_json(json_file)

    data_file.to_csv(csv_file, encoding="utf-8", index=False)
    print(f"\n'{json_file}' has been successfully exported to '{csv_file}'\n")
