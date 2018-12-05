import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np

sigmoid = nn.Sigmoid()

t = np.array([[1,1,1,1],[0,0,1,1]])
o = np.array([[1,3,3,3],[-3,-3,3,3]])

t = Variable(torch.Tensor(t))
o = Variable(torch.Tensor(o))

print(nn.BCEWithLogitsLoss()(o, t))
print(nn.BCELoss()(sigmoid(o), t)) # Different numbers

o = np.array([[3,3,3,3],[-3,-3,3,3]])
o = Variable(torch.Tensor(o))

print(nn.BCEWithLogitsLoss()(o, t))
print(nn.BCELoss()(sigmoid(o), t)) # Same numbers
