from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min: int = 1
    camal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atial:int = volume
        self.ligado = bool = False
    def liga_desliga(self):
        self.ligado = not self.ligado
    def mostrar_tv(self):

        if not self.ligado:
            conteudo = f":prohibited: [red] A TV está desligada [/red]"
        else:
            conteudo = f"CANAL ="
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
            

        tv = Panel(conteudo, title="[ TV ]", width=40)
        print(tv)

c = ControleRemoto()
c.liga_desliga()
c.mostrar_tv()