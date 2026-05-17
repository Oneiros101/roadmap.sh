import argparse

from expense_management.expense_manager import (
    add_expense,
    update_expense,
    delete_expense,
    sum_expense_values,
    list_expenses,
    export_to_csv,
)


def main():
    PROG = "Expense Tracker"
    DESCRIPTION = (
        "A CLI tool to manage expenses by adding, updating, deleting, summarizing expense entries and "
        "exporting json file to csv file"
    )
    USAGE = "python expense_tracker_cli.py COMMAND [OPTIONS] [ARGS]..."

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage=USAGE,
        prog=PROG,
        description=DESCRIPTION,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="add an expense entry")
    add_parser.add_argument(
        "--description", type=str, required=True, help="add expense's description"
    )
    add_parser.add_argument(
        "--amount", type=str, required=True, help="add expense's amount"
    )
    add_parser.add_argument(
        "--category",
        type=str,
        required=True,
        help="place expense in a certain category",
    )

    update_parser = subparsers.add_parser(
        "update", help="update an existing expense entry"
    )
    update_parser.add_argument(
        "--id", type=int, required=True, help="id of the expense to be updated"
    )
    update_parser.add_argument(
        "--description",
        type=str,
        required=True,
        help="update existing expense's description",
    )
    update_parser.add_argument(
        "--amount", type=str, required=True, help="update existing expense's amount"
    )
    update_parser.add_argument(
        "--category", type=str, help="update existing expense's category"
    )

    delete_parser = subparsers.add_parser("delete", help="delete an expense entry")
    delete_parser.add_argument(
        "--id", type=int, required=True, help="id of expense to be deleted"
    )

    summary_parser = subparsers.add_parser(
        "summary", help="summarize expense entries (sum)"
    )
    summary_parser.add_argument("--month", type=str, help="specify a month for summary")

    list_parser = subparsers.add_parser("list", help="display expenses")
    list_parser.add_argument(
        "--category",
        type=str,
        help="list one or several categories",
    )
    list_parser.add_argument("--month", type=str, help="specify a month for summary")

    export_parser = subparsers.add_parser(
        "export", help="export json file to designated type"
    )
    export_parser.add_argument(
        "--json-file",
        type=str,
        required=True,
        help="the file you wish to export to a different type",
    )
    export_parser.add_argument(
        "--to-csv", type=str, required=True, help="exports json file to csv"
    )

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)

    elif args.command == "update":
        update_expense(args.id, args.description, args.amount, args.category)

    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == "summary":
        sum_expense_values(args.month)

    elif args.command == "list":
        list_expenses(args.category, args.month)

    elif args.command == "export":
        export_to_csv(args.json_file, args.to_csv)


if __name__ == "__main__":
    main()
