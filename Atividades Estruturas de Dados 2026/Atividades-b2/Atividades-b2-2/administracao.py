''' 
*---------------------------------------------------------* 
*              Fatec São Caetano do Sul                   * 
*                   Atividade B2-1                        * 
*    Autor: Geovanna Alves Saccoccio                      * 
*    Objetivo:Desenvolver uma aplicação de servidor de    *
*   impressão entre dois grupos, administrador e aluno.   * 
*    data: 28/04/2026                                     * 
*---------------------------------------------------------* 
'''

from collections import deque

class Documento:
    def __init__(self, nome, paginas, tipo):
        self.nome = nome
        self.paginas = paginas
        self.tipo = tipo  # "aluno" ou "admin"

    def __str__(self):
        return f"{self.nome} ({self.paginas} páginas - {self.tipo})"


class GerenciadorFila:
    def __init__(self):
        self.fila_aluno = deque()
        self.fila_admin = deque()

    # Inserir documento
    def inserir_documento(self, documento):
        if documento.tipo == "admin":
            self.fila_admin.append(documento)
        else:
            self.fila_aluno.append(documento)
        print(f"Documento '{documento.nome}' adicionado na fila.")

    # Processar impressão (admin tem prioridade)
    def processar(self):
        if self.fila_admin:
            doc = self.fila_admin.popleft()
        elif self.fila_aluno:
            doc = self.fila_aluno.popleft()
        else:
            print("Fila vazia.")
            return

        print(f"Imprimindo: {doc}")

    # Visualizar filas
    def visualizar(self):
        print("\n--- FILA ADMINISTRATIVA ---")
        if self.fila_admin:
            for doc in self.fila_admin:
                print(doc)
        else:
            print("Vazia")

        print("\n--- FILA ALUNOS ---")
        if self.fila_aluno:
            for doc in self.fila_aluno:
                print(doc)
        else:
            print("Vazia")

    # Contar documentos
    def total_documentos(self):
        total = len(self.fila_admin) + len(self.fila_aluno)
        print(f"Total de documentos na fila: {total}")


# Menu
def menu():
    sistema = GerenciadorFila()

    while True:
        print("\n===== MENU =====")
        print("1 - Adicionar documento")
        print("2 - Processar impressão")
        print("3 - Visualizar filas")
        print("4 - Total de documentos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do documento: ")
            paginas = int(input("Número de páginas: "))
            tipo = input("Tipo (aluno/admin): ").lower()

            doc = Documento(nome, paginas, tipo)
            sistema.inserir_documento(doc)

        elif opcao == "2":
            sistema.processar()

        elif opcao == "3":
            sistema.visualizar()

        elif opcao == "4":
            sistema.total_documentos()

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


# Executar o sistema
if __name__ == "__main__":
    menu()