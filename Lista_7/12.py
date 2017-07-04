#-*-coding:utf8;-*-

unidade_milhar=["um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove"]
centena=["cem","duzentos","trezentos","quatrocentos","quinhentos","seicentos","oitocentos","novecentos"]
dezena=["dez","vinte","trinta","quarenta","cinquenta","secenta","setenta","oitenta","noventa"]
string=["mil"]
entrada=int(input("Insira a data:"))
entrada=str(entrada)
if len(entrada)!=4:
    print("Formato inválido")
else:
    pedaco=list(entrada)
    if pedaco[0]!="1":
        string.insert(0,unidade_milhar[int(pedaco[0])-1])
    if pedaco[2]=="0" and pedaco[3]=="0":
        string.append(centena[int(pedaco[1])-1])
    elif pedaco[1]=="1" and pedaco[2]=="0":
        string.append("cento e")
        string.append(unidade_milhar[int(pedaco[3])-1])
        
    elif int(pedaco[2])>1:   
        string.append(centena[int(pedaco[1])-1]+" e")
        string.append(unidade_milhar[int(pedaco[3])-1])

print((" ").join(string))
        





