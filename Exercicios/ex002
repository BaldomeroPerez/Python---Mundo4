# Declaração de Classe
class Gafanhoto:
    """
Essa classe cria um gafanhoto,que é uma pessoa com nome e idade.
Para criar uma nova pessoa, use variavel = gafanhoto ( nome , idade)
    """
    def __init__(self, nome = "", idade = 0): # Metodo Construtor
            # Atributos de Instancio
            self.nome = nome
            self.idade = idade

         # Metodos de instancia
    def aniversario(self):
            self.idade = self.idade + 1
    def __str__(self): # Dunder Method
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome ={self.nome} ; idade {self.idade}"


    def mensagem(self):
            return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto(nome="Maria", idade= 17)
g1.aniversario()
#print(g1)
print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Metodo
print(g1.__class__) #Atributo

#print(g1.__doc__) # Dunder Atribute

g2 = Gafanhoto(nome="Miro", idade=63)
#g2.aniversario()
#print(g2.mensagem())
print (g2)
print(g2.__getstate__())

#g3 = Gafanhoto()
#print(g3.mensagem())