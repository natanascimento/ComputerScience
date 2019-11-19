dados_tecnico_administrativo = 'sistema_escola/dados_exportados/tecnico_administrativo.txt'

from sistema_escola import dados_pessoa as p 

class tecnico_administrativo(p.pessoa):
    def __init__ (self): 
        self.matricula_funcional = " "
        self.cargo = " "
        self.cpf = " "
        self.salario_mes = " "
        self.nivel = " "
        self.lista_tecnico_administrativo = " "
        super().__init__()
    
    
    def cadastro_tecnico_administrativo (self):
        super().cadastrar_pessoa()
        self.matricula_funcional = input('Digite a matricula funcional: ')
        self.cargo = input('Digite o cargo: ')
        self.cpf = input('Digite o cpf: ')
        self.salario_mes = input('Digite o salário: ')
        self.nivel = input('Digite o nivel: ') 
        
        self.lista_tecnico_administrativo = [self.nome, self.celular, self.email, self.matricula_funcional, self.cargo, self.cpf, self.salario_mes, self.nivel]
        
        print('Cadastro realizado com sucesso! ')

        self.salvar()
    
    def salvar(self):
        with open(dados_tecnico_administrativo, 'a') as dados: 
            dados.write(str(self.lista_tecnico_administrativo + '\n'))
    
    
    def exibir(self):
        print('[nome, celular, email, matricula_funcionario, cargo, cpf, salario_mes, nivel]')
        with open(dados_tecnico_administrativo, 'r') as arquivo: 
            for linha in arquivo: 
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)
