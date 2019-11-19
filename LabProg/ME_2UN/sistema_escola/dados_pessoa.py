#Classe Pessoa#

dados_pessoa = 'pessoa.txt'

class pessoa:

    def __init__(self):
        self.nome = " "
        self.celular = " "
        self.email = " "
        self.lista_pessoa = ' '

    def cadastrar_pessoa (self):
        self.nome = input('Informe seu nome: ')
        self.celular = input('Informe seu celular: ')
        self.email = input('Informe seu email: ')

        self.lista_pessoa = [self.nome, self.celular, self.email]

        self.salvar()

    def salvar(self):
        with open (dados_pessoa, 'a') as dados:
            dados.write(str(self.lista_pessoa))

    def exibir(self):
        with open (dados_pessoa, 'r') as arquivo:
            for linha in arquivo:
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)
                
