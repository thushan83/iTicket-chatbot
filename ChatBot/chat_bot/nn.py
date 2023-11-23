import torch
import torch.nn as nn
import torch.nn.functional as f


class NN(nn.Module):
    def __init__(self,input_size, hidden_size, output_size):
        super(NN,self).__init__()
        self.linL1 = nn.Linear(input_size,hidden_size)
        self.linL2 = nn.Linear(hidden_size,hidden_size)
        self.linL3 = nn.Linear(hidden_size,output_size)

    def forward(self,x):    
        x = self.linL1(x)
        x = f.relu(x)
        x = self.linL2(x)
        x = f.relu(x)
        x = self.linL3(x)
        output = x
        return output
