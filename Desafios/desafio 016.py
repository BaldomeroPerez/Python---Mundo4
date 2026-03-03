from rich import print
from rich import inspect

class Funcionario:
    # Atributo de Classe
    empresa = "Curso em Video"
    def __init__(self, nome, cargo, setor):
        # Atributos de Instância
        self.nome = nome
        self.cargo = cargo
        self.setor = setor
        
    def apresentacao (self):
        return f":handshake: Olá, sou [blue]{self.nome}[/blue], sou {self.cargo} do setor de {self.setor},da empresa {Funcionario.empresa}."
    
c1 = Funcionario(nome="Maria", setor="Administração", cargo="Diretoria")

print(c1.apresentacao())
inspect(c1)

c2 = Funcionario(nome="Pedro", setor="TI", cargo="Programador")

print(c2.apresentacao())
inspect(c2)
