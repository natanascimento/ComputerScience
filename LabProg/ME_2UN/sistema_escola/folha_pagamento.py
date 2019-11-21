
from sistema_escola import dados_professor as prof

class folha():

    def __init__(self):
        self.salario_bruto = ' '
        self.inss = ' '
        self.irrf = ' '
        self.salario_liquido = ' '
        self.prof = prof.professor()

    def set_salario_prof(self):
        self.prof.exibir_salario()