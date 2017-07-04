#-*-coding:utf8;-*-

data=input("Insira a data:")
valido=True
i=0
k=0
lista=[""]
numeros=[]
for j in range(0,10):
    numeros.append(str(j))
while i<len(data) and valido==True:
    if data[i]=="/":
        lista.append("")
        k+=1
    else:
        if data[i] not in numeros:
            valido=False
        else:         
            lista[k]+=data[i]        
    i+=1

if len(lista[2])!=4:
    valida=False
for l in range(0,len(lista)):
    lista[l]=int(lista[l])
if (not(1<=lista[0]<=31) and 0<lista[1]<=12) or (not(1<=lista[1]<=31) and 0<lista[1]<=12):
    valido=False
elif (0<lista[0]<32 and not(0<lista[1]<=12)) or (1<=lista[1]<=31 and not(0<lista[1]<=12)):
    valido=False
if valido:
    if lista[0]>12 and lista[1]<=12:    
        print("O calendário está no modo brasileiro")
    elif int(lista[0])<=12 and int(lista[1])>12:
        print("O calendário estar no modo norte americano")
    else:
        print("O calendário pode tanto está no modo brasileiro como norte americano")
else:
    print("Data inválida")