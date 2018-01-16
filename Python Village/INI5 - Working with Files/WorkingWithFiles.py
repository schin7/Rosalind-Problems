with open('C:/Users/Owner/Desktop/rosalind_ini5.txt') as input_data:
	lines = [line.strip() for line in input_data.readlines()]

with open('C:/Users/Owner/Desktop/output_ini5.txt', "w") as output_data:
	output_data.write(lines[1])
	for i in range(3,len(lines), 2):
		output_data.write('\n'+lines[i])