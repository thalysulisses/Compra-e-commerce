#Saldo dos cartões cadastrados
saldo_cartao1 = 200  
saldo_cartao2 = 300  

#Produtos
preco_produto = 100
print("Produto disponível: Fone de ouvido - R$100")

quantidade = int(input("Quantos deseja comprar? "))
total = preco_produto * quantidade

#Opções de pagamento
print(f"Valor total da compra: R${total}")
print("Escolha a forma de pagamento:")
print("1 - Cartão")
print("2 - PIX")
print("3 - Boleto")

opcao = int(input("Digite o número da opção: "))

if opcao == 1:  #Cartão
    if saldo_cartao1 >= total:
        saldo_cartao1 -= total
        print("Compra confirmada no Cartão 1!")
        print(f"Saldo restante: R${saldo_cartao1}")
    else:
        print("Saldo insuficiente no Cartão 1.")
        escolha = int(input("Deseja tentar outro cartão (1) ou finalizar (2)? "))
        if escolha == 1:  #Cartão 2
            if saldo_cartao2 >= total:
                saldo_cartao2 -= total
                print("Compra confirmada no Cartão 2!")
                print(f"Saldo restante: R${saldo_cartao2}")
            else:
                print("Saldo insuficiente no Cartão 2. Compra negada.")
        else:
            print("Compra não realizada. Pedido finalizado sem pagamento.")
elif opcao == 2:  #PIX
    print("Compra confirmada via PIX!")
elif opcao == 3:  #Boleto
    print("Compra confirmada via Boleto!")
else:
    print("Opção inválida. Compra não realizada.")
