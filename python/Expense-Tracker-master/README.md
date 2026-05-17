
# Expense Tracker CLI

## Overview
This is a command-line interface (CLI) tool to manage personal or business expenses. The tool allows users to add, update, delete, list, summarize, and export expenses from a JSON file to a CSV format. 

## Features
- Add new expense entries with description, amount, and category.
- Update existing expense entries.
- Delete specific expense entries by ID.
- Summarize total expenses for a particular month.
- List expenses by category or month.
- Export expense data from JSON to CSV.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker-cli.git
   ```

2. Navigate into the project directory:
   ```bash
   cd expense-tracker-cli
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the CLI tool using the following commands:

### Add Expense
```bash
python expense_tracker_cli.py add --description "Lunch" --amount 15 --category "Food"
```

### Update Expense
```bash
python expense_tracker_cli.py update --id 1 --description "Lunch with Client" --amount 20 --category "Business"
```

### Delete Expense
```bash
python expense_tracker_cli.py delete --id 1
```

### Summarize Expenses
```bash
python expense_tracker_cli.py summary --month 09
```

### List Expenses
```
python expense_tracker_cli.py list
```
```
+----+------------+--------------+--------+----------+
| id |    date    | description  | amount | category |
+----+------------+--------------+--------+----------+
| 2  | 2024-09-18 |  Groceries   |  $50   |   Food   |
+----+------------+--------------+--------+----------+
| 3  | 2024-08-18 |    LG TV     |  $400  |  Movie   |
+----+------------+--------------+--------+----------+
| 4  | 2024-08-18 |  Samsung TV  |  $900  |  Movie   |
+----+------------+--------------+--------+----------+
| 5  | 2024-09-18 | Gaming mouse | $4500  |  Gaming  |
+----+------------+--------------+--------+----------+
| 6  | 2024-09-19 |   Munchies   |  $50   |   Food   |
+----+------------+--------------+--------+----------+
```
```bash
python expense_tracker_cli.py list --category "Food"
```
```
+----+------------+-------------+--------+----------+
| id |    date    | description | amount | category |
+----+------------+-------------+--------+----------+
| 2  | 2024-09-18 |  Groceries  |  $50   |   Food   |
+----+------------+-------------+--------+----------+
| 6  | 2024-09-19 |   Munchies  |  $50   |   Food   |
+----+------------+-------------+--------+----------+
```

### Export Expenses to CSV
```bash
python expense_tracker_cli.py export --json-file expenses.json --to-csv expenses.csv
```

## Project Structure
```bash
.
├── expense_tracker_cli.py    # CLI interface for expense management
├── expense_management
│   ├── expense_manager.py    # Core logic for managing expenses
│   ├── json_manager.py       # Functions for handling JSON operations
├── expenses.json             # Sample expenses data file
├── requirements.txt          # Required libraries (e.g., pandas, prettytable)
└── README.md                 # Project documentation
```

## Dependencies
- `pandas`: Used for exporting JSON data to CSV.
- `prettytable`: Used for displaying expenses in a tabular format in the console.

To install these dependencies, run:
```bash
pip install pandas prettytable
```

## Help
To see the help message:
```
python .\expense_tracker_cli.py --help
```
```
usage: python expense_tracker_cli.py COMMAND [OPTIONS] [ARGS]...

A CLI tool to manage expenses by adding, updating, deleting, summarizing expense entries and exporting json file to csv file

positional arguments:
  {add,update,delete,summary,list,export}
    add                 add an expense entry
    update              update an existing expense entry
    delete              delete an expense entry
    summary             summarize expense entries (sum)
    list                display expenses
    export              export json file to designated type

options:
  -h, --help            show this help message and exit
```

## License
This project is licensed under the MIT License.


## Project URL
https://roadmap.sh/projects/expense-tracker
