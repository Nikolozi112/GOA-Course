# 2)  1. გამოიტანეთ ყველა ელემენტი სიიდან დადებითი ინდექსირებით.
#     2. გამოიტანეთ ყველა ელემენტი სიიდან უარყოფითი ინდექსაციით.
#     3. შეცვალეთ სიის ბოლო ელემენტი ახალი მნიშვნელობით.
#     4. შეცვალეთ სიის მეხუთე ელემენტი ახალი მნიშვნელობით.

list1 = [2, 51, 11, 13, 51, 100]

# 1.
print(list1[0: 7])
# 2.
print(list1[-6: ])
# 3.
list1.insert(6, 234) 
print(list1)
# 4.
list1.insert(5, "six") 
print(list1)