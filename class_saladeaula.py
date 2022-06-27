### CLASSE SALA DE AULA ###

class Sala_de_aula:
    def __init__(self, numero = int, dia_funcionamento = str, horario_funcionamento = int, capacidade = int):
        self.numero = numero
        self.horario_funcionamento = horario_funcionamento
        self.capacidade = capacidade
        self.dia_funcionamento = dia_funcionamento
    
    def __repr__(self) -> str:
        return f"Sala de aula de numero {self.numero} que funciona no horario {self.horario_funcionamento}h com capacidade {self.capacidade}"

    def adicionar_sala(self):
        salas.append(self)

    def mudar_numero(self, numero_novo):
        self.numero = numero_novo

    def mudar_horario_funcionamento(self, horario_novo):
        self.horario_funcionamento = horario_novo
    
    def mudar_capacidade(self, capacidade_nova):
        self.capacidade = capacidade_nova

    def mudar_dia_funcionamento(self, dia_novo):
        self.dia_funcionamento = dia_novo

from dados_teste import * # Coloquei aqui pra evitar import circular