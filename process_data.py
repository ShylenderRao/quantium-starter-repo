import pandas as pd
import os

data_folder = "data"
files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

df_list = []

for file in files:
    path = os.path.join(data_folder, file)
    df = pd.read_csv(path)

    df = df[df["product"] == "pink morsel"]
    df["sales"] = df["quantity"] * df["price"]
    df = df[["sales", "date", "region"]]

    df_list.append(df)

final_df = pd.concat(df_list)
final_df.to_csv("formatted_output.csv", index=False)

print("✅ Data processed successfully!")