def min(list):
	check = 0
	for num_1 in list:
		for num_2 in list:
			if num_1 > num_2: 
				check = 0
			else:
				check = 1
		if check == 1:
			return num_1

print(min([4,5,6,4,7,8,1]))