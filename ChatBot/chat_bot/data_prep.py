import nltk
from nltk.stem.snowball import SnowballStemmer
import numpy as np

#nltk.download('punkt')


class DataClenser:

    def __init__(self):
        self.stemmer = SnowballStemmer("english")

    def tokanize(self,question):
        return nltk.word_tokenize(question)    

    def get_bag_of_words(self, tokanized_question, words):
        #print([self.stemmer.stem(q_word) for q_word in tokanized_question])
        question_words = [self.stemmer.stem(q_word) for q_word in tokanized_question]
        ##its important to have the data type  dtype=np.float32 since pytorch model expects that
        bag=np.zeros(len(words),  dtype=np.float32)
        index = 0
        #print("W",words)
        #print("QW",question_words)
        for bag_word in words:
            #print("----",index,"--", bag_word)
            if bag_word in question_words:
               bag[index] = 1
            index=index+1 

        return bag        




## TESTS
#if __name__ == "__main__":
#    dc=DataClenser()
#    tokenized_q = dc.tokanize("Hi, I need to create an order")
    #print(tokenized_q)
#    bag = dc.get_bag_of_words(tokenized_q,["hi","hello","create","order","registry","pos"])
#    print(bag)

## ----------    



