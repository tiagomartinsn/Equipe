from equipe import equipe
from aluno import aluno

eq = equipe('Alunos')
while True:
    print '1 - Adicionar aluno'
    print '2 - Remover aluno'
    print '3 - Mostrar alunos'
    op = int(raw_input('Opcao: '))
    if op == 1:
        while True:
            nome = raw_input('Digite o nome do aluno: ')
            cpf = int(raw_input('Informe o CPF: '))
            eq.cadastrarA(nome,cpf)
            novo_cadastro = raw_input('Deseja cadastrar outro aluno ?')
            if novo_cadastro.upper() == 'SIM':
                continue
            else:
                eq.imprimir()
                break
    elif op == 2:
        while True:
            excluir = int(raw_input('Informe o CPF a ser excluido: '))
            eq.removerA(excluir)
            nova_remocao = raw_input('Deseja remover outro aluno ?')
            if nova_remocao.upper() == 'SIM':
                continue
            else:
                eq.imprimir()
                break
    elif op == 3:
        while True:
            eq.imprimir()
            nova_consulta = raw_input('Deseja consultar novamente ?')
            if nova_consulta.upper() == 'SIM':
                continue
            else:
                break



