
from rich import print
import  time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.paginas_atual = 1

        print(F":open_book:[blue] Voce acabou de abrir o livro: [red]{self.titulo}[/], que tem [green]{self.total_paginas} paginas [/]no total. Voce agora esta na [yellow]pagina {self.paginas_atual} [/][/blue]")

    def avancar_paginas(self,qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.paginas_atual += 1
                print(f"Pag{self.paginas_atual} :arrow_forward:", end='')
                time.sleep(0.3)
                cont += 1
        print(f"[blue] Voce avançou {cont} paginas e agora esta na [yeloow] pagina{self.paginas_atual}[/] [/blue]")
    def fim_do_livro(self) -> bool:
       # if self.pagina == self.total_paginas:
           # return True
       # else:
           # return False
        return True if self.paginas_atual  == self.total_paginas else False

l1 = Livro ("10 coisas que aprendi", 20)

l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
