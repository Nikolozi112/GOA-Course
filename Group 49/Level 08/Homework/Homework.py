# 2) ჩამოწერეთ რომელი data type'ბი იცით და ახსენით რა რას ემსახურება

# integer - ყველა დადებითი და უარყოფითი რიცხვები.
# string - ყველა სიტვა ან წინადადება.
# float - ყველა ათწილადური რიცხვი.
# boolean - True და False.

# 3) თქვენი სიტყვებით ახსენით რაში გვჭირდება მონაცემთა ტიპის შეცვლა, მაგალითად string'ის integer'ად გადაქცევა

# მონაცემთა ტიპის ცვლილება გვჭირდება იმისთვის, რომ მათზე მოვახდინოთ სხვადასხვა ოპერაციები, როგორიცაა კონკატინაცია.ასევე იმისათვის რომ ციფრები ერთანეტს დავუმატოთ და არა შევატყუპოთ.მაგრამ რაც ყველაზე მთავარია სტრინგს ინტეჯერს ვერ დაუმატებთ.


# 4) მომხმარებელს შემოატანინეთ რაიმე მონაცემი, შეამოწმეთ როგორი ტიპისაა და ახსენით რატომაა ასე

user_input = input("Enter something: ")

print(type(user_input))

# 5) გატესტეთ ეს კოდი

print(10 < 1)

# დააკვირდით რა შედეგს გამოიტანს და ივარაუდეთ რატომ ქნა ასე

# ტერმინალში გამოჩნა False რადგან 1 არ არის მეტი 10-ზე ასევე "<" შედარების ოპერატორია, რომელიც აბრუნებს True-ს ან False-ს.