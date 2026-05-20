class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)

        if valor < no.valor:
            no.esq = self._inserir(no.esq, valor)

        else:
            no.dir = self._inserir(no.dir, valor)

        return no

    def buscar(self, no, valor):
        if no is None or no.valor == valor:
            return no

        if valor < no.valor:
            return self.buscar(no.esq, valor)

        return self.buscar(no.dir, valor)

    def imprimir_nos_internos(self):
        print("Nós internos:")
        self._imprimir_nos_internos(self.raiz)

    def _imprimir_nos_internos(self, no):
        if no is not None:

            if no.esq is not None or no.dir is not None:
                print(no.valor)

            self._imprimir_nos_internos(no.esq)
            self._imprimir_nos_internos(no.dir)

    def imprimir_folhas(self):
        print("Folhas:")
        self._imprimir_folhas(self.raiz)

    def _imprimir_folhas(self, no):
        if no is not None:

            if no.esq is None and no.dir is None:
                print(no.valor)

            self._imprimir_folhas(no.esq)
            self._imprimir_folhas(no.dir)

    def imprimir_niveis(self):
        altura = self.calcular_altura(self.raiz)

        for i in range(altura + 1):
            print(f"Nível {i}: ", end="")
            self._imprimir_nivel(self.raiz, i)
            print()

    def _imprimir_nivel(self, no, nivel):
        if no is None:
            return

        if nivel == 0:
            print(no.valor, end=" ")

        else:
            self._imprimir_nivel(no.esq, nivel - 1)
            self._imprimir_nivel(no.dir, nivel - 1)

    def calcular_altura(self, no):
        if no is None:
            return -1

        altura_esq = self.calcular_altura(no.esq)
        altura_dir = self.calcular_altura(no.dir)

        return max(altura_esq, altura_dir) + 1

    def calcular_profundidade(self, valor):
        return self._calcular_profundidade(self.raiz, valor, 0)

    def _calcular_profundidade(self, no, valor, profundidade):
        if no is None:
            return -1

        if no.valor == valor:
            return profundidade

        if valor < no.valor:
            return self._calcular_profundidade(no.esq, valor, profundidade + 1)

        return self._calcular_profundidade(no.dir, valor, profundidade + 1)

    def imprimir_ancestrais(self, valor):
        print("Ancestrais:")
        self._imprimir_ancestrais(self.raiz, valor)

    def _imprimir_ancestrais(self, no, valor):
        if no is None:
            return False

        if no.valor == valor:
            return True

        if (self._imprimir_ancestrais(no.esq, valor) or
                self._imprimir_ancestrais(no.dir, valor)):

            print(no.valor)
            return True

        return False

    def imprimir_descendentes(self, valor):
        no = self.buscar(self.raiz, valor)

        print("Descendentes:")

        if no is not None:
            self._imprimir_descendentes(no.esq)
            self._imprimir_descendentes(no.dir)

    def _imprimir_descendentes(self, no):
        if no is not None:
            print(no.valor)
            self._imprimir_descendentes(no.esq)
            self._imprimir_descendentes(no.dir)

    def analisar_arvore(self, valor_busca):
        print("===== DIAGNÓSTICO GERAL =====")

        if self.raiz is not None:
            print("Raiz:", self.raiz.valor)

        print()

        self.imprimir_nos_internos()

        print()

        self.imprimir_folhas()

        print()

        print("Árvore por níveis:")
        self.imprimir_niveis()

        print()

        print("===== DIAGNÓSTICO ESPECÍFICO =====")

        no = self.buscar(self.raiz, valor_busca)

        if no is None:
            print("Valor não encontrado.")
            return

        grau = 0

        if no.esq is not None:
            grau += 1

        if no.dir is not None:
            grau += 1

        print("Nó analisado:", no.valor)
        print("Grau do nó:", grau)

        print()

        self.imprimir_ancestrais(valor_busca)

        print()

        self.imprimir_descendentes(valor_busca)

        print()

        print("Altura do nó:", self.calcular_altura(no))

        print("Profundidade do nó:",
              self.calcular_profundidade(valor_busca))


arvore = ArvoreBST()

valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arvore.inserir(valor)

arvore.analisar_arvore(30)

print("Valor | ID de memória")

for valor in valores:
    no = arvore.buscar(arvore.raiz, valor)
    print(no.valor, "|", id(no))