"""TaskTracker - gerenciador simples de tarefas via terminal."""


def pedir_titulo():
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ficar vazio. Tente novamente.")


def pedir_prioridade():
    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }
    while True:
        entrada = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if entrada in prioridades:
            return prioridades[entrada]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    print("\n--- Cadastro de tarefa ---")
    titulo = pedir_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = pedir_prioridade()
    data_limite = input("Data limite (opcional, DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite or "Não informada",
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"  Título: {tarefa['titulo']}")
        print(f"  Descrição: {tarefa['descricao'] or 'Não informada'}")
        print(f"  Prioridade: {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status: {tarefa['status']}")


def main():
    tarefas = []
    while True:
        print("\n====== TaskTracker ======")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
