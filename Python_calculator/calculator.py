# input from user
print("Welcome to Python Calculator /n")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num1 = float(num1)
num2 = float(num2)
choice = input("Enter your choice (+, -, *, /): ")

# functions to do add, subs, divide, multiply
def add(a, b):
	return a+b

def subs(a, b):
	return a-b

def multiply(a, b):
	return a*b

def divide(a, b):
	return a/b
	


# fucntion to calculate
def calculate(num1, num2, choice):
	if choice == '+':
		return add(num1, num2)
	elif choice == '-':
		return subs(num1, num2)
	elif choice == '*':
		return multiply(num1, num2)
	elif choice == '/':
		return divide(num1, num2)
	else:
		print("Wrong input")

# fucntion to validate and execute
def validate_and_execute(num1, num2):
	try:
		if num1 < num2:
			print("First number must be greater than second one. Try again.")
		else:
			# print the result
			result = calculate(num1, num2, choice)
			print("Result = ", result)
	except ValueError:
		print("Wrong inputs. Please do not ruin my program.")
	
# print the result
validate_and_execute(num1, num2)

