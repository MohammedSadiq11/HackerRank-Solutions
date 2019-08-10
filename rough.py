import re


s=input("Enter a string :")
x=re.findall("\d+",s)
print(x)

s1=''.join(str(y) for y in x)
print(s1)
