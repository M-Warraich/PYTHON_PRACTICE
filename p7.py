#📘 𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 # 7 

# Question 1
full_name = input("Enter your full name: ")
print("Number of characters:", len(full_name))

# Question 2
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
print("\nNames with more than 5 characters:")
for name in names:
  if len(name) > 5:
    print(name)

# Question 3
sentence = input("\nEnter a sentence: ")
sentence_lower = sentence.lower()
if "python" in sentence_lower:
  print("The word 'python' is present in the sentence.")
else:
  print("The word 'python' is not present in the sentence.")

# Question 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("\nNumbers divisible by 3:")
for number in numbers:
  if number % 3 == 0:
    print(number)

# Question 5
num = int(input("\nEnter a number: "))
if num > 0:
  print("The number is positive.")
elif num < 0:
  print("The number is negative.")
else:
  print("The number is zero.")

# Question 6
num1 = int(input("\nEnter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
  print("The greater number is:", num1)
else:
  print("The greater number is:", num2)

# Question 7
cities = ["London", "Paris", "Tokyo", "New York"]
new_city = input("\nEnter a new city to add: ")
cities.append(new_city)
print("Updated list of cities:", cities)

# Question 8
words = ["apple", "banana", "cherry", "date", "elderberry"]
print("\nWords in reverse order:")
for word in reversed(words):
  print(word)

# Question 9
mark1 = int(input("\nEnter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

print("Total marks:", total_marks)
print("Average marks:", average_marks)

if average_marks >= 90:
  grade = 'A'
elif average_marks >= 80:
  grade = 'B'
elif average_marks >= 70:
  grade = 'C'
else:
  grade = 'Fail'

print("Grade:", grade)

# Question 10
fruits = ["banana", "orange", "grape", "mango"]
if "apple" in fruits:
  print("\nFound")
else:
  print("\nNot Found")