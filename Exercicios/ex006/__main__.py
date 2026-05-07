#from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main ():
    a1 = Aluno("José", 17, "informatica", "T01")
    a1.fazer_aniversario()   # acrescentou mais um ano
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor("Miro", 63, "Mestrado", "10")
    p1.dar_aula()
    #inspect(p1, methods=True)

    f1 = Funcionario("Claudia", 21, "Secretária", "Diretoria")
    f1.fazer_aniversario()
    f1.bater_ponto()
    #inspect(f1, methods=True)

if __name__ == "__main__":
    main()