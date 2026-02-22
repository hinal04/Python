#string concat 

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

#string len

text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

#string case

text = "Python is awesome"

uppercase = text.upper()
lowercase = text.lower()

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#string replace

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Replaced text:", new_text)

#string split

text = "Python is awesome"

words = text.split()

print("Words:", words)

print("First word:" , words[0])

print("Last word:" , words[-1:])

#string strip

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

#string substring
count=0
text = "Python is awesome. Python is used widely.Python is easy language is"
substring = "is"
if substring in text:
    print(substring, "found in the text")
    count = text.count(substring)
    print(count)

# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2s
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)

# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)