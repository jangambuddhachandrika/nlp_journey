import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download tokenizer models (only first time)
nltk.download('punkt')

# Step 1: Take input text
text = "Natural Language Processing is amazing! It helps computers understand humans."

# Step 2: Word Tokenization
word_tokens = word_tokenize(text)
print("Word Tokens:", word_tokens)

# Step 3: Sentence Tokenization
sentence_tokens = sent_tokenize(text)
print("Sentence Tokens:", sentence_tokens)

# Step 4: Character Tokenization
char_tokens = list(text)
print("Character Tokens:", char_tokens)
