# 1) შექმენით for loop'ი რომელიც 0'დან 200'მდე დაპრინტავს ყოველ მეექვსე რიცხვს

for i in range(0, 200, 6):
    print(i)

# 2)  გადაატეთ for loop'ი სტრინგს: "Goodbye World!"

str1 = "Goodbye world"

for i in str1:
    print(i)

# 3) ექმენით for loop'ი რომელიც 1000'დან 0'მდე დაპრინტავს ყველა რიცხვს

for i in range(1000, 0, -1):
    print(i)

# 4) მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.

# age = int(input("Enter your age:"))

# if age >= 18:
#     print("You didn't get discount.")
# else:
#     print("You got 50%' discount.")

# 5)  მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე და 18 წლის ხალხზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას, 18 წლის ადამიანი მიიღებს 25% ფასდაკლებას, ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება და თუ მიიღო რამდენი.

# age = int(input("Enter your age:"))

# if age > 18:
#     print("You didn't get discount.")
# elif age == 18:
#     print("You got 25%' discount.")ლოდ ა
# else:
#     print("You got 50%' discount.")

# 6)  მაღაზიაში ფასდაკლება არის მხორასრულოვნებზე და სტუდენტებზე. არასრუწლოვანი ან სტუდენტი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი ან არასტუდენტი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.

age = int(input("Enter your age:"))
is_student = input("If you are a student enter 1 and if you are not than enter 2: ")
if is_student == "1":
    is_student = True
else:
    is_student = False

if age < 25 or is_student:
    print("u get 50%' discount.")
else:
    print("Regular price.")