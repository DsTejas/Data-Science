import re

text = "My age is 25 and my brother is 30"
result = re.findall(r'\d+', text)
print(result)

text = "User_name123"
result = re.findall(r'\w+', text)
print(result)


text = "cat, cut, cot"
result = re.findall(r'c.t', text)
print(result)


text = "Hello world"
result = re.findall(r'^Hello', text)
print(result)


text = "I love Python"
result = re.findall(r'Python$', text)
print(result)


text = "bat, bit, but, bet"
result = re.findall(r'b[aiu]t', text)
print(result)


text = "dog or cat"
result = re.findall(r'dog|cat', text)
print(result)


text = "ha ha ha"
result = re.findall(r'(ha){3}', text)
print(result)


text = "Contact me at user123@gmail.com"
result = re.findall(r'\w+@\w+\.\w+', text)
print(result)
