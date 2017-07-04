#-*-coding:utf8;-*-
string=input("Insira a palavra:")
M=[]
m=[]
result=""
for i in range(0,len(string)):
    M.append(string[i].lower())
    m.append(string[i].upper())
for i in range(0,len(string)):
    if string[i]==M[i]:
        result+=m[i]
    elif string[i]==m[i]:
        result+=M[i] 
print(result)
