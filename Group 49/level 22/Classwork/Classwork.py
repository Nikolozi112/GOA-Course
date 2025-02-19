# 1) შექმენით ფუნქცია რომელიც ტერმინალში გამოიტანს goodbye world'ს.

def goodbye_world():
    print("Goodbye, World!")

goodbye_world()


# 2) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სახელს და გამოიტანს დამშვიდობებას.

def goodbye_name(name):
    print(f"Goodbye, {name}!")

goodbye_name("Nika")


# 3) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს 2 რიცხვს და გამოიტანს მათ ჯამს.

def sum_numbers(a, b):
    print(f"Sum: {a + b}")

sum_numbers(3245, 325662)


# 4) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს list'ს და გამოიტანს პირველ 3 რიცხვს.

def print_3(numbers):
    print(numbers[:3])

print_3([13, 124, 95, 24, 764])
