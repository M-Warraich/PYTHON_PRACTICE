#📘 𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 # 𝟭𝟬 

# 1.
str_list = ["15", "25", "40"]
int_tuple = tuple(int(s) + 10 for s in str_list)
for item in int_tuple:
  print(f"Value: {item}, Type: {type(item)}")
  if item > 30:
    print("Label: Value > 30")
  else:
    print("Label: Value <= 30")
print("\n")

# 2.
name = input("Enter your name: ")
age_str = input("Enter your age: ")
city = input("Enter your city: ")
try:
  age_int = int(age_str)
  user_dict = {"name": name, "age": age_int, "city": city}
  user_tuple = (name, age_int, city)
  print("User Dictionary:", user_dict)
  print("User Tuple:", user_tuple)
  if age_int >= 18:
    print("Eligible for voting.")
  else:
    print("Not eligible for voting.")
except ValueError:
  print("Invalid age input. Please enter a valid number for age.")
print("\n")

# 3.
marks_str = ["55", "45", "85", "35"]
marks_dict = {}
for mark_str in marks_str:
  mark_int = int(mark_str)
  status = "Pass" if mark_int >= 50 else "Fail"
  marks_dict[mark_int] = status
for mark, status in marks_dict.items():
  print(f"Mark: {mark}, Type: {type(mark)}, Status: {status}")
print("\n")

# 4.
student_tuple = ("Farah", "20", "88.5")
student_dict = {}
name = student_tuple[0]
age = int(student_tuple[1])
score = float(student_tuple[2]) + 5.0
student_dict = {"name": name, "age": age, "score": score}
for key, value in student_dict.items():
  print(f"{key}: {value}")
print("\n")

# 5.
names = ["Ana", "Sana", "Salman"]
names_longer_than_4 = 0
name_length_dict = {}
for name in names:
  name_length = len(name)
  name_length_dict[name] = name_length
  if name_length > 4:
    names_longer_than_4 += 1
  if name_length <= 4:
    label = "short"
  elif name_length <= 6:
    label = "medium"
  else:
    label = "long"
  name_length_dict[name] = (name_length, label)
print(f"Number of names longer than 4 letters: {names_longer_than_4}")
for name, (length, label) in name_length_dict.items():
    print(f"Name: {name}, Length: {length}, Label: {label}")
print("\n")

# 6.
product_dict = {}
for i in range(3): 
    product_name = input(f"Enter product {i+1} name: ")
    product_price_str = input(f"Enter price for {product_name}: ")
    try:
        product_price_float = float(product_price_str)
        product_dict[product_name] = product_price_float
    except ValueError:
        print(f"Invalid price entered for {product_name}. Skipping.")
print("\nProduct Prices:")
for name, price in product_dict.items():
  if price > 100:
    print(f"{name}: {price} (HIGHLIGHT: Above 100)")
  else:
    print(f"{name}: {price}")
print("\n")

# 7.
mixed_list = ["100", 200, 300.5, "400"]
float_list = [float(item) for item in mixed_list]
print("Converted to Floats:")
for item in float_list:
  print(f"Value: {item}")
  if item > 250:
    print("Category: Above 250")
  else:
    print("Category: Below 250")
print("\n")

# 8.
student_info_tuple = ("Ali", "25", "True")
student_info_dict = {}
name = student_info_tuple[0]
age = int(student_info_tuple[1])
is_student_str = student_info_tuple[2]
is_student = is_student_str.lower() == 'true' 
student_info_dict = {"name": name, "age": age, "is_student": is_student}
print("Student Information:")
for key, value in student_info_dict.items():
  print(f"{key}: {value}")
if student_info_dict["is_student"]:
  print("This person is a student.")
else:
  print("This person is not a student.")
print("\n")

# 9.
subjects_dict_str = {"Math": "90", "English": "85"}
subjects_dict_int = {subject: int(score_str) for subject, score_str in subjects_dict_str.items()}
total_score = sum(subjects_dict_int.values())
average_score = total_score / len(subjects_dict_int)
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")
if average_score >= 90:
  grade = 'A'
elif average_score >= 80:
  grade = 'B'
elif average_score >= 70:
  grade = 'C'
elif average_score >= 60:
  grade = 'D'
else:
  grade = 'F'
print(f"Grade: {grade}")
print("\n")

# 10.
gadgets_list = []
for i in range(5):
  gadget_name = input(f"Enter gadget name {i+1}: ")
  gadgets_list.append(gadget_name)
print("Gadget Names entered:", gadgets_list)
print("\n")