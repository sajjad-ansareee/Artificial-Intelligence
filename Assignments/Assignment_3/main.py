# backpropagation algorithm for a simple artificial neural network with one hidden layer and one output layer
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# attributes
class Neuron:
    def __init__(self, weights, bias, inputs, output, learning_rate, activation_function=sigmoid):
        '''
        1. weights:             3D list, with each 2D list for each layer, with each 1D list for each neuron in layer, with each element in list ordered from neuron in previous layer
        2. bias:                2D list with each list for each layer of the network
        3. inputs:              1D list representing the inputs to the network
        4. output:              list if even if there is a single output 
        5. learning_rate:       a floating point number representing the learning rate of the network
        6. activation_function: mapping the output of neuron for continuous values
        '''
        self.weights = weights
        self.bias = bias
        self.inputs = inputs
        self.output = output
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        # how to decide how many neurons in hidden layer and how many layers in the network?
        # for now considering a simple network with one hidden layer and one output layer, with 2 neurons in hidden layer and 1 neuron in output layer
        # one way to get the number of neurons in hidden layer: (len(weiths[0]))

    # forward pass
    def forward_pass(self):
        # calculating the output of the hidden layer
        hidden_layer_output = []
        for i in range(len(self.weights[0])):
            neuron_output = 0
            for j in range(len(self.inputs)):
                neuron_output += (self.inputs[j]) * (self.weights[0][i][j])
            neuron_output += self.bias[0][i]
            hidden_layer_output.append(self.activation_function(neuron_output))