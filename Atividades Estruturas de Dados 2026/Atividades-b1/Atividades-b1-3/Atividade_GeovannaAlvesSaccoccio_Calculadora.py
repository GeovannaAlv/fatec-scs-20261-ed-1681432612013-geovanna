''' 
*---------------------------------------------------------* 
*              Fatec São Caetano do Sul                   * 
*                   Atividade B1-3                        * 
*    Autor: Geovanna Alves Saccoccio                      * 
*    Objetivo:Desenvolver uma aplicação que simule o      *
*   funcionamento lógico da calculadora financeira HP12c, *
*   utilizando os conceitos de Estrutura de Dados de Pilha*
*   (Stack) para o processamento de expressões em Notação *
*   Polonesa Reversa (RPN).                               * 
*    data: 31/03/2026                                     * 
*---------------------------------------------------------* 
'''

class HP12c:

    def menu():
        while True:
            print("\n====== Menu ======")
            print("1 - Calcular")
            print("2 - Sair")

            op = input("Escolha: ")

            if op == "1":
                exp = input("Digite a expressão RPN: ")
                calc = HP12c()
                calc.calcular(exp)

            if op == "2":
                break

        print("Fim do programa")

    def __init__(self):
        self.pilha = [None, None, None, None]
        self.exp = []

    def mostrar(self):
        print("T=", self.pilha[0], "| Z=", self.pilha[1], "| Y=", self.pilha[2], "| X=", self.pilha[3])

    def push(self, v, t):
        self.pilha = [self.pilha[1], self.pilha[2], self.pilha[3], v]
        self.exp.append(t)
        self.mostrar()

    def pop2(self):
        b = self.pilha[3]
        a = self.pilha[2]

        self.pilha = [None, self.pilha[0], self.pilha[1], None]

        t2 = self.exp.pop()
        t1 = self.exp.pop()

        return a, b, t1, t2

    def calcular(self, texto):
        lista = texto.split()

        cont = 0
        for x in lista:
            if x.replace(".", "", 1).isdigit():
                cont += 1
            else:
                cont -= 1

        if cont != 1:
            print("Expressão inválida")
            return

        for x in lista:
            if x.replace(".", "", 1).isdigit():
                self.push(float(x), x)
            else:
                a, b, t1, t2 = self.pop2()

                if x == "+":
                    r = a + b
                elif x == "-":
                    r = a - b
                elif x == "*":
                    r = a * b
                elif x == "/":
                    r = a / b

                txt = "(" + t1 + " " + x + " " + t2 + ")"
                self.push(r, txt)

        print("\n Conta:", self.exp[-1])
        print("Resultado:", self.pilha[3])


# Loop Menu
HP12c.menu()