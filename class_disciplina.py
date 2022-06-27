### CLASSE DISCIPLINA ###

class Disciplina:
    def __init__(self, professor, nome_disciplina, numero_maximo_de_alunos, horario_de_aula, sala_de_aula_da_disciplina) -> None:
        self.professor = professor
        self.nome_disciplina = nome_disciplina
        self.numero_maximo_de_alunos = numero_maximo_de_alunos
        self.horario_de_aula = horario_de_aula
        self.sala_de_aula_da_disciplina = sala_de_aula_da_disciplina

    def __repr__(self):
        return f"Disciplina {self.nome_disciplina} do professor {self.professor}"

    def adicionar_disciplina(self):
        disciplinas.append(self)
    
    

from dados_teste import *