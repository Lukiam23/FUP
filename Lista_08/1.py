#_*_conding:utf8
pessoas=[]
for i in range(20):
    pessoa={}
    salario=float(input("Insira o seu salário: "))
    idade=int(input("Insira a sua idade: "))
    sexo=input("Insira o seu sexo(M para masculino e F para feminino:)")
    n_filhos=int(input("Insira a quantidade de filhos: "))
    pessoa["salario"]=salario
    pessoa["idade"]=idade
    pessoa["sexo"]=sexo
    pessoa["n_filhos"]=n_filhos
    pessoas.append(pessoa)
m_populacao=0
m_filhos=0
maior_s=pessoas[0]["salario"]
n_mulheres=0
sup=0
for i in pessoas:
    m_populacao+=i["salario"]
    m_filhos+=i["n_filhos"]
    if i["salario"]>maior_s:
        maior_s=i["salario"]
    if i["sexo"].upper()=="F":
        n_mulheres+=1
        if i["salario"]>10000:
            sup+=1
    
m_populacao=m_populacao/len(pessoas)
m_filhos=m_filhos/len(pessoas)
porcentagem=(sup*100)/n_mulheres
print("A média de salarios é %.2f " %(m_populacao))
print("A média do número de filhos é %.2f" %(m_filhos))
print("O maior salário é %d" %(maior_s))
print("A porcetagem de mulhres que recebem uma salário acima de 10.000 é de %.2f" %(porcentagem))
