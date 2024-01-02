from transformers import pipeline

generator = pipeline("text-generation",model = "distilgpt2")

response = generator("In big data processing we are going to learn", max_length=30 , num_return_sequences = 3)

print(response)