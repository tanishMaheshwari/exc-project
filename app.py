# summarize.py

import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# Command-line testing
if __name__ == "__main__":
    input_text = input("Enter the text to summarize:\n")
    summary = summarize_text(input_text, num_sentences=3)
    print("\n--- Summary ---\n", summary)
