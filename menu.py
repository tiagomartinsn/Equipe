from equipe import equipe
from aluno import aluno

while True:
    print '1 - Adicionar aluno'
    print '2 - Remover aluno'
    op = int(raw_input('Opcao: '))
    projeto = raw_input('Informe o nome do projeto: ')
    eq = equipe(projeto)

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
            excluir = int(raw_input('Informe o aluno a ser excluido: '))
            eq.removerA(excluir)
            nova_remocao = raw_input('Deseja remover outro aluno ?')
            if nova_remocao.upper() == 'SIM':
                continue
            else:
                eq.imprimir()
                break




