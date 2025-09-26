class LanguageModel:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_input_hidden = self.initialize_weights(input_size, hidden_size)
        self.weights_hidden_output = self.initialize_weights(hidden_size, output_size)

    def initialize_weights(self, input_size, output_size):
        return np.random.randn(input_size, output_size) * 0.01

    def forward(self, x):
        self.hidden_layer = self.activation_function(np.dot(x, self.weights_input_hidden))
        output_layer = self.activation_function(np.dot(self.hidden_layer, self.weights_hidden_output))
        return output_layer

    def activation_function(self, x):
        return 1 / (1 + np.exp(-x))

    def compute_loss(self, predicted, actual):
        return np.mean((predicted - actual) ** 2)

    def backward(self, x, y, learning_rate):
        output = self.forward(x)
        loss = self.compute_loss(output, y)
        
        # Backpropagation logic here (omitted for brevity)
        
        return loss

    def train(self, x, y, epochs, learning_rate):
        for epoch in range(epochs):
            loss = self.backward(x, y, learning_rate)
            if epoch % 100 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')