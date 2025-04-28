from banco import criar_usuario, criar_conta_corrente, depositar, sacar, extrato, listar_contas
from config import usuarios, contas

# Exemplo de uso do sistema
usuario1 = criar_usuario("João Silva", "1990-05-15", "12345678901", "Rua A, 123 Centro São Luís/MA")
conta1 = criar_conta_corrente("12345678901")

if conta1:
    depositar(conta1, 1500)
    saldo, extrato_lista = sacar(saldo=conta1['saldo'], valor=500, extrato=conta1['extrato'], limite=500, numero_saques=0, limite_saques=3)
    extrato(saldo, extrato_lista)
    listar_contas()
