from transformers import pipeline

classifier = pipeline("zero-shot-classification")
labels=["education", "sales"]
response = classifier("This is big data processing with NLP",labels)


print(response)