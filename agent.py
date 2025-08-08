import numpy as np

class Agent:
    def __init__(self, input_size=11, hidden_size=16, output_size=3, weights=None):
        if weights is None:
            # Inicializa pesos aleatórios
            self.w1 = np.random.randn(hidden_size, input_size) * 0.1
            self.b1 = np.zeros((hidden_size, 1))
            self.w2 = np.random.randn(output_size, hidden_size) * 0.1
            self.b2 = np.zeros((output_size, 1))
        else:
            self.w1, self.b1, self.w2, self.b2 = weights

    def get_weights(self):
        return (self.w1, self.b1, self.w2, self.b2)

    def set_weights(self, weights):
        self.w1, self.b1, self.w2, self.b2 = weights

    def forward(self, x):
        x = x.reshape(-1, 1)  # Coluna
        z1 = np.dot(self.w1, x) + self.b1
        a1 = np.tanh(z1)
        z2 = np.dot(self.w2, a1) + self.b2
        return z2.flatten()

    def act(self, state):
        output = self.forward(state)
        action = np.argmax(output)  # Escolhe ação com maior valor
        return action
