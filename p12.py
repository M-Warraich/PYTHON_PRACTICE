# 📘 𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 # 𝟭𝟮 

# 1.)
def double(n):
  return 2 * n
number = 5
factorial_result = math.factorial(number)
doubled_result = double(number)
print(f"Factorial of {number}: {factorial_result}")
print(f"Double of {number}: {doubled_result}")

# 2.
my_list = ["apple", "banana", "cherry", "date"]
random_item = random.choice(my_list)
print(f"Randomly chosen item from the list: {random_item}")
def greet(name):
  print(f"Hello, {name}!")
greet("Alice")
list_length = len(my_list)
print(f"Length of the list: {list_length}")

# 3.
numbers_list = [10, 20, 30, 40, 50]
total_sum = sum(numbers_list)
print(f"Sum of list elements: {total_sum}")
mean_value = statistics.mean(numbers_list)
print(f"Mean of list elements: {mean_value}")
def is_even(num):
  return num % 2 == 0
check_num1 = 7 
check_num2 = 12
print(f"{check_num1} is even: {is_even(check_num1)}")
print(f"{check_num2} is even: {is_even(check_num2)}")

# 4.
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")
def say_hello():
  print("Hello there!")
say_hello()
my_variable = "Python"
print(f"Type of my_variable: {type(my_variable)}")

# 5.
def area_of_circle(radius):
  return math.pi * (radius ** 2)
radius_value = 7 
circle_area = area_of_circle(radius_value)
print(f"Area of a circle with radius {radius_value}: {circle_area}")
print(f"Type of circle_area: {type(circle_area)}")

# 6.
random_int = random.randint(10, 100)
print(f"Generated random number: {random_int}")
def check_number(num):
  return num > 50
print(f"Is {random_int} greater than 50? {check_number(random_int)}")

# 7.
value_list = [100, 55, 120, 88]
max_value = max(value_list)
print(f"Maximum value in the list: {max_value}")
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent}: {power_result}")
def display_info(name, age):
  print(f"Name: {name}, Age: {age}")
display_info("Bob", 30)

# 8.
print("Calendar for May 2025:")
print(calendar.month(2025, 5))
my_string = "Hello World!"
string_length = len(my_string)
print(f"Length of the string '{my_string}': {string_length}")
def show_message():
  print("This is a simple message.")
show_message()

# 9.
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
my_integer = 123
integer_as_string = str(my_integer)
print(f"Integer as string: {integer_as_string}, Type: {type(integer_as_string)}")
def multiply(x, y):
  return x * y
product_result = multiply(7, 8)
print(f"Product of 7 and 8: {product_result}")

# 10.
def calculate_square_root(num):
  if num >= 0:
    return math.sqrt(num)
  else:
    return "Cannot calculate square root of a negative number."
user_input_str = input("Enter a number to find its square root: ")
try:
  user_number = int(user_input_str)
  print(f"Type of user input number: {type(user_number)}")
  square_root_result = calculate_square_root(user_number)
  print(f"Square root of {user_number}: {square_root_result}")
except ValueError:
  print("Invalid input. Please enter an integer.")