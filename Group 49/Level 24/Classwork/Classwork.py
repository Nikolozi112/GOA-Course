#1)დღეს რომელი ფუნქციები და მეთოდები ვისწავლეთ, გატესტეთ ყველა: 
# len(), .append(), .insert(), .pop(), .remove()

my_list = [10, 20, 30, 40]
print(len(my_list))  

my_list.append(40)
print(my_list)  

my_list.insert(2, 12) 
print(my_list) 

removed_element = my_list.pop(3)  
print(my_list)  
print(removed_element)  

my_list.remove(20)  
print(my_list)  

#2).pop() მეთოდის გამოყენებით გამოაცალკევეთ კონკრეტული ელემენტი 
# list'ისგან და ჩასვით ცალკე ცვლადში ზუსტად ისე როგორც მე გავაკეთე

my_list = [10, 20, 30, 40]
variable = my_list.pop(2)
print(variable)
print(my_list)


#3)ახსენით განხსვავება pop'სა და remove'ს შორის

# pop() ფუნქცია ლისტიდან ამიაგდებს ელემენტს ინდექსით ხოლო remove()-ით კი თვითონ იმ ელემენტის სახელით.


#4)შექმენით 4 ელემენტიანი list'ი და შუაში ჩაამატეთ 1 ელემენტი

my_list = [34, 73, 59, 64]
my_list.insert(2, 12) 
print(my_list)
