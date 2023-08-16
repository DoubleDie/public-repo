import time

week_hours = 7*24 
waking_hours = 7*14 
tasks = input("How many tasks do you have? ") 
time_per_task = [] 
time_for_tasks = 0 
counter = 1 

for task in range (int(tasks)): 
	time_per_task.append(int(input("Enter how many hours you will need for task %s: "%(str(counter))))) 
	counter += 1 
for x in time_per_task:
	time_for_tasks += x 

free_time = waking_hours - time_for_tasks

print("You will need a total of %s hours to complete all you tasks, leaving %s hours of your week free."%(time_for_tasks, free_time))
time.sleep(4)
while time_for_tasks > 0:
	t = 0.1
	x = 0
	counter_2 = 0

	while counter_2 != 50:
		time.sleep(t)
		counter_2 += 1
		text = 'Do ur work'
		if x <= 14.142:
			height = (-0.08*((x - 7.071067812)*(x - 7.071067812)) + 4) * 20
			for b in range(round(height)):
				text = ' ' + text
			x += 0.5
		else:
			x = 0
		print(text)
		#print(counter_2)
	print(time_for_tasks)
	hours_done = int(input("How much work have you done: "))
	time_for_tasks = time_for_tasks - hours_done
	if time_for_tasks == 0:
		print("Well done, you are free")
		break
	else:
		print("You have %s hours left... you know what that means."%(time_for_tasks))
		time.sleep(4)
