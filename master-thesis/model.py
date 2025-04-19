import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd


"""
The model architecture, consisting of 1 hidden layer.
"""

class GoClass(nn.Module):

    def __init__(self, input_dim=1280, output_dim=17, dropout=0.2):
        """
        Args
        input_dim = lenght of the feature vector for each protein sequence
        output_dim = number of classes
        dropout = choosing the portion of nodes to be dropped out, based on the density of the nodes, ranges from 0.1 to 0.5.
        """


        super(GoClass, self).__init__()

        self.fc1 = nn.Linear(input_dim, 2048)
        self.fc2 = nn.Linear(2048, 1024)
        self.fc3 = nn.Linear(1024, 512)
        self.fc4 = nn.Linear(512, 256)
        self.out = nn.Linear(256, output_dim)

        self.dropout = nn.Dropout(dropout)
        self.relu = nn.LeakyReLU()
        self.sigmoid = nn.Sigmoid()



    def forward(self, data):

        x = self.fc1(data)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc3(data)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc4(data)
        x = self.relu(x)
        x = self.dropout(x)
        out = self.out(x)
        out = self.sigmoid(out)
        return out
