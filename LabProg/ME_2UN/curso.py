dados_curso = 'curso.txt'

class curso(): 
    def __init__(self): 
        self.nome = " "
        self.valor = " " 
        self.carga_horaria = " " 
        self.qtd_alunos = " "
        super().__init__()

    def cadastrar_curso(self):
        self.nome = input('Digite o nome do curso: ')
        self.valor = input('Digite o valor do curso: ')
        self.carga_horaria = input('Digite a carga horaria do curso: ')
        self.qnt_alunos = input('Digite a quantidade de alunos: ')

        self.lista_curso = [self.nome, self.valor, self.carga_horaria, self.qnt_alunos]

        print('Cadastro realizado com sucesso!')

        self.salvar()

    def salvar(self): 
        with open (dados_curso, 'a') as dados: 
            dados.write(str(self.lista_curso) + '\n')

    def exibir(self): 
        with open (dados_curso, 'r') as arquivo:
            for linha in arquivo: 
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)


