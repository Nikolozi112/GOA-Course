distance = 11949.3792  #კმ
speed = 885.1392 #კმ/სთ

time = distance / speed

print(f"flight time: {time} hours")




bill = float(input("Enter the bill amount: "))

tip = bill * 0.2

print(f"Tip amount: {tip}")




weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight / (height ** 2)


if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI < 25:
    category = "Normal"
elif 25 <= BMI < 30:
    category = "Overweight"
else:
    category = "Obesity"


print(f"Your BMI is: {BMI:.1f}")
print(f"Category: {category}")



def search(text, word):
    
    if word in text:
        return "Word found"
    else:
        return "Word not found"


text = input("Enter the text: ")
word = input("Enter the word to search for: ")


print(search(text, word))