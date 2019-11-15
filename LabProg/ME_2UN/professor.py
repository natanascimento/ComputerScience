class professor (p.pessoa): 
    def __init__(self): 
        self.matricula_professor = " "
        self.titulacao = " "
        self.especialidade = " "
        self.plus_salario = " "
        self.salario_hora = " "
        self.linkedin = " "
        self.lattes = " "
        self.nivel = " "
        super().__init__()
    def cadastrar_professor(self):
        self.matricula_professor = input('Digite a matricula do professor: ')
        self.titulacao = input('Digite a titulação: ')
        self.especialidade = input('Digite a especialidade: ')
        self.plus_salario= input('Digite o plus salario: ')
        self.salario_hora = input('Digite o salario por hora: ')
        self.linkedin = input('Digite o Linkedin: ')
        self.lattes = input('Digite o lattes: ')
        self.nivel = input('Digite o nivel: ')
    self.lista_professor = [self.matricula_professor, self.titulacao, self.especialidade, self.plus_salario, self.salario_hora, self.linkedin, self.lattes, self.nivel, self.p.nome, self.p.celular, self.p.email]

    print('Cadastro realizado com sucesso! ')
