from nltk.stem.snowball import RussianStemmer
from sklearn.feature_extraction.text import CountVectorizer
stemmer = RussianStemmer()
analyzer = CountVectorizer().build_analyzer()

def stemming(doc):
    return (stemmer.stem(w) for w in analyzer(doc))
