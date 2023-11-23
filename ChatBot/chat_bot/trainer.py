import json
import nltk
from data_prep import DataClenser
from nn import NN
from nltk.stem.porter import PorterStemmer
import numpy as np
from torch.utils.data import Dataset, DataLoader
import torch
import torch.nn as nn

class DataSet(Dataset):
    def __init__(self, X_Training_Set, Y_Training_Set):
        self.n_samples = len(X_Training_Set)
        self.x_data = X_Training_Set
        self.y_data = Y_Training_Set

    def __getitem__(self, index):
        return self.x_data[index],self.y_data[index]

    def __len__(self):
        return self.n_samples        


class Trainer():  

     tags = []
     all_pattern_words = []
     tag_words_map = []
     ignore_words = ["?", "!", "_", ".", ","]
     X_Training_Set = []
     Y_Training_Set = []

     def __init__(self, num_epochs, batch_size, learning_rate, hidden_size):
        self.num_epochs = num_epochs
        self.batch_size =  batch_size
        self.learning_rate = learning_rate
        self.hidden_size = hidden_size       

        with open('intents.json','r') as file:
            self.intents_from_file = json.load(file)
            self.dataCln = DataClenser()
            self.stemmer = PorterStemmer()
            #print(intents_from_file)

     def prepare_training_data(self):       
        #print(self.intents_from_file)
        for intent_item in self.intents_from_file["intents"]:
            #print(intent_item)
            tag = intent_item["tag"]
            self.tags.append(tag)
            for pattern_item in intent_item["patterns"]:
                #print(pattern_item)
                pattern_words = self.dataCln.tokanize(pattern_item)
                self.all_pattern_words.extend(pattern_words)
                self.tag_words_map.append((pattern_words,tag))
            #print(self.tag_words_map)

        #clean any ignore words
        all_pattern_words = [self.stemmer.stem(word) for word in self.all_pattern_words if word not in self.ignore_words]
        non_duplicated_words = set(all_pattern_words)
        self.all_pattern_words = sorted(non_duplicated_words)
        non_duplicated_tags = set(self.tags)
        self.tags = sorted(non_duplicated_tags)
        return all_pattern_words

     def populate_training_data_sets(self):
        for pattern_words,tag in self.tag_words_map:
            bag = self.dataCln.get_bag_of_words(pattern_words,self.all_pattern_words)
            #print(bag)
            self.X_Training_Set.append(bag)
            label = self.tags.index(tag)
            self.Y_Training_Set.append(label)

        self.X_Training_Set = np.array(self.X_Training_Set, dtype=np.float32)
        self.Y_Training_Set = np.array(self.Y_Training_Set, dtype=np.int64)

     def train(self):
         self.input_size = len(self.X_Training_Set[0])
         self.output_size = len(self.tags)   

         dataset = DataSet(self.X_Training_Set,self.Y_Training_Set)
         train_loader = DataLoader(dataset=dataset, batch_size=self.batch_size, shuffle=True, num_workers=2)

         device = torch.device('cpu')
         model = NN(self.input_size, self.hidden_size,self.output_size)

         loss_func = nn.CrossEntropyLoss()
         optimizer = torch.optim.Adam(model.parameters(), self.learning_rate)

         for training_turn in range(self.num_epochs):
            for (words, labels) in train_loader:

                words = words.to(device)
                #print(".......",labels)
                labels = labels.to(device)  
                #print("*******",labels)
                outputs = model(words)

                #outputs = np.array(outputs, dtype=np.int64)
                #labels = torch.zeros(len(labels), dtype = torch.long)


                #input1 = torch.rand(3, 5)
                #target1 = torch.empty(3, dtype = torch.long).random_(5)

                #print("-------",input1)

                #print("++++++++",target1)
                #xxx = loss_func(input1, target1)
                #print("_______",xxx)
                #print("-------",outputs)

                #print("++++++++",labels)

                loss = loss_func(outputs, labels)              

                optimizer.step()

                #if(training_turn%100 == 0):
                print("Epoch = "+str(training_turn), "Loss = "+str(loss.item()))
         
         data = {
          "model_state": model.state_dict(),
          "input_size": self.input_size,
          "hidden_size": self.hidden_size,
          "output_size": self.output_size,
          "all_words": self.all_pattern_words,
          "tags": self.tags
         }

         FILE = "data.pth"
         torch.save(data, FILE)

         print("Training complete, file save to", FILE)          



     def print(self):    
        print("__",self.tags)
        print("--",self.X_Training_Set)
        print("??",self.Y_Training_Set)

       


if __name__ == "__main__":
    trainer = Trainer(num_epochs =  10 , batch_size = 8 , learning_rate = 0.001, hidden_size = 8)
    training_data = trainer.prepare_training_data()
    trainer.populate_training_data_sets()
    #trainer.print()
    trainer.train()

