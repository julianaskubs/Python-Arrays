# !/usr/bin/python
# -*- coding: utf8 -*-


def main():
    RunProgram()


class RunProgram:
    def __init__(self):
        self.matrix = []
        while True:
            # para padronizar a qtde de espacos, retirar todos os espacos e depois colocar
            # um espaco so entre cada caracter
            inp = input()
            inp = inp.replace(' ', '').replace('', ' ')
            # agora a string contem espaco no inicio e no fim, para tirar esses espacos remontamos
            # a string pegando da posicao 1 ate a ultima posicao, mas sem incluir a ultima posicao
            last_pos = len(inp) - 1
            inp = inp[1:last_pos]  # up to but not including
            self.user_input = inp
            print(len(self.user_input))

            if len(self.user_input) > 0:
                if self.user_input == 'X':
                    break
                else:
                    if self.user_input[0] in ('I', 'C', 'L', 'V', 'H', 'K', 'F', 'S'):
                        self.val_input()

    # valida a entrada de acordo com o primeiro caracter da string e chama o metodo correspondente
    def val_input(self):
        if self.user_input[0] == 'I' and len(self.user_input) == 5:
            self.create_m()
        elif self.user_input[0] == 'C' and len(self.user_input) == 1:
            self.clear_m()
        elif self.user_input[0] == 'L' and len(self.user_input) == 7:
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

    # Cria uma matriz de acordo com os parametros, todas as posicoes contendo valor 0
    def create_m(self):
        try:
            m = int(self.user_input[2])
            n = int(self.user_input[4])
            self.matrix = [[0 for x in range(m)] for y in range(n)]
            # print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.matrix]))
        except:
            print('Paramaters not enough to create a matrix')

    # Limpa a matriz, percorrendo-a linha a linha
    def clear_m(self):
        for i, item in enumerate(self.matrix, 0):
            for j, _item in enumerate(item, 0):
                item[j] = 0

        print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.matrix]))

    # Colore um pixel, de acordo com as coordenadas
    def color_pix(self):
        m = int(self.user_input[2])
        n = int(self.user_input[4])
        c = self.user_input[6]
        for i, item in enumerate(self.matrix, 0):
            # por causa do indice 0, substraimos 1 para colorir na coordenada digitada
            if i == n - 1:
                for j, _item in enumerate(item, 0):
                    if j == m - 1:
                        item[j] = c
        print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.matrix]))



if __name__ == '__main__':
    main()
