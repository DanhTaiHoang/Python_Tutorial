answer = input('Do you want to continue? ')
if answer.lower().startswith("y"):
	print("ok, carry on then")
elif answer.lower().startswith("n"):
	print("the program will stop here")
	exit()

for i in range(10):
	print(i)

