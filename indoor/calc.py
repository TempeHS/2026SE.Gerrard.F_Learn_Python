def payment():
		dollars = dollars_to_float(input("How much was the meal? "))
		percent = percent_to_float(input("What percentage would you like to tip? "))
		tip = dollars * percent
		print(f"Leave ${tip:.2f}")

def percent_to_float(d):
    return float(d)

def dollars_to_float(t):
    return float(t) * 0.01


payment()
