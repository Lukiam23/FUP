#-*-coding:utf8;-*-
string=input("Insira a palavra:")
c=input("Insira a palavra:")
result=""
for i in string:
    if i.lower()!=c.lower():
        result+=i
print("Nova palavra:",result)