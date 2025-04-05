# 2)  შექმენით ფუნქცია რომელიც დააბრუნებს "You got discount" თუ მომხმარებელი არის არასრულწლოვანი, სხვა შემთხვევაში დააბრუნებს "You didn't get discount".

def discount():

    age = int(input("Enter your age: "))

    if age <= 18:
        print("You got discount")
    else:
        print("You didn't get discount")

print(discount())

# 3) შექმენით ფუნქცია manual_reverse, რომელიც არგუმენტად მიიღებს 
# string'ს და დააბრუნებს ამ string'ს ოღონდ შეტრიალებულად.

def manual_reverse(list):

    print(list[::-1])

manual_reverse("GOA is best!")


# 4) გატესტეთ .upper(), .lower(), .capitalize(), .swapcase() და .find() მეთოდები.

text = "Hello, NIKA!"

print(text.upper())

print(text.lower())

print(text.capitalize())

print(text.swapcase())

print(text.find("!"))


# 5) ახსენით რატომ ჰქვიათ ამ ფუნქციებს მეთოდები.

# მეთოდები არის ფუნქციები, რომლებიც კონკრეტულ ობიექტთან (მაგალითად, string-თან) 
# არის დაკავშირებული და მუშაობენ კონკრეტული მონაცემების კონტექსტში.


# 6) ახსენით რა არის dot notation და რა შემთხვევაში გამოიყენება.

# გამოიყენება ობიექტების მეთოდებისა და ატრიბუტების გამოსაძახებლად.