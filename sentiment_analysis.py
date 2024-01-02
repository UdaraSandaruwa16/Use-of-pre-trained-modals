from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("Sri Lankan cricket team will never performe well")
print(result)


