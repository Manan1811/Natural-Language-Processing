import nltk
nltk.download()

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
porter = PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
x=stemSentence(sentence)
print(x)

'''
python are veri intellig and work veri pythonli and now they are python their way to success .
'''