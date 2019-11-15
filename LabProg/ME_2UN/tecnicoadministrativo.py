dados_tecnico_administrativo = 'tecnico_administrativo.txt'

import pessoas as p 

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
        self.lista_tecnico_administrativo = [self.matricula_funcional, self.cargo, self.cpf, self.salario_mes, self.nivel]
        super().cadastrar_pessoa() 
        print('Cadastro realizado com sucesso! ')

        self.salvar()
    
    def salvar(self):
        with open(dados_tecnico_administrativo, 'a') as dados: 
            dados.write(str(self.lista_tecnico_administrativo) + '\n')
    
    
    def exibir(self):
        with open(dados_tecnico_administrativo, 'r') as arquivo: 
            for linha in arquivo: 
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)
