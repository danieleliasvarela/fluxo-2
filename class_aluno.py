### CLASSE ALUNO ###

class Aluno:
    def __init__(self, curso = str, dre = int, nome = str) -> None:
        self.curso = curso
        self.dre = dre
        self.nome = nome

    def __repr__(self):
        return f"Aluno {self.nome} com DRE {self.dre} cursando {self.curso}"
        
    def adicionar_aluno(self):
        alunos.append(self)

    def mudar_curso(self, curso_novo):
        self.curso = curso_novo

    def mudar_dre(self, novo_dre):
        self.dre = novo_dre

from dados_teste import * # evitar import circular