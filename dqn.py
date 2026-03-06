import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=256):
        super(DQN, self).__init__()

        self.linear1 = nn.Linear(state_dim, hidden_dim)
        self.linear2 = nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        return self.linear2(x)
    
if __name__ == "__main__":
    state_dim = 12
    action_dim = 2
    model = DQN(state_dim, action_dim)
    state = torch.randn(1, state_dim)
    output = model(state)
    print(output)