import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import json

file_path = "C:/Users/andre/Downloads/datos_threads.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.json_normalize(data)

tokenizer = BertTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = BertForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

def predict_sentiment(comment):
    inputs = tokenizer.encode_plus(comment, return_tensors='pt', truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.softmax(outputs.logits, dim=1)

    predicted_class = predictions.argmax().item()

    sentiment_labels = ["Muy Negativo", "Negativo", "Neutral", "Positivo", "Muy Positivo"]
    predicted_sentiment = sentiment_labels[predicted_class]

    return predicted_sentiment

df['sentimiento'] = df['description'].apply(predict_sentiment)

data_with_sentiment = df.to_dict(orient='records')

output_file_path = "C:/Users/andre/Downloads/datos_threads_con_sentimiento.json"
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(data_with_sentiment, f, ensure_ascii=False, indent=4)

print(f"Archivo guardado en: {output_file_path}")
