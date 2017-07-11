#_*_coding:utf8
#função que calcula os dias
def calc_dias(data_paga,data_venc):
    partes1=data_paga.split("/")
    partes2=data_venc.split("/")
    anos=int(partes1[2])-int(partes2[2])
    meses=int(partes1[1])-int(partes2[1])
    dias=int(partes1[0])-int(partes2[0])+31*(meses)+365*(anos)
    return dias
#função que valida a data
def check_data(data):
    try:
        partes=data.split("/")
        if len(partes[2])!=4 or len(partes)!=3:
            return False
        elif int(partes[1])>12 or 1>int(partes[1]):
            return False
        elif int(partes[0])>31 or 1>int(partes[0]):
            return False
        return True
    except:
        return(False)
documentos=[]
for i in range(2):
    doc={}
    n_documento=int(input("Insira o número do documeto: "))
    cod_cliente = input("Insira o código do cliente: ")
    #Loop para verificar a data.
    run=True
    while run:
        data_vencimento=input("Insira a data de vencimento no formato dd/dd/dddd: ")
        data_pagamento=input("Insira a data de pagamento no formato dd/dd/dddd:")
        if not(check_data(data_vencimento)) or not(check_data(data_vencimento)):
            print("Data Inválida!")
        else:
            run=False
            
    valor_conta=float(input("Insira o valor da conta: "))
    valor_juros=0
    #inserção dos dados no dic doc.
    doc["n_documento"]=n_documento
    doc["cod_cliente"]=cod_cliente
    doc["data_vencimento"]=data_vencimento
    doc["data_pagamento"]=data_pagamento
    doc["valor_conta"]=valor_conta
    doc["valor_juros"]=valor_juros
    documentos.append(doc)
    print("\n\n")
total=0
for k in documentos:
    dias=calc_dias(k["data_pagamento"],k["data_vencimento"])
    juros=(0.0002*k["valor_conta"])*dias
    k["valor_juros"]=juros
    total+=k["valor_conta"]+k["valor_juros"]

print("O total arrecadado com juros é de %.2f" %(total))
