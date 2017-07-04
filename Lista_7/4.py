#-*-coding:utf8;-*-
str1=input("Insira a palavra:")
str2=input("Insira a palavra:")
anagrama=True
if len(str1)!=len(str2):
    anagrama=False
l1=list(str1.lower())
l2=list(str2.lower())
i=0
while len(l1)>0 and anagrama:
    if l1[i] in l2:
        l2.remove(l1[i])
        l1.remove(l1[i])
    else:
        anagrama=False
if len(l1)==0 and len(l2)==0:
    anagrama=True
else:
    anagrama=False

if anagrama:
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")


