## ICASSP - Prawesh Dahal
#model.py - creates a Transformer model 


import torch 
import torch.nn as nn 

from dataset_loader import Dataset_EEG

class EEGEncoder(nn.Module): 
    def __init__(self, input_channels, feature_size, num_heads, num_layers, dropout = 0.1):
        super().__init__()

        self.conv1 = nn.Conv1d(input_channels, feature_size, kernel_size=3, padding=1)
        self.relu1 = nn.ReLU()
        
        self.conv2 = nn.Conv1d(feature_size, feature_size, kernel_size= 3, padding=1)
        self.relu2 = nn.ReLU()

        encoder_layer = nn.TransformerEncoderLayer(d_model=feature_size, nhead= num_heads, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers)

    def forward(self, x): 

        x = x.permute(0,2,1) #batch, channels, time 

        x = self.conv1(x)
        x = self.relu1(x)

        x = self.conv2(x)
        x = self.relu2(x)

        x = x.permute(2,0,1) #time, batch, features

        output = self.transformer_encoder(x)

        return output
    
 ### Temporary pipeline - change the transformer model drastically
        