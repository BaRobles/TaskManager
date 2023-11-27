from datetime import datetime


def validar_data(data_vencimento):
    try:
        data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        hoje = datetime.today()
        if data_vencimento < hoje:
            return False
        return True
    except ValueError:
        return False

tasks = []

def cadastrar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    data_vencimento = input("Digite a data de vencimento da tarefa (DD/MM/AAAA): ")
    while not validar_data(data_vencimento):
        print("Data de vencimento inválida ou no passado. Tente novamente.")
        data_vencimento = input("Digite a data de vencimento da tarefa (DD/MM/AAAA): ")

    while True:
        try:
            prioridade = int(input("Digite a prioridade da tarefa (1 - Baixa, 2 - Média, 3 - Alta): "))
            if prioridade < 1 or prioridade > 3:
                print("Prioridade inválida. A prioridade deve estar no intervalo de 1 a 3.")
                print("Opções:")
                print("1. Tentar novamente")
                print("2. Voltar ao menu principal")
                opcao = input("Escolha uma opção: ")
                if opcao == "2":
                    return  # Retorna ao menu principal
            else:
                break
        except ValueError:
            print("Entrada inválida. A prioridade deve ser um número inteiro.")

    if prioridade < 1 or prioridade > 3:
        print("Prioridade inválida. A prioridade deve estar no intervalo de 1 a 3.")
    else:
        task = {
            "descricao": descricao,
            "data_vencimento": data_vencimento,
            "prioridade": prioridade
        }
        tasks.append(task)
        print("Tarefa cadastrada com sucesso!")

def mostrar_tarefas():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    else:
        tasks.sort(key=lambda x: x["prioridade"])
        print("-----")
        print("Tarefas cadastradas:")
        for idx, task in enumerate(tasks, start=1):
              print(f"{idx}. Descrição: {task['descricao']}")
              print(f"Data de Vencimento: {task['data_vencimento']}")
              print(f"Prioridade: {task['prioridade']}")
              print("-----")

def atualizar_tarefa():
    mostrar_tarefas()
    if not tasks:
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. Descrição: {task['descricao']}, Data de Vencimento: {task['data_vencimento']}, Prioridade: {task['prioridade']}")

    idx = int(input("Digite o número da tarefa que deseja atualizar: "))
    if idx < 1 or idx > len(tasks):
        print("Tarefa inválida.")
        return

    task = tasks[idx - 1]
    print(f"Tarefa selecionada: {task['descricao']}")

    descricao = input("Nova descrição da tarefa (ou aperte Enter para manter a mesma): ")
    if descricao:
        task["descricao"] = descricao
    
    while True:
      data_vencimento = input("Nova data de vencimento (DD/MM/AAAA) (ou aperte Enter para manter a mesma): ")
      if data_vencimento:
        if validar_data(data_vencimento):
          task["data_vencimento"] = data_vencimento
          break
        else:
          print("Data de vencimento inválida ou no passado. Tente novamente.")
      else:
        break # mantém a mesma data
    while True:
      prioridade_input = input("Nova prioridade (1 - Baixa, 2 - Média, 3 - Alta) (ou aperte Enter para manter a mesma): ")
      if prioridade_input:
        try:
          prioridade = int(prioridade_input)
          if 1 <= prioridade <=3:
            task["prioridade"] = prioridade
            break
          else:
            print("Prioridade inválida. A prioridade deve estar no intervalo de 1 a 3.")
        except ValueError:
         print("Entrada inválida. A prioridade deve ser um número inteiro.")
      else:
       break

    print("Tarefa atualizada com sucesso!")

def excluir_tarefa():
    mostrar_tarefas()
    if not tasks:
        return
    idx = int(input("Digite o número da tarefa que deseja excluir: "))
    if idx < 1 or idx > len(tasks):
        print("Tarefa inválida.")
        return

    task = tasks.pop(idx - 1)
    print(f"Tarefa '{task['descricao']}' excluída com sucesso!")

while True:
    print("\nGerenciador de Tarefas")
    print("1. Cadastrar Tarefa")
    print("2. Mostrar Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Excluir Tarefa")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_tarefa()
    elif opcao == "2":
        mostrar_tarefas()
    elif opcao == "3":
        atualizar_tarefa()
    elif opcao == "4":
        excluir_tarefa()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
