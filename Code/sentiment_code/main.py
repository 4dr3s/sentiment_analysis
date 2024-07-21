import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch

file_path = "C:/Users/andre/Downloads/datos_threads.csv"
df = pd.read_csv(file_path, sep=";")

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

output_file_path = "C:/Users/andre/Downloads/datos_threads_con_sentimiento.csv"
df.to_csv(output_file_path, index=False, sep=";")

print(f"Archivo guardado en: {output_file_path}")
