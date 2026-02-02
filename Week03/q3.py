# Question 3: Coordinate System
point1 = (3,5)
point2 = (7,2)

# Unpacking: Assigning tuple elements to individual variables (names basically)
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
x1, y1 = point1
x2, y2 = point2

print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")

# Distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Distance between points: {distance}")

# Converting String to tuple
char_tuple = tuple("PYTHON")
print(f"Character tuple: {char_tuple}")
for char in char_tuple:
    print(char)

