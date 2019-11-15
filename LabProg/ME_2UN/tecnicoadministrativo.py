class tecnico_administrativo(p.pessoa):
    def __init__ (self): 
        self.matricula_funcional = " "
        self.cargo = " "
        self.cpf = " "
        self.salario_mes = " "
        self.nivel = " "
        super().__init__()
    def cadastro_tecnico_administrativo (self):
        self.matricula_funcional = input('Digite a matricula funcional: ')
        self.cargo = input('Digite o cargo: ')
        self.cpf = input('Digite o cpf: ')
        self.salario_mes = input('Digite o salário: ')
        self.nivel = input('Digite o nivel: ')
    self.lista_tecnico_administrativo = [self.matricula_funcional, self.cargo, self.cpf, self.salario_mes, self.nivel, self.p.nome, self.p.celular, self.p.email]

    print('Cadastro realizado com sucesso! ')
