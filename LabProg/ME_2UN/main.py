#Menu#

import pessoa as p
import aluno as a 
import tecnicoadministrativo as t
import professor as f
import curso as c 


class menu:

    def __init__(self):
        self.opcao = ' '
        self.subopcao = ' '
        self.p = p.pessoa()
        self.a = a.aluno()
        self.t = t.tecnico_administrativo()
        self.f = f.professor()
        self.c = c.curso()

    def main_menu(self):
        print('1  -  Pessoa\n')
        print('2 - Aluno\n')
        print('3 - Tecnico Adiminstrativo\n')
        print('4 - Professor\n')
        print('5 - Curso\n ')
        self.opcao = input('Informe uma opção: ')


        if self.opcao == '1':
            print('1  -  Cadastrar Pessoa \n2  -  Exibir Pessoa')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.p.cadastrar_pessoa()
            if self.subopcao == '2':
                self.p.exibir()
        
        
        if self.opcao == '2':
            print('1  - Cadastrar Aluno\n2  -  Exibir Aluno')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.a.cadastro_aluno()
            if self.subopcao == '2':
                self.a.exibir_aluno()
        
        if self.opcao == '3':
            print('1  -  Cadastrar Tecnico Administrativo \n2  -  Exibir Tecnico Administrativo')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.t.cadastro_tecnico_administrativo()
            if self.subopcao == '2':
                self.t.exibir()
        
        
        if self.opcao == '4':
            print('1  -  Cadastrar Professor\n2  -  Exibir Professor')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1': 
                self.f.cadastrar_professor()
            if self.subopcao == '2':
                self.f.exibir()
        
        
        if self.opcao == '5':
            print('1  -   Cadastrar Curso \n2  -  Exibir Curso')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.c.cadastrar_curso()
            if self.subopcao == '2':
                self.c.exibir()           
        

main = menu()
main.main_menu()