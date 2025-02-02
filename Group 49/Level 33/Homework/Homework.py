# 1) Write a Python program that takes a user's name and age as input. Use the format() function to create a sentence that says, "Hello, [Name]! You are [Age] years old."

name = input("Enter your name: ")
age = input("Enter your age: ")

msg = "Hello, {}! You are {} years old.".format(name, age)
print(msg)


# 2) Given a list of words ["Python", "is", "fun"], use the join() function to combine them into a single string, separated by spaces. The result should be "Python is fun".

words = ["Python", "is", "fun"] 
word = " ".join(words) 
print(word)


# 3) Write a program that asks the user to input a sentence. Use the split() function to break the sentence into a list of words. Print the list of words.

sentence = input("Enter a sentence: ") 
words = sentence.split() 
print("List of words:", words)


# 4) Create a program that asks the user for a sentence and a word to replace. Then, ask for the new word to replace it with. Use the replace() function to make the substitution and print the modified sentence.

txt = input("Enter a sentence: ") 
old_word= input("Enter the word to replace: ") 
new_word= input("Enter the new word: ") 
Changed_txt = txt.replace(old_word, new_word) 
print("New sentence:", Changed_txt)


# 5) Write a Python script that takes a mixed-case string and converts it entirely to lowercase using the lower() function.

text = input("Please enter a mixed-case string: ")

lowercase = text.lower()

print("Lowercase version:", lowercase)


# 6) Create a program that asks the user to input a sentence and then converts the entire sentence to uppercase using the upper() function 
 
txt = input("Please enter a text: ")

uppercase = txt.upper()

print("Uppercase version:", uppercase)