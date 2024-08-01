from torch.utils.data import Dataset
import torch
from PIL import Image
import numpy as np
import os
import json

class MyDataset(Dataset):
    def __init__(self, root, mode='train', transform=None):
        self.root = root
        self.transform = transform
        self.classes = ['Normal', 'AMD', 'DME']
        split = mode
        types = os.listdir(root)
        self.list_paths = []
        for type in types:
            subs = os.listdir(f'{root}/{type}')
            for sub in subs:
                img_paths = [i for i in os.listdir(f'{root}/{type}/{sub}') if i.endswith('TIFF')]
                for i, img_path in enumerate(img_paths):
                    if split == 'train' and i % 5 != 4:
                        full_path = f'{type}/{sub}/{img_path}'
                        self.list_paths.append(full_path)
                    if split == 'test' and i % 5 == 4:
                        full_path = f'{type}/{sub}/{img_path}'
                        self.list_paths.append(full_path)



    def __len__(self):
        return len(self.list_paths)

    def __getitem__(self, idx):
        # Take picture
        image_path = f'{self.root}/{self.list_paths[idx]}'
        image = np.array(Image.open(image_path).convert('RGB'))
        if self.transform is not None:
            image = self.transform(image=image)['image']
        type = self.classes.index(image_path.split('/')[6])

        return image, type
