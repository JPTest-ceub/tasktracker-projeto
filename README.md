# TaskTracker

Aplicação de linha de comando para cadastrar e visualizar tarefas, desenvolvida em Python 3.11 como projeto do Bootcamp II.

## Funcionalidades

- Cadastro de tarefas com título, descrição, prioridade e data limite.
- Validação de título obrigatório (não aceita texto vazio ou espaços).
- Validação de prioridade: Alta, Média/Media ou Baixa.
- Status inicial automático: `Pendente`.
- Listagem das tarefas e aviso quando a lista está vazia.

> As tarefas ficam na memória durante a execução e são apagadas ao encerrar o programa.

## Estrutura do projeto

```text
tasktracker-projeto/
├── Dockerfile
├── docker-compose.yml
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Tecnologias

- Python 3.11
- Docker
- Docker Compose
- Git e GitHub

## Como executar localmente com Python

Na raiz do projeto:

```bash
python src/main.py
```

Em alguns ambientes Windows, use `py src/main.py`.

## Como construir a imagem Docker

Na raiz do projeto, execute:

```bash
docker build -t tasktracker .
```

## Como executar em container isolado

```bash
docker run -it --rm tasktracker
```

As opções `-it` mantêm o terminal interativo e `--rm` remove o container ao terminar.

## Como executar com Docker Compose (recomendado)

```bash
docker compose build
docker compose run --rm tasktracker-app
```

O serviço utiliza `stdin_open: true` e `tty: true` para permitir a interação com `input()` no terminal.

## Uso

No menu, escolha:
1. Cadastrar nova tarefa.
2. Visualizar tarefas cadastradas.
3. Sair da aplicação.

Durante o cadastro, informe título, descrição, prioridade e, se desejar, data limite. Prioridades aceitas: Alta, Média ou Baixa.

## Planejamento

O documento `docs/planejamento_logico.pdf` registra o planejamento lógico entregue na etapa inicial.
