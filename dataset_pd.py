## Dataset for ICASSP 

import torch 
from torch.utils.data import ConcatDataset, Dataset
import torchvision.transforms as transforms 
import numpy as np
import os 

#path = '/Users/praweshd/Documents/ICASSP-2024-auditory-eeg-challenge/data/split_data'

# Extract just the EEG training file paths 
#train_eeg = [os.path.join(path,file) for file in os.listdir(path) if "train" in file and "eeg" in file]
 
# Example file 
#data = np.load(train_eeg[0])
# each eeg dim is shape: (47964, 64)

class Dataset_EEG(Dataset): 


    def __init__(self, path = '/Users/praweshd/Documents/ICASSP-2024-auditory-eeg-challenge/data/split_data', file_type = ["train"], frame_length = 64, hop_length = 32):
        super().__init__()
        self.frame_length = frame_length
        self.hop_length = hop_length   
        self.input_paths = [os.path.join(path,file) for  file in os.listdir(path) if file_type[0] in file and "eeg" in file]

        for file in self.input_paths: 
            
            data_shape = np.load(file, mmap_mode= 'r') 
            # mmap - access small portion of eegfile w/o reading into memory
            
