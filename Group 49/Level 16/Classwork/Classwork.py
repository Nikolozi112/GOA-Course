#1)

for i in range(0, 200, 6):
    print(i)

#2)

str1 = "Goodbye world"

for i in str1:
    print(i)

#3)

for i in range(100, 0, -1):
    print(i)

#4)

age = int(input("Enter your age:"))

if age >= 18:
    print("You didn't get discount.")
else:
    print("You got 50%' discount.")

#5)

age = int(input("Enter your age:"))

if age > 18:
    print("You didn't get discount.")
elif age == 18:
    print("You got 25%' discount.")
else:
    print("You got 50%' discount.")

#6)

age = int(input("Enter your age:"))
is_student = False

if age < 18 or is_student:
    print("You got 50%' discount.")
else:
    print("Regular price.")