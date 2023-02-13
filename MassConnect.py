from Layer import Layer
from Link import Link
from StockData import StockData

class MassConnect:
	linked_neurons=[]
	def __init__(self, input_layer_neurons, output_layer_neurons):
		self.input_layer = Layer(layer_type='input', num_neurons=input_layer_neurons)
		self.hidden_layers = []
		self.output_layer = Layer(layer_type='output', num_neurons=output_layer_neurons)


	def add_hidden_layer(self, num_neurons):
		hidden_layer = Layer(layer_type='hidden', num_neurons=num_neurons)
		self.hidden_layers.append(hidden_layer)

	def connect_layers(self):
		for in_n in self.input_layer.neurons:
			for hide_n in self.hidden_layers[0].neurons:
				in_n.update_status()
				hide_n.update_status()
				link = Link(in_n, hide_n)
				connected_ports = in_n.connect(hide_n)
				if (in_n, connected_ports, link, hide_n) not in MassConnect.linked_neurons:
					MassConnect.linked_neurons.append((in_n, connected_ports, link, hide_n))

		prev_hidden_layer = self.hidden_layers[0]
		for i in range(1, len(self.hidden_layers)):
			curr_hidden_layer = self.hidden_layers[i]
			for prev_n in prev_hidden_layer.neurons:
				for curr_n in curr_hidden_layer.neurons:
					prev_n.update_status()
					curr_n.update_status()
					link = Link(prev_n, curr_n)
					connected_ports = prev_n.connect(curr_n)
					if (prev_n, connected_ports, link, curr_n) not in MassConnect.linked_neurons:
						MassConnect.linked_neurons.append((prev_n, connected_ports, link, curr_n))
					
			prev_hidden_layer = curr_hidden_layer

		for hide_n in prev_hidden_layer.neurons:
			for out_n in self.output_layer.neurons:
				hide_n.update_status()
				out_n.update_status()
				link = Link(hide_n, out_n)
				connected_ports = hide_n.connect(out_n)
				if (hide_n, connected_ports, link, out_n) not in MassConnect.linked_neurons:
					MassConnect.linked_neurons.append((hide_n, connected_ports, link, out_n))

		#Collect data
		data = StockData(MassConnect.linked_neurons)


mass = MassConnect(input_layer_neurons=5,output_layer_neurons=2)
mass.add_hidden_layer(num_neurons=5)
mass.connect_layers()
