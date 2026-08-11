import argparse
import sys
from pathlib import Path
from datetime import date
import pandas as pd

FILE_PATH = Path("data.csv")

# Fileexistence check and file empty check
def initialize_csv():
    if not FILE_PATH.is_file() or FILE_PATH.stat().st_size == 0:
        df = pd.DataFrame(columns=["id", "account", "money", "date", "description"])
        df.to_csv(FILE_PATH, header=True, index=False)

# Add new entry
def add_money(amount, description):
    df_csv = pd.read_csv(FILE_PATH)
    new_id = 1 if df_csv.empty else df_csv["id"].max() + 1

    df = pd.DataFrame([{
        "id": new_id,
        "account": "bank", 
        "money": amount, 
        "date": date.today().isoformat(),
        "description": description
    }])
    df.to_csv(FILE_PATH, mode="a", header=False, index=False)
    print(f"Added: \n{df}")

# Remove transaction by the id
def remove_transaction(id):
    df = pd.read_csv(FILE_PATH)

    # check id before removing
    df_removed = df[df["id"] == id] # Show which row was removed, before removing it
    if df_removed.empty:
        print(f"Error: Transaction with ID {id} not found")
        return
    print(f"Removed: \n{df_removed}")

    df = df[df["id"] != id] # to remove the row 
    df.to_csv(FILE_PATH, header=True, index=False)

# Commands
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")
# Subcommand: add
add_parser = subparsers.add_parser("add", help="add a new transaction")
add_parser.add_argument("amount", type=float, help="amount of money (also negative)")
add_parser.add_argument( "-d", "--description",
                    default="No description", 
                    help="add a description to the transaction"
                    )
# Subcommand: remove
remove_parser = subparsers.add_parser("remove", help="remove a transaction")
remove_parser.add_argument("id", type=int, help="id of the transaction")

args = parser.parse_args()

print(args)

initialize_csv()

if args.command == "add":
    add_money(args.amount, args.description) 
elif args.command == "remove":
    remove_transaction(args.id)
else:
    parser.print_help()
    sys.exit(0)