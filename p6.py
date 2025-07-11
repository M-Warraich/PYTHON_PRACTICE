#📘 𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 # 6

# Question 1
while x in range (1,21):
     print (x)

# Question 2
while a in range (3,31,3):
     print (a)

# Question 3
sum = 0
while b in range (2,21,2):
     sum = sum + b 
     print (sum)

# Question 4
while c in range (1,10,2):
     print (c)

# Question 5
names = ["MUHAMMAD","MOIZ","ALI","SAIM","KHIZER"]
for d in names:
    print (d)

# Question 6
word = "banana"
count = word.count('a')
print(f"The letter 'a' appears {count} times in the word '{word}'.")

# Question 7
mylist = [21,88,25,95,67,55]
for e in mylist:
    if e % 2 ==1
       print (e)

# Question 8
for f in range (1,51)
    if f % 5 == 0
       print (f)

# Question 9
words = ["cat", "elephant", "bat"]
for word in words:
    print(f"The word '{word}' has {len(word)} letters.")

# Question 10
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"The average of the three numbers is: {average}")

# Question 11
print("Table of 5 in reverse:")
for i in range(10, 0, -1):
  print(f"5 x {i} = {5 * i}")

# Question 12
print("\nCharacters in 'Python Is Fun':")
for char in "Python Is Fun":
  print(char)

# Question 13
print("\nEvery second item in a list:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(numbers), 2):
  print(numbers[i])

# Question 14
print("\nConsonant count in a word:")
word = input("Enter a word: ")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
consonant_count = 0
for char in word:
  if char in consonants:
    consonant_count += 1
print(f"The word '{word}' has {consonant_count} consonants.")

# Question 15
print("\nCubes of numbers from 1 to 5:")
for i in range(1, 6):
  print(f"The cube of {i} is {i**3}")

# Question 16
print("\nWords starting with 'a':")
word_list = ["apple", "banana", "apricot", "cherry", "date"]
for word in word_list:
  if word.startswith('a'):
    print(word)

# Question 17
print("\nNumbers between 100 and 110 (excluding 105):")
for i in range(100, 111):
  if i != 105:
    print(i)

# Question 18
print("\nFirst 5 positive multiples of 4:")
for i in range(1, 6):
  print(4 * i)

# Question 19
print("\nWords in 'Coding is easy' on new lines:")
sentence = "Coding is easy"
words = sentence.split()
for word in words:
  print(word)

# Question 20
print("\nEven numbers in a list:")
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
  if number % 2 == 0:
number