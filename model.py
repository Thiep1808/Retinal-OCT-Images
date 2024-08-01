import torch
import torchvision
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = torchvision.models.resnet50()

        self.model.fc = torch.nn.Sequential(
            torch.nn.Linear(2048, 512),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.3),
            torch.nn.Linear(in_features=512,
                            out_features=3))
        # self.model2 = torchvision.models.vgg19(pretrained=True)
        # self.model2.classifier = torch.nn.Sequential(
        #     torch.nn.Linear(25088, 2048),
        #     torch.nn.ReLU(),
        #     torch.nn.Dropout(p=0.3),
        #     torch.nn.Linear(2048, 512),
        #     torch.nn.ReLU(),
        #     torch.nn.Dropout(p=0.3),
        #     torch.nn.Linear(in_features=512,
        #                     out_features=3))

        # weights = torchvision.models.EfficientNet_B7_Weights.DEFAULT
        #efnet = torchvision.models.efficientnet_b5()

        # Recreate the classifier layer
        # self.efnet = efnet
        # self.efnet.classifier = torch.nn.Sequential(torch.nn.Linear(2048, 512),
        #                                             torch.nn.ReLU(),
        #                                             torch.nn.Dropout(p=0.3),
        #                                             torch.nn.Linear(in_features=512,
        #                                             out_features=3))


    def forward(self, x):
        y = self.model(x)
        return y
