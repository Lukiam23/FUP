#-*-coding:utf8;-*-

senha=input("Insira a senha:")
valida=True
if len(senha)>15 and len(senha)<8:
    valida=False
numero=0
string=""
maiuscula=[]
minuscula=[]
for i in senha:
    try:
        if type(int(i))==type(int()):    
            numero+=1
    except:
        string+=i
n_maiuscula=0
n_minuscula=0
for i in string:
    maiuscula.append(i.upper())
    minuscula.append(i.lower())

for i in range(0,len(string)):
    if string[i]==maiuscula[i]:
        n_maiuscula+=1
    elif string[i]==minuscula[i]:
        n_minuscula+=1
if (n_maiuscula<1 or n_minuscula<1 or numero<1):
    valida=False

if valida:
    print("A senha é valida pois possui %s letras minúsculas %s maiúsculas e %s dígitos" %(n_minuscula,n_maiuscula,numero))
else:
    print("Senha inválida")


