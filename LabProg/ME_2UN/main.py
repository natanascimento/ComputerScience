#Menu#

import pessoa as p

class menu:

    def __init__(self):
        self.opcao = ' '
        self.subopcao = ' '
        self.p = p.pessoa()
    def main_menu(self):
        print('1  -  Pessoa\n')
        self.opcao = input('Informe uma opção: ')

        if self.opcao == '1':
            print('1  -  Cadastrar Pessoa \n2  -  Exibir Pessoa')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.p.cadastrar_pessoa()
            if self.subopcao == '2':
                self.p.exibir()

main = menu()
main.main_menu()