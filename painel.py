import json



def menu_principal():
    print('----- MENU PRINCIPAL -----\n')
    print("(1)***** [ESTUDANTES] MENU *****")
    print("(2)***** [PROFESSORES]  *****")
    print("(3)***** [DISCIPLINAS] *****")
    print("(4)***** [TURMAS]  *****")
    print("(5)***** [MATRICULAS] *****")
    print("(0)***** [Sair] *****")
    return input("Escolha uma opção seguinte:")

def menu_operacoes():
    print('(1) Incluir.')
    print('(2) Listar.')
    print('(3) Editar.')
    print('(4) Excluir.')
    print('(9) Voltar ao menu principal.\n')
    return input("Escolha uma opção")

def salvar_arquivo(lista_qualquer, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista_qualquer, arquivo_aberto)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_qualquer = json.load(arquivo_aberto)

        return lista_qualquer
    except:
        return []


arquivo_estudante = "estudantes.json"
arquivo_professores = "professores.json"
arquivo_disciplina = "disciplina.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"

def incluir_aluno(nome_arquivo):

    print("\n\n===== INCLUIR =====\n")
    codigo = int(input("Codigo do Aluno :"))
    nome = input("Nome do Aluno: ")
    cpf = input("CPF do Aluno: ")

    dados_estudante = {"cod": codigo, "nome_estudante": nome, "cpf": cpf}
    lista_qualquer = ler_arquivo(nome_arquivo)
    lista_qualquer.append(dados_estudante)
    salvar_arquivo(lista_qualquer, nome_arquivo)


def incluir_professores(nome_arquivo):
    print("\n\n===== INCLUIR =====\n")
    codigo_professores = int(input("codigo do professor(a) "))
    nome_professores = input("Nome do Professor(a) ")
    cpf_professores = input("CPF do professor(a) ")

    dados_professores ={"cod_prof": codigo_professores, "nome_prof": nome_professores, "cpf_prof": cpf_professores}
    lista_qualquer = ler_arquivo(nome_arquivo)
    lista_qualquer.append(dados_professores)
    salvar_arquivo(lista_qualquer, nome_arquivo)


def incluir_disciplinas(nome_arquivo):
    print("\n\n===== INCLUIR =====\n")
    codigo_disciplina = int(input("Digite o codigo da Disciplina: "))
    nome_disciplina = input("digite o nome da disciplina")

    dados_disciplina = {"cod_disciplina": codigo_disciplina, "nome_disciplina": nome_disciplina}
    lista_qualquer = ler_arquivo(nome_arquivo)
    lista_qualquer.append(dados_disciplina)
    salvar_arquivo(lista_qualquer, nome_arquivo)

def incluir_turmas(nome_arquivo):
    print("\n\n===== INCLUIR =====\n")
    codigo_turma = int(input("Digite o codigo da Turma: "))
    codigo_prof = int(input("Digite o codigo do professor(a): "))
    codigo_disciplina = int(input("Digite o codigo da disciplina: "))

    dados_turma = {"cod_turma": codigo_turma, "cod_prof": codigo_prof, "cod_disciplinas": codigo_disciplina}
    lista_qualquer = ler_arquivo(nome_arquivo)
    lista_qualquer.append(dados_turma)

    for cadastro in lista_qualquer:
        if cadastro["cod_turma"] == codigo_turma:
            print("Já possui esse codigo no cadastro! ")
        else:
            salvar_arquivo(lista_qualquer, nome_arquivo)


def incluir_matriculas(nome_arquivo):
    print("\n\n===== INCLUIR =====\n")
    codigo_turma = int(input("Digite o codigo da turma: "))
    codigo_estudante = int(input("Digite o codigo do estudante: "))

    dados_matriculas = {"cod_turmas": codigo_turma, "cod_alunos": codigo_estudante}
    lista_qualquer = ler_arquivo(nome_arquivo)
    lista_qualquer.append(dados_matriculas)

    for cadastro in lista_qualquer:
        if cadastro["cod_turmas"] == codigo_turma:
            print("Já possui esse codigo no cadastro! ")
        else:
            salvar_arquivo(lista_qualquer, nome_arquivo)




def listar_cadastros(nome_arquivo):
    lista_qualquer = ler_arquivo(nome_arquivo)
    if len(lista_qualquer) == 0:
        print("ISSO AQUI TA MAIS VAZIO DOQ MINHA CARTEIRA")
    else:
        for cadastro in lista_qualquer:
            print(f"Dados do cadastro:{cadastro}")

def excluir_cadastro(codigo, nome_arquivo):
    cadastro_para_remover = None
    lista_qualquer = ler_arquivo(nome_arquivo)
    if nome_arquivo == arquivo_estudante:
        for cadastro in lista_qualquer:
            if cadastro["cod_estudante"] == codigo:
                cadastro_para_remover = cadastro
                break

        if cadastro_para_remover is not None:
            lista_qualquer.remove(cadastro_para_remover)
            salvar_arquivo(lista_qualquer, nome_arquivo)

    if nome_arquivo == arquivo_professores:
        for cadastro in lista_qualquer:
            if cadastro["cod"] == codigo:
                cadastro_para_remover = cadastro
                break

        if cadastro_para_remover is not None:
            lista_qualquer.remove(cadastro_para_remover)
            salvar_arquivo(lista_qualquer, nome_arquivo)

    if nome_arquivo == arquivo_disciplina:
        for cadastro in lista_qualquer:
            if cadastro["cod_disciplina"] == codigo:
                cadastro_para_remover = cadastro
                break

        if cadastro_para_remover is not None:
            lista_qualquer.remove(cadastro_para_remover)
            salvar_arquivo(lista_qualquer, nome_arquivo)

    if nome_arquivo == arquivo_turmas:
        for cadastro in lista_qualquer:
            if cadastro["cod_turma"] == codigo:
                cadastro_para_remover = cadastro
                break

        if cadastro_para_remover is not None:
            lista_qualquer.remove(cadastro_para_remover)
            salvar_arquivo(lista_qualquer, nome_arquivo)

    if nome_arquivo == arquivo_matriculas:
        for cadastro in lista_qualquer:
            if cadastro["cod_turmas"] == codigo:
                cadastro_para_remover = cadastro
                break

        if cadastro_para_remover is not None:
            lista_qualquer.remove(cadastro_para_remover)
            salvar_arquivo(lista_qualquer, nome_arquivo)


def editar_cadastro(codigo, nome_arquivo):
    print("\n\n===== Editar: =====\n")
    lista_qualquer = ler_arquivo(nome_arquivo)
    if nome_arquivo == arquivo_estudante:
        for cadastro in lista_qualquer:
            if cadastro["cod_estudante"] == codigo:
             cadastro["nome_estudante"] = input("Digite o novo nome ")
             cadastro["cpf"] = input("Digite novo CPF")
             salvar_arquivo(lista_qualquer, nome_arquivo)
             break

    if nome_arquivo == arquivo_professores:
        for cadastro in lista_qualquer:
            if cadastro["cod"] == codigo:
                cadastro["nome_prof"] = input("Digite o novo nome do prof ")
                cadastro["cpf_prof"] = input("Digite novo CPF do prof ")
                salvar_arquivo(lista_qualquer, nome_arquivo)
                break

    if nome_arquivo == arquivo_disciplina:
        for cadastro in lista_qualquer:
            if cadastro["cod_disciplina"] == codigo:
                cadastro["nome_disciplina"] = input("Digite o novo nome da Disciplina ")
                salvar_arquivo(lista_qualquer, nome_arquivo)
                break

    if nome_arquivo == arquivo_turmas:
        for cadastro in lista_qualquer:
            if cadastro["cod_turma"] == codigo:
                cadastro["cod_prof"] = int(input("Digite o novo codigo do professor "))
                cadastro["cod_disciplinas"] = int(input("Digite o novo codigo da disciplinas "))
                salvar_arquivo(lista_qualquer, nome_arquivo)
                break

    if nome_arquivo == arquivo_matriculas:
        for cadastro in lista_qualquer:
            if cadastro["cod_turmas"] == codigo:
                cadastro["cod_alunos"] = int(input("Digite o novo codigo do aluno "))
                salvar_arquivo(lista_qualquer, nome_arquivo)
                break




def processar_menu_operacoes(op, nome_arquivo):
    if op == "1":
        if nome_arquivo == arquivo_professores:
            incluir_professores(nome_arquivo)
        elif nome_arquivo == arquivo_estudante:
            incluir_aluno(nome_arquivo)
        elif nome_arquivo == arquivo_disciplina:
            incluir_disciplinas(nome_arquivo)
        elif nome_arquivo == arquivo_turmas:
            incluir_turmas(nome_arquivo)
        elif nome_arquivo == arquivo_matriculas:
            incluir_matriculas(nome_arquivo)

    elif op == "2":
        listar_cadastros(nome_arquivo)

    if op == "3":
        codigo = int(input("digite o codigo para editar"))
        editar_cadastro(codigo, nome_arquivo)

    elif op == "4":
        codigo = int(input("digite o codigo para excluir"))
        excluir_cadastro(codigo, nome_arquivo)

    if op == "9":
        return False

    else:
        print("\n\n----------------")

    return True

while True:
    menu = menu_principal()
    print(f"opção escolhida: {menu}")

    if menu == "1":

        while True:
            op = menu_operacoes()
            if not processar_menu_operacoes(op, arquivo_estudante):
                break

    if menu == "2":
        while True:
            op = menu_operacoes()
            if not processar_menu_operacoes(op, arquivo_professores):
                break

    if menu == "3":
        while True:
            op = menu_operacoes()
            if not processar_menu_operacoes(op, arquivo_disciplina):
                break
    if menu == "4":
        while True:
            op = menu_operacoes()
            if not processar_menu_operacoes(op, arquivo_turmas):
                break
    if menu == "5":
        while True:
            op = menu_operacoes()
            if not processar_menu_operacoes(op, arquivo_matriculas):
                break
    if menu == "0":
        print("End...")
        break


