import xlsxwriter

class StockData:
	def __init__(self, connections):
		row=0
		col=0
		workbook = xlsxwriter.Workbook('connectionsData.xlsx')
		worksheet = workbook.add_worksheet()
		# Add header row
		header_row = ["Connection ID","Neuron ID", "Start Port", "Start Color", "Start Dimension", "Start Position", "Start Linked", "Start Weight", "Start Momentum", "Start Velocity", "Start Status",
		"ID Start Port","Start Port Degree","Start Port Strength", "Start Port Resistence","Start Port Connection",
		"Link Length", "Link Time", "Link Acceleration", "Link Color",
		"Neuron ID", "End Port", "End Color", "End Dimension", "End Position", "End Linked", "End Weight", "End Momentum", "End Velocity", "End Status",
		"ID Finish Port","Finish Port Degree","Finish Port Strength", "Finish Port Resistence","Finish Port Connection"]
		for i, header in enumerate(header_row):
			worksheet.write(row, i, header)
		row += 1

		# Write data for each connection
		for n in range(len(connections)):
			#collect the data of the start neuron
			worksheet.write(row, col , str(n))
			worksheet.write(row, col+1, connections[n][0].id_num)
			worksheet.write(row, col+2, len(connections[n][0].ports))
			worksheet.write(row, col+3, str(connections[n][0].color))
			worksheet.write(row, col+4, connections[n][0].dim)
			worksheet.write(row, col+5, str(connections[n][0].position))
			worksheet.write(row, col+6, connections[n][0].linked)
			worksheet.write(row, col+7, connections[n][0].weight)
			worksheet.write(row, col+8, connections[n][0].momentum)
			worksheet.write(row, col+9, connections[n][0].velocity)
			worksheet.write_boolean(row, col+10, connections[n][0].status)
			#collect the data of the port of the start neuron
			worksheet.write(row, col+11, connections[n][1][0].id_num)
			worksheet.write(row, col+12, connections[n][1][0].degree_of_connectivity)
			worksheet.write(row, col+13, connections[n][1][0].strength_of_connection)
			worksheet.write(row, col+14, connections[n][1][0].resistance)
			worksheet.write_boolean(row, col+15, connections[n][1][0].type_of_connection)
			#collect the data of the link
			worksheet.write(row, col+16, connections[n][2].length)
			worksheet.write(row, col+17, connections[n][2].time)
			worksheet.write(row, col+18, connections[n][2].acceleration)
			worksheet.write(row, col+19, str(connections[n][2].color))
			#collect the data of the finish neuron
			worksheet.write(row, col+20, connections[n][3].id_num)
			worksheet.write(row, col+21, len(connections[n][3].ports))
			worksheet.write(row, col+22, str(connections[n][3].color))
			worksheet.write(row, col+23, connections[n][3].dim)
			worksheet.write(row, col+24, str(connections[n][3].position))
			worksheet.write(row, col+25, connections[n][3].linked)
			worksheet.write(row, col+26, connections[n][3].weight)
			worksheet.write(row, col+27, connections[n][3].momentum)
			worksheet.write(row, col+28, connections[n][3].velocity)
			worksheet.write_boolean(row, col+29, connections[n][3].status)
			#collect the data of the port of the finish neuron
			worksheet.write(row, col+30, connections[n][1][1].id_num)
			worksheet.write(row, col+31, connections[n][1][1].degree_of_connectivity)
			worksheet.write(row, col+32, connections[n][1][1].strength_of_connection)
			worksheet.write(row, col+33, connections[n][1][1].resistance)
			worksheet.write_boolean(row, col+34, connections[n][1][1].type_of_connection)
			row+=1
		workbook.close()

