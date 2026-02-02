# Question 1: Student Grades
grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()

print("======================")
print("Student Grades\n")
print(f"Sorted grades: {grades}")
print(f"Highest grades: {grades[-1]}") # Negative indexing starts from the end
print(f"Lowest grades: {grades[0]}")
print(f"Total number of grades: {len(grades)}")


# Question 2: Shopping Cart
print("======================")
print("Shopping Cart\n")
cart = ["apple","banana","milk","bread","apple","eggs"]

print(f"Number of apples: {cart.count('apple')}")
print(f"Position of milk: {cart.index('milk')}") # index is to find where the item is

cart.remove("apple") # Removes the first occurence
removed_item = cart.pop() # pop Removes and returns the last item
print(f"Removed item using pop: {removed_item}")
print(f"Is banana in cart? {'banana' in cart}")
print(f"Final cart: {cart}")





