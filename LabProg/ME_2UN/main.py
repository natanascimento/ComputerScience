#Menu#

import pessoa as p
import aluno as a 
import tecnicoadministrativo as t

class menu:

    def __init__(self):
        self.opcao = ' '
        self.subopcao = ' '
        self.p = p.pessoa()
        self.a = a.aluno()
        self.t = t.tecnico_administrativo()

    def main_menu(self):
        print('1  -  Pessoa\n')
        print('2 - Aluno\n')
        print('3 - Tecnico Adiminstrativo')
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

main = menu()
main.main_menu()