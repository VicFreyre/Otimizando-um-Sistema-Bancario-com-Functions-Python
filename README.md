# Otimizando-um-Sistema-Bancario-com-Functions-Python
Desafio de Código DIO - Suzano Pyhton Bootcamp 

Este é um sistema bancário simples, desenvolvido em Python, com funcionalidades para depósito, saque, extrato e gerenciamento de contas e usuários. O sistema é modularizado em três partes principais: funcionalidades bancárias, configuração de dados e execução principal.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- **Criar usuário**: Cadastro de um usuário bancário com informações como nome, CPF, data de nascimento e endereço.
- **Criar conta corrente**: Vinculação de uma conta corrente a um usuário existente.
- **Depósito**: Permite realizar depósitos em uma conta.
- **Saque**: Realiza saques, com limite diário de 3 transações de até R$ 500 cada.
- **Extrato**: Exibe o histórico de movimentações da conta, incluindo depósitos e saques, além do saldo atual.
- **Listar contas**: Exibe todas as contas bancárias e seus respectivos titulares.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

sistema_bancario/ │ ├── config.py # Armazena as listas de usuários e contas ├── banco.py # Contém as funções relacionadas ao banco (criar usuário, criar conta, depositar, sacar, etc.) ├── main.py # Arquivo principal que gerencia a execução do sistema └── README.md # Este arquivo de documentação

