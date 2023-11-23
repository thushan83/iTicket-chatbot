import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

#nltk.download('punkt')


class DataClenser:

    def __init__(self):
        self.stemmer = PorterStemmer()

    def tokanize(self,question):
        return nltk.word_tokenize(question)    

    def get_bag_of_words(self, tokanized_question, words):
        #print([self.stemmer.stem(q_word) for q_word in tokanized_question])
        question_words = [self.stemmer.stem(q_word) for q_word in tokanized_question]
        bag=np.zeros(len(words), dtype=int)
        for index,bag_word in words:
            print(index,"-", bag_word)
            #if bag_word in question_words:
            #    bag[index] = 1

        return bag        




## TESTS
if __name__ == "__main__":
    dc=DataClenser()
    tokenized_q = dc.tokanize("Hi, I need to create an order")
    print(tokenized_q)
    bag = dc.get_bag_of_words(tokenized_q,["hi","hello","create","order","registry","pos"])
    print(bag)

## ----------    



