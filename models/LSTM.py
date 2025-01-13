import torch
import torch.nn as nn
import torchvision.models as models
class CNNLSTM(nn.Module):
    def __init__(self, num_classes=2):
        super(CNNLSTM, self).__init__()
        
        
        self.resnet = models.resnet18(pretrained=True)
        self.resnet.fc = nn.Sequential(nn.Linear(self.resnet.fc.in_features, 64))

        self.lstm = nn.LSTM(input_size=64, hidden_size=32, num_layers=1)
      

        self.fc1 = nn.Linear(32, num_classes)
       
    def forward(self, x_3d):
        hidden = None
        for t in range(x_3d.size(1)):
            with torch.no_grad():
                x = self.resnet(x_3d[:, t, :, :, :])

            out, hidden = self.lstm(x.unsqueeze(0), hidden)

        x = self.fc1(out[0])
        return x,hidden
