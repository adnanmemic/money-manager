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