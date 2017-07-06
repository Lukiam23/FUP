contas={}
for i in range(3):
    numero=input("Insira o número da conta %s: " %(i+1))
    contas[numero]=0
run=1
while run==1:
    print("     #### Menu ####")
    print("     0.Sair")
    print("     1.Creditar")
    print("     2.Debitar")
    print("     3.Tranferência")
    print("     4.Valor das contas")
    p=input("Digite uma das opções:")
    if p=="0":
        print("Adeus")
        print(contas)
        run=0
    elif p=="1":
        numero=input("Insira o número da sua contas: ")
        if numero in contas:
            valor_credito=float(input("Insira o valor:"))
            if valor_credito>=0:
                contas[numero]+=valor_credito
            else:
                print("Valores negativos não são aceitos")
        else:
            print("Conta não encontrada")
    elif p=="2":
        numero=input("Insira o número da sua contas: ")
        if numero in contas:
            valor_debito=float(input("Insira o valor:"))
            if 0<=valor_debito and valor_debito<=contas[numero]:
                contas[numero]-=valor_debito
            else:
                print("Você não possui saldo suficiente")
        else:
            print("Conta não encontrada")
    elif p=="3":
        numero_origem=input("Insira o número da conta de origem: ")
        numero_destino=input("Insira o número da conta de destino: ")
        if numero_origem in contas and numero_destino in contas:
            valor_transferencia=float(input("Insira o valor:"))
            if 0<=valor_transferencia and valor_transferencia<=contas[numero_origem]:
                contas[numero_destino]+=valor_transferencia
                contas[numero_origem]-=valor_transferencia
            else:
                print("Você não possui saldo suficiente")
        else:
            print("Conta não encontrada")
    elif p=="4":
        print(contas)
