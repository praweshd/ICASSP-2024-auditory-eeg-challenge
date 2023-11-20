## ICASSP - Prawesh Dahal
#model.py - creates a Transformer model 


import torch 
import torch.nn as nn 

from dataset_loader import Dataset_EEG

class EEGEncoder(nn.Module): 
    def __init__(self, input_channels, feature_size):
        super().__init__()

        self.conv1 = nn.Conv1d(input_channels, feature_size, kernel_size=3, padding=1)
        self.relu1 = nn.ReLU()
        
        self.conv2 = nn.Conv1d(feature_size, feature_size, kernel_size= 3, padding=1)
        self.relu2 = nn.ReLU()

    def forward(self, x): 
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.conv2(x)
        x = self.relu2(x)

        return x 
    


        