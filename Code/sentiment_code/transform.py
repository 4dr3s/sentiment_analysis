import pandas as pd
import json

file_path = "C:/Users/andre/Downloads/datos_tiktok2.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.json_normalize(data)
print(df)


def change_row(data_row):
    if 'K' in data_row:
        str_number = data_row.replace('K', '00').replace('.', '')
        return int(str_number)
    return int(data_row)


df["reactions"] = df["reactions"].apply(change_row)

modified_data = df.to_dict(orient='records')
output_file_path = "C:/Users/andre/Downloads/datos_tiktok2.json"
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(modified_data, f, ensure_ascii=False, indent=4)
