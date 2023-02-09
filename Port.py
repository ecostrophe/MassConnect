import random

class Port:
	num_port = 0
	def __init__(self, id_num, degree=None,strength=None):
		self.id_num = self.set_id_num(id_num)
		self.degree_of_connectivity = degree if degree is not None else random.randint(1,10)
		self.strength_of_connection = strength if strength is not None else random.uniform(1, 10)
		self.momentum = self.strength_of_connection / self.degree_of_connectivity
		self.resistance = (1/ self.degree_of_connectivity) * (1 /self.strength_of_connection)
		self.type_of_connection = False
		self.link = []
		Port.num_port += 1
	
	def set_id_num(self,id_num):
		return str(Port.num_port)+"P"+str(id_num)

	def set_type_of_connection(self, type_connection):
		self.type_of_connection = type_connection
