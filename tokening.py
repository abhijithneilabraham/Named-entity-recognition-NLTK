import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
eg='I am from India.My place is Eranakulam. India is in Asia'
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent=preprocess(eg)
print(sent)
