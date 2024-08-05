import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def prepdata(fn):
    csvfile = pd.read_csv(fn)
    csvfile = csvfile[csvfile['Currency'] == 'Etherium']
    x = csvfile[['Open', 'High', 'Low']]
    y = csvfile['Close']
    x = torch.tensor(x.values).float()
    y = torch.tensor(y.values).float()
    xtrn, xtst, ytrn, ytst = train_test_split(x, y, test_size=0.15, shuffle=False)
    return xtrn, xtst, ytrn.unsqueeze(1), ytst.unsqueeze(1), csvfile

xtrain, xtest, ytrain, ytest, csvf = prepdata('ETH-BTC-USD.csv')

class HybrNN(nn.Module):
    def __init__(self):
        super(HybrNN, self).__init__()
        self.fc1 = nn.Linear(3, 40)
        self.fc2 = nn.Linear(40, 70)
        self.fc3 = nn.Linear(70, 100)
        self.fc4 = nn.Linear(100, 1)
    def forward(self, x):
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = f.relu(self.fc3(x))
        x = self.fc4(x)
        return x

model = HybrNN()

def trainmodel(mdl, xtrn, ytrn, xtst, ytst, epochs=100):
    crit = nn.MSELoss()
    optimize = optim.Adam(mdl.parameters(), lr=0.001)
    trnloss = []
    tstloss = []
    print("Model Training")
    for epoch in range(epochs):
        mdl.train()
        optimize.zero_grad()
        outs = mdl(xtrn)
        loss = crit(outs, ytrn)
        loss.backward()
        optimize.step()
        trnloss.append(loss.item())
        mdl.eval()
        with torch.no_grad():
            test_outputs = mdl(xtst)
            test_loss = crit(test_outputs, ytst)
            tstloss.append(test_loss.item())
            print(f'Epoch {epoch}, Train Loss: {loss.item():.4f}, Test Loss: {test_loss.item():.4f}')
    return trnloss, tstloss

trainlosses, testlosses = trainmodel(model, xtrain, ytrain, xtest, ytest)

def printlosses(trnloss, tstloss):
    plt.figure(figsize=(10, 5))
    plt.plot(trnloss, label='Training loss')
    plt.plot(tstloss, label='Test loss')
    plt.title('Training and Test Losses')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

printlosses(trainlosses, testlosses)

def predictreal(mdl, xtst, ytst):
    mdl.eval()
    with torch.no_grad():
        predictions = mdl(xtst)
    plt.figure(figsize=(10, 5))
    plt.plot(ytst.numpy(), label='Real Values')
    plt.plot(predictions.numpy(), label='Predicted Values')
    plt.title('Comparison of Real and Predicted Values')
    plt.xlabel('Days')
    plt.ylabel('Values')
    plt.legend()
    plt.show()

predictreal(model, xtest, ytest)
last_row = csvf.iloc[-1][['Open', 'High', 'Low']].astype(float).values
last_row_tensor = torch.tensor(last_row).float()
model.eval()
with torch.no_grad():
    predicted_currency = model(last_row_tensor.unsqueeze(0))
print(f'Prognosed tomorrow`s currency: {predicted_currency.item()}')
