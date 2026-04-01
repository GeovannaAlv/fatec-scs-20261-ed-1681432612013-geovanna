''' 
*---------------------------------------------------------* 
*              Fatec São Caetano do Sul                   * 
*                   Atividade B1-1                        * 
*    Autor: Geovanna Alves Saccoccio                      * 
*    Objetivo: Implementar as operações fundamentais de   *
*    num sistema de cadastro utilizando a estrutura de    *
*   dados Dicionario em Python, aplicando conceitos de    *
*    abstração e persistência em memória.                 * 
*    data: 24/02/2026                                     * 
*---------------------------------------------------------* 
'''

catalogo = {
    1: { 'id_filme': 1, 'titulo': 'Avatar', 'diretor':'James Cameron' },
    2:  { 'id_filme': 2, 'titulo': 'Vingadores: Ultimato', 'diretor':'Anthony e Joe Russo' },
    3: { 'id_filme': 3, 'titulo': 'Titanic', 'diretor':'James Cameron' }
}

def menu():
  print("Menu de opções")
  print("1- buscar filme \n2- Adicionar filme \n3- Remover filme \n4- Listar todos os filmes")


def adicionar_filme():
  try: 
   id_filme = int(input("Digite o id do filme que deseja adicionar "))
  except ValueError: 
     print(f"id inválido, digite um número")
     return
  if id_filme in catalogo:
   print(f"Ja existe um filme com esse id")
   return

  else: 
   titulo = input("digite o título do novo filme: ")
   diretor = input("digite o título do diretor do novo: ")
   catalogo[id_filme] = { 'id_filme': id_filme, 
                          'titulo': titulo, 
                          'diretor': diretor } 
  print(f"filme '{titulo}' adicionado com sucesso!")

def buscar_filme():
  try: 
     id_buscar = int(input(f"digite o id do filme: "))
  except ValueError: 
     print(f"digite um número válido.")
     return  
    
  if id_buscar in catalogo:
   filme = catalogo.get(id_buscar)
   print(filme.values())
  else:
     print(f"Filme não encontrado.")


def remover_filme():
  try: 
   id_filme = int(input(f"Selecione o id do filme que deseja remover: "))
  except ValueError: 
     print(f"inválido, digite um número.")
     return
  if id_filme in catalogo:
    item_removido = catalogo.pop(id_filme)
    print (f"items removidos: {item_removido.values()}")
  else:
    print(f"filme não encontrado")

def listar_todos():

    if catalogo:
      print("\nlista de filmes")
      print(catalogo.values()) 

    else:
      print("\nO catalogo esta vazio.")
   
      
 #--- Testes de Funcionamento-
 
while True:
    menu ()
    opcao = int(input('Selecione uma opção'))
    if opcao == 1: buscar_filme()
    elif opcao == 2: adicionar_filme()
    elif opcao == 3: remover_filme()
    elif opcao == 4: listar_todos()
    else:
      print("opção inválida")
                      