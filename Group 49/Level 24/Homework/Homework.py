#3)შექმენით list'ი და ამოაგდეთ მეექვსე ელემენტი ინდექსის მეშვეობით (pop) 

my_list = [10, 20, 30, 40, 50, 60]
removed_element = my_list.pop(5)  
print(my_list)

#4)შექმენით list'ი და ამოაგდეთ მეორე ელემენტი მნიშვნელობის მეშვეობით (remove)

my_list = [10, 20, 30, 40]
my_list.remove(20)  
print(my_list)  

#5)შექმენით list'ი და ბოლოში ჩაამატეთ ახალი ელემენტი

my_list = [10, 20, 30, 40]
my_list.append(50)
print(my_list)

#6) შექმენით list'ი და მეორე ელემენტად ჩაამატეთ ახალი ელემენტი

my_list = [10, 20, 30, 40]
my_list.insert(1, 15) 
print(my_list) 

#7)შექმენით list'ი და ამოშალეთ ბოლო ელემენტი

my_list = [10, 20, 30, 40]
removed_element = my_list.pop(3)  
print(my_list)

#8)შექმენით list'ი და დათვალეთ რამდენი ელემენტია შიგნით

my_list = [10, 20, 30, 40]
print(len(my_list))  
