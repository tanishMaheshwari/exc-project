# summarize.py

import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

nltk.download('punkt')

def summarize_text(text, method="LSA", num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    if method == "LSA":
        summarizer = LsaSummarizer()
    elif method == "LexRank":
        summarizer = LexRankSummarizer()
    elif method == "Luhn":
        summarizer = LuhnSummarizer()
    else:
        raise ValueError("Invalid summarization method selected.")

    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)
