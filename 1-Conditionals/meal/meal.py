


def main():
	meal = input("What's the time? ")
	time = convert(meal)
	if time > 7.0 and time < 8.0:
		print("Breakfast!")
	elif time > 12.0 and time < 13.0:
		print("Lunch!")
	elif time > 18.0 and time < 19.0:
		print("Dinner")
	else:
		print("")
	
	
	

def convert(thing):
	x, y = thing.split(":")
	x = int(x)
	y = int(y)
	return (x + y/60)
	

main()





