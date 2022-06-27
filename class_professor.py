### CLASSE PROFESSOR ###

class Professor:
    def __init__(self, nome, disciplina) -> None:
        self.nome = nome
        self.disciplina = disciplina

    def __repr__(self) -> str:
        return f"Professor {self.nome} da disciplina {self.disciplina}"

    def adicionar_professor(self):
        professores.append(self)
    
    def mudar_disciplina(self, disciplina_nova):
        self.disciplina = disciplina_nova

from dados_teste import *