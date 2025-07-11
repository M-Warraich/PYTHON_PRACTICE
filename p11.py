#📘 𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 # 𝟭𝟭 

# 1.
print("--- Task 1 ---")
my_set = {10, 20, 30}
my_set.add(50)
my_set.update([40, 60])
print(my_set)
print("\n")

# 2.
print("--- Task 2 ---")
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print("After removing 'banana' (present):", fruits)
try:
  fruits.remove("orange")
except KeyError as e:
  print(f"Error when using remove() for 'orange' (not present): {e}")
fruits.discard("orange")
print("After using discard() for 'orange' (not present): No error")
fruits.discard("apple")
print("After using discard() for 'apple' (present):", fruits)
print("\n")

# 3.
print("--- Task 3 ---")
colors = {"red", "green", "blue"}
print("Initial set:", colors)
popped_item = colors.pop()
print(f"After popping one item ({popped_item}):", colors)
colors.clear()
print("After clearing the set:", colors)
print("\n")

# 4.
print("--- Task 4 ---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
print("Union:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)
difference_set1_2 = set1.difference(set2)
print("Difference (set1 - set2):", difference_set1_2)
difference_set2_1 = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2_1)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)
print("\n")

# 5.
print("--- Task 5 ---")
A = {1, 2, 3}
B = {1, 2}
is_b_subset_a = B.issubset(A)
print(f"Is B a subset of A? {is_b_subset_a}")
is_a_superset_b = A.issuperset(B)
print(f"Is A a superset of B? {is_a_superset_b}")
are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint? {are_disjoint}")
print("\n")

# 6.
print("--- Task 6 ---")
vowels_frozenset = frozenset(['a', 'e', 'i', 'o', 'u'])
print("Frozenset:", vowels_frozenset)
try:
  vowels_frozenset.add('z')
except AttributeError as e:
  print(f"Caught expected error when trying to add: {e}")
try:
  vowels_frozenset.remove('a')
except AttributeError as e:
  print(f"Caught expected error when trying to remove: {e}")

print("Frozenset remains unchanged because it is immutable.")
print("\n")

# 7.
print("--- Task 7 ---")
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])
union_fs = fs1.union(fs2)
print("Union of frozensets:", union_fs)
intersection_fs = fs1.intersection(fs2)
print("Intersection of frozensets:", intersection_fs)
difference_fs1_2 = fs1.difference(fs2)
print("Difference (fs1 - fs2) of frozensets:", difference_fs1_2)
symmetric_difference_fs = fs1.symmetric_difference(fs2)
print("Symmetric Difference of frozensets:", symmetric_difference_fs)
print("\n")

# 8.
print("--- Task 8 ---")
cities = {"Lahore", "Karachi", "Islamabad"}
check_cities = ["Lahore", "Multan", "Karachi"]
print("Checking membership:")
for city in check_cities:
  if city in cities:
    print(f"{city} is in the set of cities.")
  else:
    print(f"{city} is NOT in the set of cities.")
new_cities = {"Peshawar", "Quetta"}
are_cities_disjoint = cities.isdisjoint(new_cities)
print(f"Are the sets of cities and new_cities disjoint? {are_cities_disjoint}")
another_cities = {"Faisalabad", "Lahore"}
are_cities_disjoint_another = cities.isdisjoint(another_cities)
print(f"Are the sets of cities and another_cities disjoint? {are_cities_disjoint_another}")
print("\n")


# 9.
print("--- Task 9 ---")
setA = {1, 2, 3}
setB = {3, 4, 5}
union_result = setA | setB
print("setA | setB (Union):", union_result)
intersection_result = setA & setB
print("setA & setB (Intersection):", intersection_result)
difference_result = setA - setB
print("setA - setB (Difference):", difference_result)
symmetric_difference_result = setA ^ setB
print("setA ^ setB (Symmetric Difference):", symmetric_difference_result)
print("\n")

# 10.

print("--- Task 10 ---")
user_input_list_str = input("Enter a list of items separated by commas (e.g., apple, banana, cherry): ")
user_items_list = [item.strip() for item in user_input_list_str.split(',')]
user_items_set = set(user_items_list)
print("User input list:", user_items_list)
print("Converted to set:", user_items_set)
print("\n")