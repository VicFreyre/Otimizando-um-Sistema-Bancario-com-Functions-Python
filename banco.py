from config import usuarios, contas

# Função para criar um usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print(f"Erro: CPF {cpf} já cadastrado.")
        return None
    usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")
    return usuario

# Função para criar uma conta corrente
def criar_conta_corrente(usuario_cpf):
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == usuario_cpf), None)
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return None
    numero_conta = len([conta for conta in contas if conta['usuario']['cpf'] == usuario_cpf]) + 1
    conta = {'agencia': "0001", 'numero_conta': numero_conta, 'usuario': usuario, 'saldo': 0, 'extrato': []}
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso para {usuario['nome']}.")
    return conta

# Função para depositar
def depositar(conta, valor):
    if valor <= 0:
        print("Erro: O valor do depósito deve ser positivo.")
        return
    conta['saldo'] += valor
    conta['extrato'].append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

# Função para sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Erro: Limite de saques diários atingido.")
        return saldo, extrato
    if valor > saldo:
        print("Erro: Saldo insuficiente.")
        return saldo, extrato
    if valor > limite:
        print(f"Erro: O valor máximo para saque é R$ {limite:.2f}.")
        return saldo, extrato
    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato

# Função para visualizar extrato
def extrato(saldo, extrato):
    print("\n--- Extrato ---")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    for movimento in extrato:
        print(movimento)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

# Função para listar contas
def listar_contas():
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
