# MINI PROJECT : TEXT SUMMARIZER

# install library
!pip install -q sumy

import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

print("=================================")
print("        TEXT SUMMARIZER")
print("=================================")

# user enters paragraph
print("\nEnter your paragraph:\n")
text = input()

# convert text to document
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# initialize summarizer
summarizer = LsaSummarizer()

# choose number of sentences for summary
num_sentences = int(input("\nHow many sentences should the summary contain? "))

summary = summarizer(parser.document, num_sentences)

print("\n------ SUMMARY ------\n")

# print summarized sentences
for sentence in summary:
    print(sentence)

print("\nSummary generated successfully.")
