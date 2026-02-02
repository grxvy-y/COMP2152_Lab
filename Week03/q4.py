# Question 4: Class Attendance Logic
monday_class = {"Alice", "Bob", "Charlie", "David"}
wednesday_class = {"Charlie", "David", "Eve", "Frank"}

monday_class.add("Grace")  # New student joins Monday class

# & (Intersection): Only students present in BOTH sets
both = monday_class & wednesday_class

# | (Union): Everyone from both sets combined (no duplicates)
all_students = monday_class | wednesday_class

# - (Difference): Students in Monday who are NOT in Wednesday
monday_only = monday_class - wednesday_class

# ^ (Symmetric Difference): Students who attended ONLY one day (not both)
only_one_day = monday_class ^ wednesday_class

# <= (Subset): Check if all Monday students attended Wednesday
is_monday_subset = monday_class <= all_students

print(f"Monday Class: {monday_class}")
print(f"Wednesday Class: {wednesday_class}")
print(f"Attended Both Classes: {both}")
print(f"Attended either Students: {all_students}")
print(f"Monday Only: {monday_only}")
print(f"Only One class (not both): {only_one_day}")
print(f"Is Monday Subset of all students?: {is_monday_subset}")
