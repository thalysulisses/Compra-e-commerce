# CÓDIGO ATUALIZADO COM VETORES E FUNÇÕES

# VETORES
saldos_cartoes = [200, 300] 
produtos = ["Fone de ouvido", "Mouse", "Teclado"]
precos = [100, 50, 150]

# FUNÇÕES
def mostrar_produtos():
    print("Produtos disponíveis:")
    for i in range(len(produtos)):
        print(f"{i+1} - {produtos[i]} - R${precos[i]}")

def escolher_produto():
    print("\nEscolha o produto: ",)
    for i in range(len(produtos)):
        print(f"{i+1} - {produtos[i]}")
    opcao = int(input("Digite o número do produto: "))
    return opcao

def escolher_quantidade():
    quantidade = int(input("Quantos deseja comprar? "))
    return quantidade

def calcular_total(preco, quantidade):
    return preco * quantidade

def pagamento_cartao(total):
    # CARTÃO 1
    if saldos_cartoes[0] >= total:
        saldos_cartoes[0] -= total
        print("Compra confirmada no Cartão 1!")
        print(f"Saldo restante: R${saldos_cartoes[0]}")
    else:
        print("Saldo insuficiente no Cartão 1.")
        escolha = int(input("Deseja tentar outro cartão (1) ou finalizar (2)? "))
        if escolha == 1: #CARTÃO 2
            if saldos_cartoes[1] >= total:
                saldos_cartoes[1] -= total
                print("Compra confirmada no Cartão 2!")
                print(f"Saldo restante: R${saldos_cartoes[1]}")
            else:
                print("Saldo insuficiente no Cartão 2. Compra negada.")
        else:
            print("Compra não realizada. Pedido finalizado sem pagamento.")

def escolher_pagamento(total):
    print(f"\nValor total da compra: R${total}")
    print("Escolha a forma de pagamento:")
    print("1 - Cartão")
    print("2 - PIX")
    print("3 - Boleto")

    opcao = int(input("Digite o número da opção: "))

    if opcao == 1:
        pagamento_cartao(total)
    elif opcao == 2:
        print("Compra confirmada via PIX!")
    elif opcao == 3:
        print("Compra confirmada via Boleto!")
    else:
        print("Opção inválida. Compra não realizada.")


# PROGRAMA PRINCIPAL
mostrar_produtos()
produto_escolhido = escolher_produto()
quantidade = escolher_quantidade()
total = calcular_total(precos[produto_escolhido -1], quantidade)
escolher_pagamento(total)
