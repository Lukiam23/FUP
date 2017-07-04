#-*-coding:utf8;-*-
nome=input("Insira a palavra:")
i=0
lista=[""]
j=0
while i<len(nome):
    if nome[i]!=" ":
        lista[j]+=nome[i]
    else:
        lista.append("")
        j+=1
    i+=1
result=lista[len(lista)-1]+","
i=0
while i<len(lista)-1:
    result+=lista[i]+" "
    i+=1
print(result)