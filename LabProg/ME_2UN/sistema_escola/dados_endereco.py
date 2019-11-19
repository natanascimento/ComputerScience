
dados_endereco = 'sistema_escola/dados_exportados/endereco.txt'

class endereco:
    def __init__(self): 
        self.logradouro = " "
        self.numero = " "
        self.complemento = " "
        self.bairro = " "
        self.cidade = " "
        self.uf = " "
        self.lista_endereco = ' '

    def cadastrar_endereco (self): 
        self.logradouro = input('Digite o endereço: ')
        self.numero = input('Digite o número: ')
        self.complemento = input('Digite o complemento: ')
        self.bairro = input('Digite o bairro: ')
        self.cidade = input('Digite a cidade: ')
        self.uf = input('Digite o uf: ')
    
        self.lista_endereco = [self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.uf]

        print('Cadastro relizado com sucesso!')

        self.salvar()
    
    def salvar(self):
        with open(dados_endereco, 'a') as dados: 
            dados.write(str(self.lista_endereco))
    
    def exibir(self):
        print('[logradouro, numero, complemento, bairro, cidade, UF]')
        with open(dados_endereco, 'r') as arquivo: 
            for linha in arquivo: 
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)