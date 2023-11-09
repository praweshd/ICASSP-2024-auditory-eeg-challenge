## Dataset for ICASSP 
# Prawesh Dahal

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

#Data Initialization that creates Xdata samples
class Dataset_EEG(Dataset):  

    def __init__(self, path = '/Users/praweshd/Documents/ICASSP-2024-auditory-eeg-challenge/data/split_data', file_type = ["train"], frame_length = 64, hop_length = 30):
        super().__init__()
        self.frame_length = frame_length
        self.hop_length = hop_length   
        self.input_paths = [os.path.join(path,file) for  file in os.listdir(path) if file_type[0] in file and "eeg" in file]
        
        cnt = 0
        self.fileidx = {}

        for file in self.input_paths: 
            
            data = np.load(file, mmap_mode= 'r')  # mmap - access small portion of eegfile w/o reading into memory
            num_samples = data.shape[0]
            num_windows = 1 +  (num_samples - self.frame_length) // self.hop_length 

            for win in range(num_windows):
                self.fileidx[cnt] = (file, win)
                cnt+= 1 

    def __len__(self):
        return len(self.fileidx)

    def __getitem__(self,idx): 
        file, win = self.fileidx[idx]
        start = win*self.hop_length
        stop = start + self.frame_length 
        Xdata = np.load(file,mmap_mode='r')[start : stop]
        return torch.from_numpy(Xdata.copy())
    

# Create an instance of the Dataset_EEG class
dataset = Dataset_EEG()
print(len(dataset))

# Access the Xdata
for i in range(len(dataset)):
    Xdata = dataset[0]

    #print(f"Xdata for index {i}: {Xdata}")



            
        


