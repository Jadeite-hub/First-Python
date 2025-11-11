word1 = 'Hello'
word2 = "Welcome"
word3 = """to Python class"""
print(word1, word2, word3)

sentence = "Python is fun to learn!"
print(sentence)

message = """Python is powerful.
It is easy to learn.
It is loved by developers."""
print(message)

text = "PYTHON"

first_char = text[0]
third_char = text[2]
last_char = text[-1]

print("First character:", first_char)
print("third character:", third_char)
print("last character:", last_char)

language = "Python"
for ch in language:
    print(ch)

fruit = "Banana" 
print("Length of", fruit, "is",
len(fruit))   

word = "Learning Python is cool"
if "Python" in word:
    print("Yes, 'Python' is found!")
else:
    print("'Python' is not found.") 

if "Java" not in word:
    print("'Java' is not found in the sentence.")
else:
    print("'Java' is found in the sentence.")

message = "Coding is fun"
count_n = 0

for ch in message:
    if ch == "n" :
        count_n += 1

print("Total 'n' found:", count_n)

poem = """I like Python for many reasons.
It makes tasks simple and readable.
Its community and libraries are srong."""
print(poem.upper())




#ASSIGNMENT 2

name = "Ada"
age = 18
school = "Bright Future Academy"

print("My name is " + name + ", I am " + 
str(age) + " years old, and I attend " + school + ".")

country = "Nigeria"
capital = "Abuja"

print("The capital of " + country + " is " + capital + ".")

first_name = "John"
middle_name = "Paul"
last_name = "Okoro"

print("Full name: " + first_name + " " + middle_name + " " + last_name)

food = "Rice"
drink = "Juice"

print("I love eating " + food + " with " + drink + ".")

b = "Hello, World"
print(b[2:5])

#Slicing from the start

name = "Hello, World"
print(name[:5])
