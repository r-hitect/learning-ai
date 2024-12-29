import numpy as np

# Exercise 1.1.1 Simple print
print("Hello AI world!")

# Exercise 1.1.2 Simple math
a = 3
b = 5

c = a + b
d = a * b

print(f"The sum of {a} and {b} is {c}")
print(f"The product of {a} and {b} is {d}")


# Exercise 1.1.3 Simple function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(5)
print(f"The factorial of 5 is {f}")

# Exercise 1.1.4 Dictionaries
students_grades = {"Alice": 23, "Bob": 22, "John": 24}

for name, grade in students_grades.items():
    print(f"{name} scored {grade}")

# Exercise 1.1.5 Files
with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.\nWelcome to AI programming.")
with open("sample.txt", "r") as f:
    print(f"File content is: {f.read()}")

# Exercise 1.1.6 Exploring Python Libraries: numpy
arr = np.array([2, 3, 5, 43, 6])
squared_arr = arr**2
print(f"Original Array: {arr}")
print(f"Squared Array: {squared_arr}")
