from rich import print
from rich.panel import Panel
class Churrasco:
    # Atributos de Classe

    consumo_padrao:float = 0.400 # Cada pessoa come em media 400 gramas de carne.
    preco_kilo:float = 82.40 # Cada kg de carne custa $ 82,40.

    def __init__(self, titulo, quant):
        # Atributos de Instancia
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é {self.titulo} com  {self.participantes} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kilo   # no lugar do Churrasco (self.__class__)

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [yellow]{self.titulo}[/] com [blue]{self.participantes}[/] convidados"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao} Kg e cada Kg custa R$ {Churrasco.preco_kilo:,.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f} kg[/] de carne."
        conteudo += f"\nO custo total será de [red]R${self.calcular_custo_total():,.2f} [/]."
        conteudo += f"\nCada pessoa pagará [red]R$ {self.calcular_custo_individual():,.2f} [/]para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco("Churras dos Amigos", quant= 15)

c1.analisar()

#print(c1)
c2 = Churrasco("Festa de fim de Ano", quant= 80)
c2.analisar()
