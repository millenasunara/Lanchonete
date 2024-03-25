print("=-=-=-=-=-=-=Bem- Vindo=-=-=-=-=-=-=")
lanches = {
    1: "Hambúrguer",
    2: "Sanduíche de frango",
    3: "Pizza",
    4: "Taco",
    5: "Pastel"
}

bebidas = {
    1: "Refrigerante",
    2: "Suco",
    3: "Água",
    4: "Cerveja",
    5: "Chá"
}

sobremesas = {
    1: "Sorvete",
    2: "Bolo de chocolate",
    3: "Mousse",
    4: "Frutas",
    5: "Cheesecake"
}


pedido = {
    "lanches": [],
    "bebidas": [],
    "sobremesas": []
}



def fazer_pedido_lanche():
    print("\nCardápio de Lanches:")
    for indice, item in lanches.items():
        print(f"{indice}: {item}")

    indice = int(input("\nDigite o índice do lanche desejado: "))
    if indice in lanches:
        pedido['lanches'].append(lanches[indice])
        print(f"Lanche escolhido: {lanches[indice]}")
    else:
        print("Índice inválido!")



def fazer_pedido_bebida():
    print("\nCardápio de Bebidas:")
    for indice, item in bebidas.items():
        print(f"{indice}: {item}")

    indice = int(input("\nDigite o índice da bebida desejada: "))
    if indice in bebidas:
        pedido["bebidas"].append(bebidas[indice])
        print(f"Bebida escolhida: {bebidas[indice]}")
    else:
        print("Índice inválido!")



def fazer_pedido_sobremesa():
    print("\nCardápio de Sobremesas:")
    for indice, item in sobremesas.items():
        print(f"{indice}: {item}")

    indice = int(input("\nDigite o índice da sobremesa desejada: "))
    if indice in sobremesas:
        pedido["sobremesas"].append(sobremesas[indice])
        print(f"Sobremesa escolhida: {sobremesas[indice]}")
    else:
        print("Índice inválido!")



def finalizar_pedido():
    print("\nResumo do Pedido:")
    for categoria, itens in pedido.items():
        if itens:
            print(f"{categoria.capitalize()}: {', '.join(itens)}")

    resposta = input("O pedido está correto? (SIM ou NÃO): ").strip().lower()

    if resposta == "sim":
        with open("comanda.txt", "w") as arquivo:
            arquivo.write("Comanda:\n")
            for categoria, itens in pedido.items():
                if itens:
                    arquivo.write(f"{categoria.capitalize()}: {', '.join(itens)}\n")
        print("\nPedido finalizado e salvo na comanda.txt!")
        pedido.clear()
        print("\nNovo pedido:")
    elif resposta == "nao" or resposta == "não":
        print("\nPedido não finalizado. Corrija seu pedido.")
    else:
        print("\nResposta inválida! Digite 'SIM' se o pedido estiver correto ou 'NÃO' se não estiver.")



def main():
    while True:
        print("\nOpções de Pedido:")
        print("1: Fazer Pedido de Lanche")
        print("2: Fazer Pedido de Bebida")
        print("3: Fazer Pedido de Sobremesa")
        print("4: Finalizar Pedido")
        print("5: Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            fazer_pedido_lanche()
        elif opcao == 2:
            fazer_pedido_bebida()
        elif opcao == 3:
            fazer_pedido_sobremesa()
        elif opcao == 4:
            finalizar_pedido()
        elif opcao == 5:
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
