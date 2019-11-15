dados_professor = 'professor.txt'

class professor (): 
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
        self.lista_professor = [self.matricula_professor, self.titulacao, self.especialidade, self.plus_salario, self.salario_hora, self.linkedin, self.lattes, self.nivel]

        print('Cadastro realizado com sucesso! ')

        self.salvar()
    
    
    def salvar(self):
        with open(dados_professor, 'a') as dados:
            dados.write(str(self.lista_professor) + '\n')
    

    def exibir(self):
        with open(dados_professor, 'r') as arquivo:
            for linha in arquivo:
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)

