import nltk
nltk.download()

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
'''
Non-English Stemmers
Python nltk provides not only two English stemmers: PorterStemmer and LancasterStemmer but also a lot of non-English stemmers as part of SnowballStemmers, ISRIStemmer, RSLPSStemmer. Python NLTK included SnowballStemmers as a language to create to create non-English stemmers. One can program one's 
own language stemmer using snowball. Currently, it supports the following languages:
SnowballStemmers:Danish,Dutch,English,French,German,Hungarian,Italian,Norwegian,Porter,Portuguese,Romanian,Russian,Spanish,Swedish,
ISRIStemmer is an Arabic stemmer and RSLPStemmer is stemmer for the Portuguese Language.
'''
porter = PorterStemmer()
lancaster=LancasterStemmer()
from nltk.stem.snowball import SnowballStemmer
englishStemmer=SnowballStemmer("english")
englishStemmer.stem("having")

word_list = ["friend", "friendship", "friends", "friendships","stabil","destabilize","misunderstanding","railroad","moonlight","football"]
print("{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
for word in word_list:
    print("{0:20}{1:20}{2:20}".format(word,porter.stem(word),lancaster.stem(word)))

englishStemmer=SnowballStemmer("english")
print(englishStemmer.stem("having"))
englishStemmer2=SnowballStemmer("english", ignore_stopwords=True)
print(englishStemmer2.stem("having"))


'''
Output:
Word                Porter Stemmer      lancaster Stemmer   
friend              friend              friend              
friendship          friendship          friend              
friends             friend              friend              
friendships         friendship          friend              
stabil              stabil              stabl               
destabilize         destabil            dest                
misunderstanding    misunderstand       misunderstand       
railroad            railroad            railroad            
moonlight           moonlight           moonlight           
football            footbal             footbal 
have
having
'''