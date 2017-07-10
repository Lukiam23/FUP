#_*_coding:utf8
entrada=""
servicos=[]
while entrada!="sair":
    existe=False
    k=0
    entrada=input("Insira o número OS ou digite sair: ")
    while k<len(servicos) and not(existe):
        if servicos[k]["numero_OS"]==entrada:
            existe=True
        k+=1
    if entrada!="sair" and not(existe):
        servico={}
        data=input("Insira a data do serviço: ")
        valor=float(input("Insira o valor do serviço: "))
        descricao=input("Insira a descrição do serviço: ")
        nome=input("Insira o nome do cliente: ")
        servico["numero_OS"]=entrada
        servico["data"]=data
        servico["valor"]=valor
        servico["descricao"]=descricao
        servico["nome"]=nome
        servicos.append(servico)
    elif existe:
        print("Protocolo já existe")

m_servico=0
maior_servico={"nome":servicos[0]["nome"],"valor":servicos[0]["valor"],"descricao":servicos[0]["descricao"],"data":servicos[0]["data"]}
for i in servicos:
    m_servico+=i["valor"]
    if maior_servico["valor"]<i["valor"]:
        maior_servico["valor"]=i["valor"]
        maior_servico["nome"]=i["nome"]
        maior_servico["descricao"]=i["descricao"]
        maior_servico["data"]=i["data"]
m_servico=m_servico/len(servicos)
print("A média de preços foi %.2f" %(m_servico))
print("O maior valor foi o de %.2f do %s cuja descrição era \"%s\" e de data %s" %(maior_servico["valor"],maior_servico["nome"],maior_servico["descricao"],maior_servico["data"]))
