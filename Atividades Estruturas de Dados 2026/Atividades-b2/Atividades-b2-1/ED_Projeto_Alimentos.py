from datetime import datetime, date

fila_1 = []
fila_2 = []
log_descartes = []


def formatar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data.strftime("%d/%m/%Y")
    except ValueError:
        return None


def gerar_produto():
    print("\n=== Entrada de Estoque ===")

    while True:
        sku = input("SKU: ").strip()
        if sku.isdigit():
            sku = int(sku)
            break
        print("SKU inválido.")

    while True:
        nome = input("Produto: ").strip()
        if nome:
            break
        print("Nome inválido.")

    while True:
        data_str = input("Validade (DD/MM/AAAA): ").strip()
        data_formatada = formatar_data(data_str)

        if data_formatada:
            break
        print("Data inválida.")

    produto = {
        "id_sku": sku,
        "nome_produto": nome,
        "data_validade": data_formatada,
        "processado": False 
    }

    fila_1.append(produto)
    print("Produto adicionado à Fila 1.")


def processar_produto():
    if not fila_1:
        print("Fila 1 vazia.")
        return

    produto = None
    for item in fila_1:
        if not item.get("processado"):
            produto = item
            break

    if produto is None:
        print("Todos os produtos já foram processados.")
        return

    validade = datetime.strptime(
        produto["data_validade"], "%d/%m/%Y"
    ).date()

    dias = (validade - date.today()).days

    if dias < 0:
        log_descartes.append(produto)
        produto["processado"] = True
        print("Produto vencido! Descartado (Perda).")
        return

    if dias <= 2:
        produto["critico"] = True
        produto["prioridade"] = 1
    else:
        produto["critico"] = False
        produto["prioridade"] = 2

    produto["dias_restantes"] = dias
    produto["processado"] = True 

    fila_2.append(produto)

    fila_2.sort(key=lambda x: datetime.strptime(x["data_validade"], "%d/%m/%Y"))

    print("Produto enviado para a Fila 2.")


def mostrar_fila_1():
    if not fila_1:
        print("Fila 1 vazia.")
        return

    print("\n=== FILA 1 (ESTOQUE BRUTO) ===")
    for p in fila_1:
        print("SKU:", p["id_sku"], "| Produto:", p["nome_produto"], "| Validade:", p["data_validade"], "| Processado:", p["processado"])

def mostrar_fila_2():
    if not fila_2:
        print("Fila 2 vazia.")
        return

    print("\n=== FILA 2 (CLASSIFICADOS) ===")
    for p in fila_2:
        print("SKU:", p["id_sku"], "| Produto:", p["nome_produto"], "| Validade:", p["data_validade"], "| Dias restantes:", p["dias_restantes"], "| Prioridade:", "Alta" if p["critico"] else "Normal")

def mostrar_descartes():
    if not log_descartes:
        print("Nenhum descarte.")
        return

    print("\n=== DESCARTES (PERDAS) ===")
    for p in log_descartes:
        print("SKU:", p["id_sku"], "| Produto:", p["nome_produto"], "| Validade:", p["data_validade"])

def menu():
    while True:
        print("\n====== MENU ======")
        print("1 - Adicionar Produto")
        print("2 - Processar Produto")
        print("3 - Mostrar Fila 1")
        print("4 - Mostrar Fila 2")
        print("5 - Mostrar Descartes")
        print("6 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            gerar_produto()

        elif opcao == "2":
            processar_produto()

        elif opcao == "3":
            mostrar_fila_1()

        elif opcao == "4":
            mostrar_fila_2()

        elif opcao == "5":
            mostrar_descartes()

        elif opcao == "6":
            break

        else:
            print("Opção inválida.")


menu()