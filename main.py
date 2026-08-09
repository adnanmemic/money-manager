import sys
import pathlib
from datetime import date
import pandas as pd

FILE_PATH = pathlib.Path("data.csv")

# Fileexistence check
def initialize_csv():
    if not FILE_PATH.is_file():
        df = pd.DataFrame(columns=["account", "money", "date"])
        df.to_csv(FILE_PATH, index=False)

# Add new entry
def add_money(amount):
    df = pd.DataFrame([
        {"account": "bank", "money": amount, "date": date.today().isoformat()}
    ])
    df.to_csv(FILE_PATH, mode="a", header=False, index=False)

# arguments check: python3 main.py <mode> <amount>
if len(sys.argv) < 3:
    print("Error: not enough arguments", file=sys.stderr)
    sys.exit(1)

mode = sys.argv[1]
amount = sys.argv[2]

initialize_csv()

match mode:
    case "add":
        add_money(amount) 
        print(f"Added: {sys.argv[2]}")