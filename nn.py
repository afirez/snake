import torch
import torch.nn as nn

class Net(nn.Module):       
    def __init__(self, n_input, n_hidden1, n_hidden2, n_output):
        super(Net, self).__init__()

        self.a = n_input
        self.b = n_hidden1
        self.c = n_hidden2
        self.d = n_output

        self.fc1 = nn.Linear(n_input, n_hidden1)
        self.fc2 = nn.Linear(n_hidden1, n_hidden2)
        self.out = nn.Linear(n_hidden2, n_output)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        y = self.fc1(x)
        y = self.relu(y)
        y = self.fc2(y)
        y = self.sigmoid(y)
        y = self.out(y)
        return y

    def update(self, weights):
        with torch.no_grad():
            weights = torch.FloatTensor(weights)
            x = self.a * self.b
            y = x + self.b * self.c
            z = y + self.c * self.d
            self.fc1.weight.data = weights[0 : x].reshape(self.a, self.b)
            self.fc2.weight.data = weights[x : y].reshape(self.b, self.c)
            self.out.weight.data = weights[y : z].reshape(self.c, self.d)

    def predict(self, input):
        input = torch.tensor([input])
        y = self(input)
        return torch.argmax(y, dim=1).tolist()[0]

    def show(self):
        for parameters in self.parameters():
            print(parameters)

if __name__ == '__main__':
    model = Net(32, 20, 12, 4)
    model = Net(2, 2, 2, 2)
    weights = [1.0 for _ in range(16)]
    model.update(weights)
    input = [1.0, 2.0]
    print(model.predict(input))
