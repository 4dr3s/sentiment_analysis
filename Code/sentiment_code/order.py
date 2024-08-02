import json
import pandas as pd
from datetime import datetime

file_path = "C:/Users/andre/Downloads/datos_threads_instagram_con_sentimiento.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.json_normalize(data)

date_intervals = [
    (datetime(2023, 6, 5), datetime(2023, 6, 20), 'Fechas entre 5 de junio y 20 de junio de 2023'),
    (datetime(2023, 6, 21), datetime(2023, 9, 1), 'Fechas entre 21 de junio y 1 de septiembre de 2023'),
    (datetime(2023, 9, 2), datetime(2023, 10, 15), 'Fechas entre 2 de septiembre y 15 de octubre de 2023'),
    (datetime(2023, 10, 16), datetime(2023, 11, 23), 'Fechas entre 16 de octubre y 23 de noviembre de 2023'),
    (datetime(2023, 11, 24), datetime(2023, 11, 26), 'Fechas entre 24 de noviembre y 26 de noviembre de 2023'),
    (datetime(2023, 11, 27), datetime(2023, 11, 28), 'Fechas entre 27 de noviembre y 28 de noviembre de 2023'),
    (datetime(2023, 11, 29), datetime(2023, 12, 8), 'Fechas entre 29 de noviembre y 8 de diciembre de 2023'),
    (datetime(2023, 12, 9), datetime(2023, 12, 26), 'Fechas entre 9 de diciembre y 26 de diciembre de 2023'),
    (datetime(2023, 12, 27), datetime(2024, 3, 21), 'Fechas entre 27 de diciembre de 2023 y 21 de marzo de 2024'),
    (datetime(2024, 3, 22), datetime(2024, 4, 5), 'Fechas entre 22 de marzo y 5 de abril de 2024'),
    (datetime(2024, 4, 6), datetime(2024, 5, 13), 'Fechas entre 6 de abril y 13 de mayo de 2024'),
    (datetime(2024, 5, 14), datetime(2024, 5, 15), 'Fechas entre 14 de mayo y 15 de mayo de 2024'),
    (datetime(2024, 5, 16), datetime(2024, 7, 24), 'Fechas entre 16 de mayo de 2024 y 24 de julio de 2024'),
]

df['date_range'] = None

for index, i in df.iterrows():
    date_post = datetime.strptime(i['post_date'], '%Y-%m-%d')
    for start_date, end_date, description in date_intervals:
        if start_date <= date_post <= end_date:
            df.at[index, 'date_range'] = description
            break

modified_data = df.to_dict(orient='records')
output_file_path = "C:/Users/andre/Downloads/datos_threads_instagram_range_date.json"
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(modified_data, f, ensure_ascii=False, indent=4)

