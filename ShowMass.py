import pygame
from MassConnect import MassConnect

#pygame.init()
window = pygame.display.set_mode((1000, 1000),pygame.RESIZABLE)

#Varible
run = True
clock=pygame.time.Clock()
#creat a Neural network
mass = MassConnect(input_layer_neurons=5,output_layer_neurons=2)
mass.add_hidden_layer(num_neurons=20)
mass.add_hidden_layer(num_neurons=50)
mass.add_hidden_layer(num_neurons=10)
mass.connect_layers()

#Fill the screen
window.fill((255,255,255))
#Start tests and display
while run:
	#Show the neurons
	for in_l in mass.input_layer.neurons:
		pygame.draw.circle(window,in_l.color,(in_l.position[0],in_l.position[1]),in_l.dim,0)
		pygame.display.update()
	for o_l in mass.output_layer.neurons:
		pygame.draw.circle(window,o_l.color,(o_l.position[0],o_l.position[1]),o_l.dim,0)
		pygame.display.update()
	for h_lst in mass.hidden_layers:
		for h_l in h_lst.neurons:
			pygame.draw.circle(window,h_l.color,(h_l.position[0],h_l.position[1]),h_l.dim,0)
			pygame.display.update()
	#
	for lin_l in mass.linked_neurons:
		s= lin_l[2].x_pos
		f= lin_l[2].y_pos
		l_color = lin_l[2].color
		pygame.draw.lines(window, l_color, False, [s,f],1)

	pygame.display.update()
	clock.tick(50)
	#The differents events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()

