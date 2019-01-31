#PJ Mallery
#Assignment 3 part 1
#python3

#initialize variables
num_large = None
num_small = None
num_sum = 0
num_count = 0

#Begin loop
while True:
	user_num = input("Enter a number: ")  #input entered as string, need to convert
	if user_num = "done":
		break
	else:
		try:
			real_num = float(user_num)
			num_sum = num_sum + real_num
			num_count += 1
			if num_large is None or num_large < real_num:
				num_large = real_num
			if num_small is None or num_small > real_num:
				num_small = real_num
		except:
			print("Not a valid number, please try again. Type done to finish entering numbers.")
			continue
			
#Average involves division, so make sure to avoid divide by 0
if num_count == 0:
	print("No numbers entered, could not compute total, average, count, max, or min.")
else:
	num_avg = num_sum / num_count
	print("Total: " + str(num_sum))
	print("Average: " + str(num_avg))
	print("Count: " + str(num_count))
	print("Maximum: " + str(num_large))
	print("Minimum: " + str(num_small))
