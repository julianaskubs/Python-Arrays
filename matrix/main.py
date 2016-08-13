# !/usr/bin/python
# -*- coding: utf8 -*-
import re


def main():
    RunProgram()


class RunProgram:
    def __init__(self):
        while True:
            # para padronizar a qtde de espacos, juntar todos os caracteres e depois separa-los,
            # no caso da entrada estar com quantidades diferentes de espacos
            inp = input()
            inp = inp.replace(' ', '').replace('', ' ')
            len_inp = len(inp) - 1
            inp = inp[1:len_inp]  # up to but not including
            self.user_input = inp

            if self.user_input == 'X':
                break
            else:
                if self.user_input[0] in ('I', 'C', 'L', 'V', 'H', 'K', 'F', 'S'):
                    self.val_input()

    # valida a entrada de acordo com a primeira String e chama o metodo correspondente
    def val_input(self):
        if self.user_input[0] == 'I':
            self.create_m()
        elif self.user_input[0] == 'C':
            self.clear_m()
        elif self.user_input[0] == 'L':
            self.color_pix()
        elif self.user_input[0] == 'V':
            self.draw_vert()
        elif self.user_input[0] == 'H':
            self.draw_horiz()
        elif self.user_input[0] == 'K':
            self.draw_rect()
        elif self.user_input[0] == 'F':
            self.fill_region()
        elif self.user_input[0] == 'S':
            self.save_img()

    # Cria uma matriz de acordo com os parametros
    def create_m(self):
        try:
            m = int(self.user_input[2])
            n = int(self.user_input[4])
            print(type(m))
            matrix = [[0 for x in range(m)] for y in range(n)]
            # Sprint('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in matrix]))
        except:
            print('Paramaters not enough to create a matrix')


if __name__ == '__main__':
    main()
