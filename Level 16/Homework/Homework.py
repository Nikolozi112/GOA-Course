#2)

Number1 = 1

for i in range(1, 11):
    Number1 *= i

print("1-დან 10-ის ჩათვლით რიცხვების ნამრავლი არის:", Number1)

#3)

Number2 = 1
i = 1

while i <= 10:
    Number2 *= i
    i += 1

print("1-დან 10-ის ჩათვლით რიცხვების ნამრავლი არის:", Number2)

#4)

score = int(input("Your score on the test:"))

if score >=90:
    print("You got A+!")
elif score >= 79:
    print("You got A!")
elif score >= 69:
    print("You got B!")
elif score >=59:
    print("You got C!")
elif score >=49:
    print("You got D!")
elif score >=39:
    print("You got E!")
elif score >=29:
    print("You got C!")
elif score >=19:
    print("You got F!")
elif score <=19:
    print("You got F!")
