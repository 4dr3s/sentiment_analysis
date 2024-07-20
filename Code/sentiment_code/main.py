from transformers import BertModel, BertTokenizer, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader
from textwrap import wrap
import numpy as np
import pandas as pd
import torch

random_seed = 0
max_len = 200
batch_size = 16
dataset_path = 'C:/Users/andre/Downloads/datos_threads.csv'
n_classes = 2

np.random.seed(random_seed)
torch.manual_seed(random_seed)
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

df = pd.read_csv(dataset_path, sep=';')
print(df)

pre_trained_model = 'dccuchile/bert-base-spanish-wwm-cased'
tokenizer = BertTokenizer.from_pretrained(pre_trained_model)

sample_txt = 'Estoy comiendo en familia'
tokens = tokenizer.tokenize(sample_txt)
tokens_ids = tokenizer.convert_tokens_to_ids(tokens)
print('Frase: ', sample_txt)
print('Tokens: ', tokens)
print('Tokens numéricos: ', tokens_ids)

encoding = tokenizer.encode_plus(
    sample_txt,
    max_length=10,
    truncation=True,
    add_special_tokens=True,
    return_token_type_ids=False,
    pad_to_max_length=True,
    return_attention_mask=True,
    return_tensors='pt'
)
