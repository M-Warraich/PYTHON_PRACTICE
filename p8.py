#📘 𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 # 8

# 1.
float_strings = ["1.5", "2.8", "3.0"]
float_numbers = [float(f_str) for f_str in float_strings]
sum_of_floats = sum(float_numbers)
print(f"Sum of floats: {sum_of_floats}")
print("-" * 20)

# 2.
try:
  num_str = input("Enter a number: ")
  num = float(num_str)
  if num > 0:
    print("The number is positive.")
  elif num < 0:
    print("The number is negative.")
  else:
    print("The number is zero.")
except ValueError:
  print("Invalid input. Please enter a valid number.")
print("-" * 20)

# 3. 
try:
  num_str1 = input("Enter the first integer: ")
  num_str2 = input("Enter the second integer: ")
  int_num1 = int(num_str1)
  int_num2 = int(num_str2)
  sum_of_ints = int_num1 + int_num2
  print(f"Sum of integers: {sum_of_ints}, Type: {type(sum_of_ints)}")
except ValueError:
  print("Invalid input. Please enter valid integers.")
print("-" * 20)

# 4.
mixed_list = ["5", 8, 10.5, True]
converted_list = []
for item in mixed_list:
  if isinstance(item, str):
    try:
      converted_list.append(int(item))
    except ValueError:
      converted_list.append(item) 
  else:
    converted_list.append(item)
print(f"Original list: {mixed_list}")
print(f"Converted list: {converted_list}")
print("-" * 20)

# 5.
try:
  mark1_str = input("Enter mark 1: ")
  mark2_str = input("Enter mark 2: ")
  mark3_str = input("Enter mark 3: ")
  mark1 = int(mark1_str)
  mark2 = int(mark2_str)
  mark3 = int(mark3_str)
  total_marks = mark1 + mark2 + mark3
  percentage = (total_marks / 300) * 100
  print(f"Total marks: {total_marks}")
  print(f"Percentage: {percentage:.2f}%")
except ValueError:
  print("Invalid input. Please enter valid integers for marks.")
print("-" * 20)

# 6.
float_str_value = "4.2"
float_value = float(float_str_value)
result = float_value * 2
print(f"String float: {float_str_value}")
print(f"Float value: {float_value}")
print(f"Result multiplied by 2: {result}")
if result > 5:
  print("Result is greater than 5.")
else:
  print("Result is not greater than 5.")

print("-" * 20)

# 7.
marks_strings = ["65", "45", "78", "30"]
passing_mark = 50
print("Checking marks for pass/fail:")
for mark_str in marks_strings:
  try:
    mark = int(mark_str)
    if mark >= passing_mark:
      print(f"Mark {mark}: Pass")
    else:
      print(f"Mark {mark}: Fail")
  except ValueError:
    print(f"Invalid mark (not an integer): {mark_str}")

print("-" * 20)

# 8.
email = input("Enter an email address: ")
if "@" in email:
  print("Valid email address (contains '@').")
else:
  print("Invalid email address (does not contain '@').")

print("-" * 20)

# 9.
sentence = input("Enter a sentence: ").lower()
word_count = sentence.split().count("the")
print(f"The word 'the' appears {word_count} times.")

print("-" * 20)

# 10.
numbers_as_strings = [str(i) for i in range(1, 11)]
numbers_as_ints = [int(num_str) for num_str in numbers_as_strings]
even_numbers = [num for num in numbers_as_ints if num % 2 == 0]
print(f"Original list of numbers (as strings): {numbers_as_strings}")
print(f"Even numbers from the list: {even_numbers}")