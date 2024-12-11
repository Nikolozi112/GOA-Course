# 2)  გამოიყენეთ for loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

Number1 = 1

for i in range(1, 11):
    Number1 *= i

print(Number1)

# 3)  გამოიყენეთ while loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

Number2 = 1
i = 1

while i <= 10:
    Number2 *= i
    i += 1

print(Number2)

# 4) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. (hints:       10 % 2 = 0;        5 % 2 = 1)

number = int(input("Enter nummber: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# 5)  მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ ფოტოს მიხედვით: (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)

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