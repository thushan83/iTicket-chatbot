from nn import NN
from data_prep import DataClenser
import torch
import json
import random

class ChatManager():
    def __init__(self):
        self.device = torch.device('cpu')
        with open('intents.json','r') as file:
           self.intents_from_file = json.load(file)

        FILE = "data.pth"
        data = torch.load(FILE) 

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        self.all_words = data['all_words']
        self.tags = data['tags']
        model_state = data["model_state"]  

        self.model = NN(input_size,hidden_size,output_size)
        self.model.load_state_dict(model_state)
        self.model.eval()
        self.dataCln = DataClenser()

    def find_answer(self,question):
        q_words = self.dataCln.tokanize(question)
        x = self.dataCln.get_bag_of_words(q_words,self.all_words)
        x = x.reshape(1,x.shape[0])
        x = torch.from_numpy(x).to(self.device)

        op = self.model(x)
        _, predicted = torch.max(op,dim = 1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(op, dim=1)
        prob = probs[0][predicted.item()]

        default_response = "Sorry I do not have the answer, or I do not understand your question"
        print("------------------------------------------------------")
        print("model op---",op)
        print("tags---",self.tags)
        print("prob---",str(prob.item()),"tag---",str(predicted.item()))
        print("------------------------------------------------------")
        if prob.item() > 0.54:
            for intent in self.intents_from_file['intents']:
                print(tag,"---",intent["tag"])
                if tag == intent["tag"]:
                    return(random.choice(intent['responses']))
        else:
            return default_response

#def main():  
#    chatbot_name = "iTicket: "
#    guest = "You: "
#    cm = ChatManager()  
#    print(chatbot_name,"Welcome how can I help you ?")
#    while True:
#        question = ""
#        question = input(guest)
#        print(chatbot_name, cm.find_answer(question))

#if __name__ == "__main__":
#    main()
  
