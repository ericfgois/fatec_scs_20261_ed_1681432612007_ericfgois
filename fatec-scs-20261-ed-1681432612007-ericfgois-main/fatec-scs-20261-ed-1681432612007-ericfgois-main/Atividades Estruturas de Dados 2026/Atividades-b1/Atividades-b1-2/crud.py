'''
*----------------------------------------------------------*
* Fatec Antônio Russo - São Caetano do Sul                 *
* Exemplo de Manipulação de Lista ligada                   *
* Autor: Eric Fracassi de Gois                             *
* Objetivo: Mostrar manipulação de lista ligada em python  *
* data: 17/03/2026                                         *
*----------------------------------------------------------*
'''
produto = {}

# achar o cabeça
def valorExiste(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]
    return False

# 1 - Inserir no início
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")
    if (valorExiste(listaEntrada, valor)):
        print("Código de produto Duplicado")
        return listaEntrada
    
    novoNo = {"valor": valor, "proximo": listaEntrada}
   
    print("Produto Inserido")
    return novoNo

# 2 - Inserir no fim
def inserirFim(listaEntrada):
    valor = input("Digite o valor para inserir no fim: ")
    
    if valorExiste(listaEntrada, valor):
        print("Código de produto Duplicado")
        return listaEntrada     
    novoNo = {"valor": valor, "proximo": None}
    
    if listaEntrada is None:
        print("Produto Inserido como primeiro da lista")
        return novoNo
        
    atual = listaEntrada
    while atual["proximo"] is not None:
        atual = atual["proximo"]
    atual["proximo"] = novoNo
    print("Produto incluído no fim com sucesso") 
    return listaEntrada

# 3 - Inserir no meio
def inserirMeio(listaEntrada):
    valor = input("Digite o valor para inserir no meio: ")
    
    if valorExiste(listaEntrada, valor):
        print("Código de produto Duplicado")
        return listaEntrada
        
    referencia = input("Inserir após qual produto existente? ")
    atual = listaEntrada
    while atual is not None:
        if atual["valor"] == referencia:
            novoNo = {"valor": valor, "proximo": atual["proximo"]}
            atual["proximo"] = novoNo
            print(f"Produto {valor} inserido após {referencia}")
            return listaEntrada
        atual = atual["proximo"]
        
    print(f"Produto de referência '{referencia}' não encontrado.")
    return listaEntrada

# 4 - Listar
def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista Vazia")
        return
    
    listaAtual = listaRecebida
    while listaAtual is not None:
        print(listaAtual["valor"], end="->")
        listaAtual = listaAtual["proximo"]

# 5 - Remover Nó
def remover(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia")
        return None
    
    valor = input("Digite o valor para remover: ")
    
    if listaEntrada["valor"] == valor:
        print(f"Produto {valor} removido da posição 0")
        return listaEntrada["proximo"]
    
    atual = listaEntrada
    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == valor:
            print(f"Produto {valor} removido da posição seguinte a {atual['valor']}")
            atual["proximo"] = atual["proximo"]["proximo"]
            return listaEntrada
        atual = atual["proximo"]
    
    print("Produto não encontrado para remoção")
    return listaEntrada

# 6 - Buscar Nó
def buscar(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia")
        return None
    
    valor = input("Digite o valor para buscar: ")

    atual = listaEntrada
    posicao = 0
    while atual is not None:
        if atual["valor"] == valor:
            print(f"Produto {valor} encontrado na posição {posicao}")
            return atual
        atual = atual["proximo"]
        posicao += 1
        

    print("Produto não encontrado")
    return None

#menu
def menu():
    lista = None
    while True:
        print("\n======== Menu do CRUD =======")
        print("1 - Inserir no início")
        print("2 - Inserir no fim")
        print("3 - Inserir no meio")
        print("4 - Listar")
        print("5 - Remover Nó")
        print("6 - Buscar Nó")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            lista = inserirInicio(lista)
        elif opcao == "2":
            inserirFim(lista)
        elif opcao == "3":
            inserirMeio(lista)
        elif opcao == "4":
            listar(lista)
        elif opcao == "5":
            remover(lista)
        elif opcao == "6":
            buscar(lista)
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida")
    print("Obrigado por usar o sistema")

print("**Bem vindo ao programa**")
menu()