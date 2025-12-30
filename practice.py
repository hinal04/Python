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