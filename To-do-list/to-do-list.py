# create an empty list
to_do_list = []

# create a while loop to keep the program running
while True:
	task = input("Enter a task, or enter 'done' to end: ")

	#if press done
	if task == 'done':
		break
	else:
		to_do_list.append(task)

print("The entered tasks are: ")

for i in to_do_list:
	print(i)