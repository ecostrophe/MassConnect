import math

class Link:
	"""
	The Link class represents a connection between two neurons
	"""
	linked_neurons = []
	def __init__(self, n_start, n_finish):
		self.id_link = self.set_id_link(n_start,n_finish)
		self.x_pos = n_start.position
		self.y_pos = n_finish.position
		self.length = math.dist(self.x_pos, self.y_pos)
		self.time = n_finish.velocity / self.length
		self.acceleration = (n_finish.velocity - n_start.velocity) / self.time
		self.color = (0,0,0)
		print("id link:",self.id_link)

	def set_id_link(self,n_start,n_finish):
		return n_start.id_num+"SL"+str(len(Link.linked_neurons))+"LF"+n_finish.id_num

	def update_resistance(self):
	 #new_resistance =(degree_of_connectivity * self.length)/ strength_of_connection
	 pass
