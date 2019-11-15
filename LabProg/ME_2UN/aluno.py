class aluno (p.pessoa): 
    def __init__(self):
        self.rg = " "
        self.cpf = " "
        self.convenio = " "
        self.matricula = " "
        self.facebook = " "
        self.linkedin = " "
        self.instagram = " "
        super().__init__()
    def cadastro_aluno (self): 
        self.rg = input('Digite o RG: ')
        self.cpf = input('Digite o CPF: ')
        self.convenio = input('Digite o convenio: ')
        self.matricula = input('Digite a matricula: ')
        self.facebook = input('Digite o facebook: ')
        self.linkedin = input('Digite o linkedin: ')
        self.instagram = input('Digite o instagram: ')
    self.lista_aluno = [self.rg, self.cpf, self.convenio, self.matricula, self.facebook, self.linkedin, self.instagram, self.p.nome, self.p.celular, self.p.email]

    print('Cadastro realizado com sucesso! ')
