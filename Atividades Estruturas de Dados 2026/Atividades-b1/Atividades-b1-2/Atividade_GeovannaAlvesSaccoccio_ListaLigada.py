'''
*---------------------------------------------------------*
*               Fatec São Caetano do Sul                  *
*                 Atividade B1-2                          *
*  Autor: Geovanna Alves Saccoccio                        *
*  Objetivo:Mostrar manipulação de lista ligada em python *
*  data: 09/03/2026                                       *
*---------------------------------------------------------*
'''
# Banco de dados em memoria (Dicionario)
produtos = {}

def valorExite(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]
    return False     

# funcao de Inclusao
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")
    if (valorExite(listaEntrada, valor)):
       print("Codigo de produto Duplicado")
       return listaEntrada
    novoNo = {"valor":  valor, "proximo": listaEntrada}
    return novoNo

# funcao de consulta
def inserirFim(listaEntrada):
    valor = input("Digite o valor: ")
    if (valorExite(listaEntrada, valor)):
        print("Codigo de produto Duplicado")
        return listaEntrada
    novoNo = {"valor": valor, "proximo": None}
    if listaEntrada is None:
        return novoNo
    atual = listaEntrada
    while atual["proximo"] is not None:
        atual = atual["proximo"]
    atual["proximo"] = novoNo
    return listaEntrada

# funcao de Alteracao
def inserirMeio(listaEntrada):
    valor = input("Digite o valor: ")
    if (valorExite(listaEntrada, valor)):
        print("Codigo de produto Duplicado")
        return listaEntrada
    pos = int(input("Digite a posição: "))
    novoNo = {"valor": valor, "proximo": None}
    if pos <= 1 or listaEntrada is None:
        novoNo["proximo"] = listaEntrada
        return novoNo
    atual = listaEntrada
    contador = 1
    while atual["proximo"] is not None and contador < pos - 1:
        atual = atual["proximo"]
        contador += 1
    novoNo["proximo"] = atual["proximo"]
    atual["proximo"] = novoNo
    return listaEntrada

# funcao de Exclusao
def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista vazia")
        return
    listaAtual = listaRecebida
    while listaAtual is not None:
        print(listaAtual["valor"], end="->")
        listaAtual = listaAtual["proximo"]

# funcao de Lista
def buscar(listaRecebida):
    argumentoPesquisa = input("informe o argumento de pesquisa:")
    
    listaAtual = listaRecebida
    posicao = 0
    
    while listaAtual is not None:
        posicao += 1
        if listaAtual["valor"] == argumentoPesquisa:
            break
        listaAtual = listaAtual["proximo"]
    if listaAtual is None:
        print("Valor não encontrado")
    else:
        print(f"valor encontrado na posição {posicao}")

def remover(listaEntrada):
    valor = input("Digite o valor a remover: ")
    if listaEntrada is None:
        return None
    if listaEntrada["valor"] == valor:
        return listaEntrada["proximo"]
    atual = listaEntrada
    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == valor:
            atual["proximo"] = atual["proximo"]["proximo"]
            return listaEntrada
        atual = atual["proximo"]
    print("Valor não encontrado")
    return listaEntrada

# Exemplo de Menu de Interacao
def menu():
    lista = None
    while True:
        print("\n1-Inserir no Início \n2-inserir no Fim \n3-Inserir no meio \n4-listar \n5-remover \n6-Buscar \n0-Sair")
        opcao = input("Escolha uma operacao: ")
        
        if opcao == '1':
           lista = inserirInicio(lista)
        elif opcao == '2':
           lista = inserirFim(lista)
        elif opcao == '3':
           lista = inserirMeio(lista)
        elif opcao == '4':
           listar(lista)
        elif opcao == '5':
           lista = remover(lista)
        elif opcao == '6':   
           buscar(lista)
        elif opcao == '0':
           print("Obrigado por usar o sistema")
           break
        else:
           print("**Opcao invalida**")
            
print("**bem vindo ao programa**")
menu()