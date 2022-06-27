from class_aluno import Aluno
from class_disciplina import Disciplina
from class_professor import Professor
from class_saladeaula import Sala_de_aula
from dados_teste import *

# PRIMEIRO INPUT
a = int(input("""Qual ação deseja realizar?:\n 
1) Criar dados
2) Excluir dados
3) Alterar dados
4) Mostrar dados
5) Listar dados
6) Associar dados 
7) Desassociar dados

"""))

print(f"\n→ → → Você selecionou a opção {a}\n")

########### CASO O USUÁRIO SELECIONE A OPÇÃO DE CRIAR DADOS ###########

if a == 1:
    b = int(input("""Deseja CRIAR dados de:\n
    1) Sala de aula
    2) Aluno
    3) Professor
    4) Disciplina

    """))

    print(f"\n→ → → Você selecionou a opção {b}\n")
    
    if b == 1:                                      # USUARIO ESCOLHEU SALA DE AULA
        numero_sala_de_aula = int(input("Digite o numero da sala de aula (numero natural): "))
        horario_funcionamento_sala_de_aula = int(input("Digite o horario de funcionamento da sala de aula: "))
        dia_funcionamento = str(input(input("Digite o dia de funcionamento da sala de aula: ")))
        capacidade = int(input("Digite o numero da capacidade da sala de aula: "))
        
        # EH CRIADA UMA SALA COM AS INFORMACOES PASSADAS PELO USUARIO   
        sala_criada = Sala_de_aula(numero_sala_de_aula, dia_funcionamento, horario_funcionamento_sala_de_aula)

        # ADICIONO ESSAS INFORMACOES AOS DADOS
        print(f"\nDADOS ANTES:\n{alunos}\n")
        sala_criada.adicionar_sala()
        print(f"DADOS DEPOIS:\n{alunos}\n\nDADO ADICIONADO COM SUCESSO!\n")

    elif b == 2:                                      # USUARIO ESCOLHEU ALUNO
        curso_do_aluno = str(input("Digite o curso do aluno (apenas letras): "))
        dre_do_aluno = str(input("Digite o DRE do aluno (apenas numeros): "))
        nome_do_aluno = str(input("Digite o nome do aluno (apenas letras): "))
        
        # EH CRIADO UM PERFIL DE ALUNO COM AS INFORMACOES PASSADAS PELO USUARIO
        aluno_criado = Aluno(curso_do_aluno, dre_do_aluno, nome_do_aluno)

        # ADICIONO ESSE ALUNO AOS DADOS E MOSTRO AO USUARIO
        print(f"\nDADOS ANTES:\n{alunos}\n")
        aluno_criado.adicionar_aluno()
        print(f"DADOS DEPOIS:\n{alunos}\n\nDADO ADICIONADO COM SUCESSO!\n")

    elif b == 3:                                      # USUARIO ESCOLHEU PROFESSOR
        nome_do_professor = str(input("Digite o nome do professor (apenas letras): "))
        disciplina_do_professor = str(input("Digite o nome da disciplina do professor (apenas letras): "))

        # EH CRIADO UM PERFIL DE PROFESSOR COM AS INFORMACOES PASSADAS PELO USUARIO
        professor_criado = Professor(nome_do_professor, disciplina_do_professor)
    
        # ADICIONO ESSE PROFESSOR AOS DADOS E MOSTRO AO USUARIO
        print(f"\nDADOS ANTES:\n{professores}\n")
        professor_criado.adicionar_professor()
        print(f"DADOS DEPOIS:\n{professores}\n\nDADO ADICIONADO COM SUCESSO!\n")

    else:                                      # USUARIO ESCOLHEU DISCIPLINA
        nome_da_disciplina = str(input("Digite o nome da disciplina: "))
        professor_da_disciplina = str(input("Digite o nome do professor da disciplina: "))
        numero_maximo_de_alunos = int(input("Digite o numero maximo de alunos: "))
        horario_de_aula = int(input("Digite o horario de aula da disciplina: "))
        sala_de_aula_da_disciplina = int(input("Digite a sala de aula da disciplina: "))

        # A DISCIPLINA EH CRIADA
        disciplina_criada = Disciplina(professor_da_disciplina, nome_da_disciplina, numero_maximo_de_alunos)

        # ADICIONO A DISCIPLINA AOS DADOS E MOSTRO AO USUARIO
        print(f"\nDADOS ANTES:\n{disciplinas}\n")
        disciplina_criada.adicionar_disciplina()
        print(f"DADOS DEPOIS:\n{disciplinas}\n\nDADO ADICIONADO COM SUCESSO!\n")

########### CASO O USUÁRIO SELECIONE A OPÇÃO DE EXCLUIR DADOS ###########

if a == 2:
    c = int(input("""Deseja EXCLUIR dados de:\n
    1) Sala de aula
    2) Aluno
    3) Professor
    4) Disciplina

    """))

    print(f"\n→ → → Você selecionou a opção {c}\n")

    if c == 1:                                      # USUARIO ESCOLHEU SALA DE AULA
        for dados in range(len(salas)):
            print(f"{dados} - {salas[dados]}")
        
        indice_de_exclusao = int(input("Digite o numero de sala de aula que deseja excluir: "))

        # EXCLUI O DADO DO INDICE QUE O USUARIO ESCOLHER

        salas.pop(indice_de_exclusao)
        
        # MOSTRO A LISTA DE SALAS ATUALIZADA APOS A EXCLUSAO

        print(salas)
        
    elif c == 2:                                      # USUARIO ESCOLHEU ALUNO
        for dados in range(len(alunos)):
            print(f"{dados} - {alunos[dados]}")

        indice_de_exclusao = int(input("Digite o numero de aluno que deseja excluir: "))

        # EXCLUI O DADO DO INDICE QUE O USUARIO ESCOLHER

        alunos.pop(indice_de_exclusao)

        # MOSTRO A LISTA DE ALUNOS ATUALIZADA APOS A EXCLUSAO

        print(alunos)

    elif c == 3:                                      # USUARIO ESCOLHEU PROFESSOR
        for dados in range(len(professores)):
            print(f"{dados} - {professores[dados]}")

        indice_de_exclusao = int(input("Digite o numero de professor que deseja excluir: "))

        # EXCLUI O DADO DO INDICE QUE O USUARIO ESCOLHER

        professores.pop(indice_de_exclusao)

        # MOSTRO A LISTA DE PROFESSORES ATUALIZADA APOS A EXCLUSAO

        print(professores)

    else:                                      # USUARIO ESCOLHEU DISCIPLINA
        for dados in range(len(disciplinas)):
            print(f"{dados} - {disciplinas[dados]}")

        indice_de_exclusao = int(input("Digite o numero de disciplina que deseja excluir: "))

        # EXCLUI O DADO DO INDICE QUE O USUARIO ESCOLHER

        disciplinas.pop(indice_de_exclusao)

        # MOSTRO A LISTA DE DISCIPLINAS ATUALIZADA APOS A EXCLUSAO

        print(disciplinas)

########### CASO O USUÁRIO SELECIONE A OPÇÃO DE ALTERAR DADOS ########### (FEITO PARCIALMENTE)

if a == 3:
    d = int(input("""Deseja ALTERAR dados de:\n
    1) Sala de aula
    2) Aluno
    3) Professor
    4) Disciplina

    """))

    print(f"\n→ → → Você selecionou a opção {d}\n")
    
    if d == 1:                                      # USUARIO ESCOLHEU SALA DE AULA
        for dados in range(len(salas)):
            print(f"{dados} - {salas[dados]}")
        
        indice_de_escolha = int(input("\nSelecione o indice do dado que deseja alterar: "))
        print(f"\n→ → → Você selecionou a opção {indice_de_escolha}\n")

        indice_de_escolha2 = int(input("""Selecione qual valor deseja alterar em SALA DE AULA:
        1) Numero da sala
        2) Horario de funcionamento
        3) Capacidade
        4) Dia de funcionamento 
        """))
        
        if indice_de_escolha2 == 1:
            print(f"O valor atual desse dado = {salas[indice_de_escolha].numero}")
            numero_novo = int(input("Digite o numero novo da sala de aula:\n"))
            salas[indice_de_escolha].mudar_numero(numero_novo)
            print(f"O novo valor = {salas[indice_de_escolha].numero}\n")
            print(f"{salas[indice_de_escolha]}")

        if indice_de_escolha2 == 2:
            print(f"O valor atual desse dado = {salas[indice_de_escolha].horario_funcionamento}")
            horario_novo = int(input("Digite o horario de funcionamento novo da sala de aula:\n"))
            salas[indice_de_escolha].mudar_horario_funcionamento(horario_novo)
            print(f"O novo valor = {salas[indice_de_escolha].horario_funcionamento}\n")
            print(f"{salas[indice_de_escolha]}")

        if indice_de_escolha2 == 3:
            print(f"O valor atual desse dado = {salas[indice_de_escolha].capacidade}")
            capacidade_nova = int(input("Digite o numero da capacidade nova da sala de aula:\n"))
            salas[indice_de_escolha].mudar_capacidade(capacidade_nova)
            print(f"O novo valor = {salas[indice_de_escolha].capacidade}\n")
            print(f"{salas[indice_de_escolha]}")

        if indice_de_escolha2 == 4:
            print(f"O valor atual desse dado = {salas[indice_de_escolha].dia_funcionamento}")
            dia_novo = int(input("Digite o numero do novo dia de funcionamento da sala de aula:\n"))
            salas[indice_de_escolha].mudar_dia_funcionamento(dia_novo)
            print(f"O novo valor = {salas[indice_de_escolha].dia_funcionamento}\n")
            print(f"{salas[indice_de_escolha]}")
        
    if d == 2:                                      # USUARIO ESCOLHEU ALUNO
        for dados in range(len(alunos)):
            print(f"{dados} - {alunos[dados]}")

        indice_de_escolha = int(input("\nSelecione o indice do dado que deseja alterar: "))
        print(f"\n→ → → Você selecionou a opção {indice_de_escolha}\n")

        indice_de_escolha2 = int(input("""Selecione qual valor deseja alterar em ALUNO:
        1) Curso
        2) DRE
        """))
    
        if indice_de_escolha2 == 1:
            print(f"O valor atual desse dado = {alunos[indice_de_escolha].curso}")
            curso_novo = str(input("Digite o curso novo do aluno:\n"))
            salas[indice_de_escolha].mudar_curso(curso_novo)
            print(f"O novo valor = {alunos[indice_de_escolha].curso}\n")
            print(f"{alunos[indice_de_escolha]}")

        if indice_de_escolha2 == 2:
            print(f"O valor atual desse dado = {alunos[indice_de_escolha].dre}")
            dre_novo = int(input("Digite o DRE novo do aluno:\n"))
            alunos[indice_de_escolha].mudar_dre(dre_novo)
            print(f"O novo valor = {alunos[indice_de_escolha].dre}\n")
            print(f"{alunos[indice_de_escolha]}")

    if d == 3:                                      # USUARIO ESCOLHEU PROFESSOR
        for dados in range(len(professores)):
            print(f"{dados} - {professores[dados]}")

        indice_de_escolha = int(input("\nSelecione o indice do dado que deseja alterar: "))
        print(f"\n→ → → Você selecionou a opção {indice_de_escolha}\n")

        indice_de_escolha2 = int(input("""Selecione qual valor deseja alterar em PROFESSOR:
        1) Disciplina
        """))

        if indice_de_escolha2 == 1:
            print(f"O valor atual desse dado = {professores[indice_de_escolha].disciplina}")
            disciplina_nova = str(input("Digite a nova disciplina ministrada pelo professor:\n"))
            professores[indice_de_escolha].mudar_disciplina(disciplina_nova)
            print(f"O novo valor = {professores[indice_de_escolha].disciplina}\n")
            print(f"{professores[indice_de_escolha]}")

########### CASO O USUÁRIO SELECIONE A OPÇÃO DE MOSTRAR DADOS ###########

if a == 4:
    e = int(input("""Deseja mostrar dados de:\n
    1) Sala de aula
    2) Aluno
    3) Professor
    4) Disciplina

    """))

    print(f"\n→ → → Você selecionou a opção {e}\n")

    if e == 1:                                      # USUARIO ESCOLHEU SALA DE AULA
        for dados in range(len(salas)):
            print(f"{dados} - {salas[dados]}")
            indice_de_escolha = int(input("Selecione o indice do dado que deseja visualizar: "))
            print(salas[indice_de_escolha])

    if e == 2:                                      # USUARIO ESCOLHEU ALUNO
        for dados in range(len(alunos)):
            print(f"{dados} - {alunos[dados]}")
            indice_de_escolha = int(input("Selecione o indice do dado que deseja visualizar: "))
            print(alunos[indice_de_escolha])
    if e == 3:                                      # USUARIO ESCOLHEU PROFESSOR
        for dados in range(len(professores)):
            print(f"{dados} - {professores[dados]}")
            indice_de_escolha = int(input("Selecione o indice do dado que deseja visualizar: "))
            print(professores[indice_de_escolha])
    if e == 4:                                      # USUARIO ESCOLHEU DISCIPLINA
        for dados in range(len(disciplinas)):
            print(f"{dados} - {disciplinas[dados]}")
            indice_de_escolha = int(input("Selecione o indice do dado que deseja visualizar: "))
            print(disciplinas[indice_de_escolha])            

########### CASO O USUÁRIO SELECIONE A OPÇÃO DE LISTAR DADOS ###########

if a == 5:
    f = int(input("""Deseja listar dados de:\n
    1) Sala de aula
    2) Aluno
    3) Professor
    4) Disciplina

    """))

    print(f"\n→ → → Você selecionou a opção {f}\n")

    if f == 1:                                      # USUARIO ESCOLHEU SALA DE AULA
        for dados in range(len(salas)):
            print(f"{dados} - {salas[dados]}")
    if f == 2:                                      # USUARIO ESCOLHEU ALUNO
        for dados in range(len(salas)):
            print(f"{dados} - {alunos[dados]}")
    if f == 3:                                      # USUARIO ESCOLHEU PROFESSOR
        for dados in range(len(salas)):
            print(f"{dados} - {professores[dados]}")
    if f == 4:                                      # USUARIO ESCOLHEU DISCIPLINA
        for dados in range(len(salas)):
            print(f"{dados} - {disciplinas[dados]}")

########### CASO O USUÁRIO SELECIONE A OPÇÃO DE ASSOCIAR DADOS ########### (NAO FEITO)

if a == 6:
    g = int(input("""Deseja associar dados de:\n
    1) Sala de aula
    2) Aluno
    3) Professor
    4) Disciplina

    """))

    print(f"\n→ → → Você selecionou a opção {g}\n")

########### CASO O USUÁRIO SELECIONE A OPÇÃO DE DESASSOCIAR DADOS ########### (NAO FEITO)

if a == 7:
    h = int(input("""Deseja desassociar dados de:\n
    1) Sala de aula
    2) Aluno
    3) Professor
    4) Disciplina

    """))

    print(f"\n→ → → Você selecionou a opção {h}\n")

   
