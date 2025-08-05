import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

text = "Natural Language Processing is amazing! It helps computers understand humans."
# Word Tokenization
print("Word Tokenization:", word_tokenize(text))
# Sentence Tokenization
print("Sentence Tokenization:", sent_tokenize(text))
