contas=[]
run=1
while run==1:
    print("     #### Menu ####")
    print("     0.Sair")
    print("     1.Creditar")
    print("     2.Debitar")
    print("     3.Tranferência")
    print("     4.Valor das contas")
    print("     5.Criar conta")
    print("     6.Deletar conta")
    p=input("Digite uma das opções:")
    if len(contas)!=0 or p=="5":
        if p=="0":
            print("Adeus")
            print(contas)
            run=0
        elif p=="1":
            numero=input("Insira o número da sua contas: ")
            existe=False
            k=-1
            while not(existe) and k<len(contas):
                k+=1
                if numero in contas[k]:
                    existe=True
                
            if existe:
                valor_credito=float(input("Insira o valor:"))
                if valor_credito>=0:
                    contas[k][numero]+=valor_credito
                else:
                    print("Valores negativos não são aceitos")
            else:
                print("Conta não encontrada")
        elif p=="2":
            numero=input("Insira o número da sua contas: ")
            existe=False
            k=-1
            while not(existe) and k<len(contas):
                k+=1
                if numero in contas[k]:
                    existe=True
               
            if existe:
                valor_debito=float(input("Insira o valor:"))
                if 0<=valor_debito and valor_debito<=contas[k][numero]:
                    contas[k][numero]-=valor_debito
                else:
                    print("Você não possui saldo suficiente")
            else:
                print("Conta não encontrada")
        elif p=="3":
            numero_origem=input("Insira o número da conta de origem: ")
            numero_destino=input("Insira o número da conta de destino: ")
            existe1=False
            existe2=False
            pos1=-1
            pos2=-1
            while not(existe1) and pos1<len(contas):
                pos1+=1
                if numero_origem in contas[pos1]:
                    existe1=True

            while not(existe2) and pos2<len(contas):
                pos2+=1
                if numero_destino in contas[pos2]:
                    existe2=True
               
            if existe1 and existe2:
                valor_transferencia=float(input("Insira o valor:"))
                if valor_transferencia<=contas[pos1][numero_origem]:
                    contas[pos2][numero_destino]+=valor_transferencia
                    contas[pos1][numero_origem]-=valor_transferencia
                elif 0>valor_transferencia:
                    print("Números negativos não são válidos")
                else:
                    print("Você não possui saldo suficiente")
            else:
                print("Conta não encontrada")
        elif p=="4":
            print(contas)
        elif p=="5":
            numero=input("Insira o número da conta: ")
            existe=True
            if len(contas)==0:
                existe=False
            k=0
            while  existe and k<len(contas):
                if numero not in contas[k]:
                    existe=False
                k+=1
            if existe:
                print("Conta já existe")
            else:
                contas.append({numero:0})
                print("Conta criada.")
        elif p=="6":
            numero=input("Insira o número da conta: ")
            k=0
            achado=False
            while not achado and k<len(contas):
                if numero in contas[k]:
                    contas.pop(k)
                    achado=True
                    print("Conta removida")
                else:
                    print("Conta não existe")
                k+=1
    else:
        print("Não há contas. Digite 5 e crie uma conta.")
