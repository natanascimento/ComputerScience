from sistema_escola import dados_professor as prof

dados_curso = 'sistema_escola/dados_exportados/curso.txt'
valor_curso = 'sistema_escola/dados_exportados/valor_total_curso.txt'

class curso(): 
    def __init__(self): 
        self.nome = " "
        self.valor = " " 
        self.carga_horaria = " " 
        self.qtd_alunos = " "
        self.lista_curso = ' '
        self.lista_valor = ' '
        self.prof = prof.professor()

    def cadastrar_curso(self):
        self.nome = input('Digite o nome do curso: ')
        self.valor = float(input('Digite o valor do curso: '))
        self.carga_horaria = input('Digite a carga horaria do curso: ')
        self.qnt_alunos = int(input('Digite a quantidade de alunos: '))

        self.lista_curso = [self.nome, self.valor, self.carga_horaria, self.qnt_alunos]

        print('Cadastro realizado com sucesso!')

        self.calcular_valor_curso()

        self.salvar()

    def salvar(self): 
        with open (dados_curso, 'a') as dados: 
            dados.write(str(self.lista_curso))

    def exibir(self):
        print('[nome, valor, carga_horario, qnt_alunos]')
        with open (dados_curso, 'r') as arquivo:
            for linha in arquivo: 
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)

#Calculando valor total do curso

    def calcular_valor_curso (self):
        self.valor_total_curso = (self.valor * self.qnt_alunos)

        if self.valor_total_curso == self.prof.describenivel:
            print ('Ta Pago')

        self.lista_valor = [self.valor_total_curso]

        self.salvar_valor()

    def salvar_valor(self): 
        with open (valor_curso, 'a') as dados: 
            dados.write(str(self.lista_valor) + '\n')
    
    def exibir_valor (self):
        with open (valor_curso, 'r') as arquivo:
            for linha in arquivo: 
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)


