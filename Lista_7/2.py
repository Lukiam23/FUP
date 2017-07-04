#-*-coding:utf8;-*-

en=input("Insira a palavra:")
palindromo=True
i=0
j=len(en)-1
for k in range(0,int((len(en))/2)):
    if(en[i]!=en[j]):
        palindromo=False
    i+=1
    j-=1
if palindromo==True:
    print("A palavra é palindroma")
else:
    print("A palavra não é palindroma")