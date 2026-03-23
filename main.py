# ==============================
# 1. Basic Program
# ==============================
print("=== Welcome to Python Learning ===")


# ==============================
# 2. Variables & Data Types
# ==============================
name = "Praneeth"
age = 25
is_devops = True

print("\nUser Info:")
print("Name:", name)
print("Age:", age)
print("DevOps Engineer:", is_devops)


# ==============================
# 3. User Input
# ==============================
user_name = input("\nEnter your name: ")
print("Hello", user_name)


# ==============================
# 4. Condition Example
# ==============================
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible")


# ==============================
# 5. Loops
# ==============================
print("\nFor Loop Example:")
for i in range(1, 6):
    print("Number:", i)

print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# ==============================
# 6. Functions
# ==============================
def greet(name):
    return f"Hello {name}, welcome to DevOps!"

message = greet(user_name)
print(message)


# ==============================
# 7. List Example
# ==============================
tools = ["Docker", "Kubernetes", "Jenkins", "AWS"]

print("\nDevOps Tools:")
for tool in tools:
    print("-", tool)


# ==============================
# 8. Dictionary Example
# ==============================
user = {
    "name": user_name,
    "role": "DevOps Engineer",
    "skills": tools
}

print("\nUser Details:")
for key, value in user.items():
    print(key, ":", value)


# ==============================
# 9. Simple Calculator
# ==============================
print("\n=== Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero")


# ==============================
# 10. File Handling
# ==============================
file_name = "devops_log.txt"

# Write to file
with open(file_name, "w") as f:
    f.write("User: " + user_name + "\n")
    f.write("Role: DevOps Engineer\n")

# Read file
print("\nReading file:")
with open(file_name, "r") as f:
    print(f.read())


# ==============================
# 11. DevOps Automation Example
# ==============================
import os

print("\n=== DevOps Automation ===")

# Create a folder
folder_name = "project_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists")

# Create a file inside folder
file_path = folder_name + "/app.txt"
with open(file_path, "w") as f:
    f.write("This is a DevOps automation file")

print("File created inside folder")


# ==============================
# 12. End Message
# ==============================
print("\n=== Program Completed Successfully ===")