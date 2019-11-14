import pickle

dados_pessoa = 'pessoa.pickle'

class pessoa:

    def __init__(self):
        self.nome = " "
        self.celular = " "
        self.email = " "
    
    def cadastrar_pessoa (self):
        self.nome = input('Informe seu nome: ')
        self.celular = input('Informe seu celular: ')
        self.email = input('Informe seu email: ')

        lista_pessoa = [self.nome, self.celular, self.email]

        pickle.dump(lista_pessoa, open(dados_pessoa, 'ab+'))

        print ('Cadastro Realizado com Sucesso!')

        #exportando os dados
        self.save_pessoa()

    def exibir_pessoa(self):
        print('nome, celular, email')
        with open ('pessoa.txt', 'r') as arquivo:
            for linhas in arquivo:
                linhas_em_branco = linhas.strip()
                print(linhas_em_branco)

    def save_pessoa (self):
        with open ('pessoa.txt', 'a') as dados:
            nova_lista = pickle.load(open(dados_pessoa, 'rb'))
            dados.write(str(nova_lista) + '\n')