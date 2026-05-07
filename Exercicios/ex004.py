from rich import print, inspect

class Pessoa:
    def __init__(self, nome = " ", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1  # =self.idade + 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f" {self.nome} acabou de fazer a matricula")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f" Prof {self.nome} começou a dar aula")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f" {self.nome} acabou de bater o ponto")


a1 = Aluno("José", 17, "informatica", "T01")
a1.fazer_aniversario()   # acrescentou mais um ano
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("Miro", 63, "Mestrado", "10")
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Claudia", 21, "Secretária", "Diretoria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)