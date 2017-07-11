#coding:utf8
vetor=[]
for i in range(10):
    produto={}
    cod=int(input("Insisa o código do produto: "))
    desc=input("Insira a descrição do produto:")
    valor=float(input("Insira o valor do produto: "))
    quant=int(input("Insira a quantidade de produto em estoque: "))
    #Add no dic produto.
    produto["cod"]=cod
    produto["desc"]=desc
    produto["valor"]=valor
    produto["quant"]=quant
    #Add no vetor.
    vetor.append(produto)
#Organizará o vetor.
for i in range(0,len(vetor)):
    for j in range(0,len(vetor)):
        if vetor[i]["cod"]<vetor[j]["cod"]:
            temp=vetor[i]["cod"]
            vetor[i]["cod"]=vetor[j]["cod"]
            vetor[j]["cod"]=temp

