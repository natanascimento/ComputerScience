
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
    
    
