from Neuron import Neuron

class Layer:
	"""the Layer class has two attributes: layer_type and num_neurons.
	"""
	def __init__(self, layer_type, num_neurons, neurons=None):
		#The layer_type attribute can take one of the three values you proposed:
		#'input', 'hidden', or 'output'
		self.layer_type = layer_type
		#The num_neurons attribute represents the number of neurons in the layer.
		self.num_neurons = num_neurons
		self.neurons = neurons if neurons is not None else [Neuron(i,layer=self.layer_type) for i in range(num_neurons)]
	
	def set_layer_type (self, new_type):
		self.layer_type=new_type
