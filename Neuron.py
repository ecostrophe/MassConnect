import random
from Port import Port

class Neuron:
	num_neuron = 0
	def __init__(self, id_num, ports = None, weight = None, layer=None):
		self.color = (255,0,0)
		self.layer = layer
		self.position = [random.randint(200,1000), random.randint(200,1000)]
		self.id_num = self.set_id_neuron(id_num)
		self.ports = ports if ports is not None else [Port(i) for i in range(random.randint(1,10))]
		self.dim = 7
		self.linked = 0
		self.weight = weight if weight is not None else random.uniform(1, 10)
		self.momentum = self.weight/self.update_momentum()
		self.velocity = self.momentum / self.weight
		self.linked_neurons = []
		self.status = self.set_status()

	def get_ports(self):
		all_port = []
		print("for",self.id_num,"neuron have:",len(self.ports),"ports")
		for port in self.ports:
			print("port:",port.id_num,"Status:",port.type_of_connection)
			all_port.append(port)
		return all_port
		
	def set_status(self):
		port_connection = []
		for port in self.get_ports():
			port_connection.append(port.type_of_connection)
		if all(port_connection) is True:
			return True
		else:
			return False

	def set_id_neuron(self, id_num):
		Neuron.num_neuron += 1
		id_layer = ""
		if self.layer == "input":
			id_layer = "I"
			self.color = (0,0,255)
			self.position = [random.randint(200,300), random.randint(200,1000)]
		elif self.layer == "hidden":
			id_layer = "H"
			self.color = (255,0,0)
			self.position = [random.randint(400,800), random.randint(200,1000)]
		elif self.layer == "output":
			id_layer = "U"
			self.color = (0,255,0)
			self.position = [random.randint(900,1000), random.randint(200,1000)]
		else:
			id_layer = "-"
		new_id = str(Neuron.num_neuron)+id_layer+str(id_num)
		return new_id
		
	def update_status(self):
		self.status= self.set_status()

	def update_velocity (self, new_velocity):
		self.velocity = new_velocity
	
	def update_momentum (self):
		new_momentum = 0
		for port in self.ports:
			new_momentum += port.momentum
		return new_momentum

	def connect(self, other_neuron):
		ports = self.get_ports()
		connect_port = random.choice(ports)
		connect_port.set_type_of_connection(type_connection=True)
		self.linked += 1
		self.update_status()
		self.linked_neurons.append(other_neuron)
		other_ports = other_neuron.get_ports()
		connect_other_port = random.choice(other_ports)
		connect_other_port.set_type_of_connection(type_connection=True)
		other_neuron.linked +=1
		other_neuron.update_status()
		other_neuron.linked_neurons.append(self)
		return (connect_port,connect_other_port)

		