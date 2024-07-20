import json
import csv

# Cargar archivo json
json_file_path = "C:/Users/andre/Downloads/datos_threads.json"
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)

threads_csv = "C:/Users/andre/Downloads/datos_threads.csv"
headers = ["post_link", "user_name", "profile_link", "post_date", "description", "multimedia"]
with open(threads_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')
    writer.writeheader()
    for entry in data:
        entry['multimedia'] = ', '.join(entry['multimedia'])
        writer.writerow(entry)
