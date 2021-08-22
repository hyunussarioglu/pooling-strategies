from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")

text = "Bilgiye ulaşmanın en güzel yolu düşünmektir."

tokenized = tokenizer.tokenize(text, add_special_tokens = True)

print(tokenized)