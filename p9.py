#📘 𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 # 9

# 1.
marks_str = input("Enter marks: ")
marks = int(marks_str)
if marks >= 40:
  print("Pass")
else:
  print("Fail")

# 2.
ages_str = ["17", "25", "16", "30", "18"]
ages = [int(age) for age in ages_str]
print("Ages 18+:")
for age in ages:
  if age >= 18:
    print(age)

# 3.
num_str = input("Enter a number: ")
num = int(num_str)
if num % 5 == 0 and num % 7 == 0:
  print(f"{num} is divisible by both 5 and 7.")
elif num % 5 == 0:
  print(f"{num} is divisible by 5.")
elif num % 7 == 0:
  print(f"{num} is divisible by 7.")
else:
  print(f"{num} is not divisible by 5 or 7.")

# 4.
numbers_str = ["3", "6", "9", "12"]
numbers = [int(num) for num in numbers_str]
print("Numbers divisible by 6:")
for num in numbers:
  if num % 6 == 0:
    print(num)

# 5.
name = input("Enter your name: ")
age_str = input("Enter your age: ")
age = int(age_str)
if age >= 18:
  print(f"Hello, adult {name}!")
else:
  print(f"Hi, kid {name}!")

# 6.
my_list = [15, 8, 23, 4, 10]
print(f"Highest number: {max(my_list)}")
print(f"Lowest number: {min(my_list)}")

# 7.
number_string = "100200300"
digit_sum = 0
for digit in number_string:
  digit_sum += int(digit)
print(f"Sum of digits: {digit_sum}")

# 8.
password = input("Enter a password: ")
if len(password) >= 8:
  print("Valid password (at least 8 characters).")
else:
  print("Invalid password (less than 8 characters).")

# 9.
mixed_list = [1, "hello", 3.14, True, 10, "world", 20, False]
integer_count = 0
for item in mixed_list:
  if isinstance(item, int):
    integer_count += 1
print(f"Number of integers in the list: {integer_count}")

# 10.
import keyword
print(f"Total number of Python keywords: {len(keyword.kwlist)}")