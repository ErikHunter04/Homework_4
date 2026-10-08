import pandas as pd

DATA_PATH="../data/"

df = pd.read_csv(f"{DATA_PATH}clean_dialog.csv")

data = {
        "pony_name": ["Twilight Sparkle","Rarity","Pinkie Pie","Rainbow Dash","Fluttershy"],
        "total_line_count": [],
        "percent_all_lines": []
        }

for pony in data.get("pony_name"):
    data.get("total_line_count").append((df["pony"] == pony).sum())

clean = pd.DataFrame(data)
clean.to_csv(f"{DATA_PATH}Line_percentages.csv", index=False)
