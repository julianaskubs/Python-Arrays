# !/usr/bin/python
# -*- coding: utf8 -*-

from PIL import Image
import numpy as np


def main():
    RunProgram()


class RunProgram:
    def __init__(self, prompt=True, cmd=None, matrix=[]):
        self.matrix = matrix
        if prompt:
            while True:
                self.user_input = input()

                if len(self.user_input) > 0:
                    if self.user_input[0] == 'X':
                        break
                    else:
                        if self.user_input[0] in ('I', 'C', 'L', 'V', 'H', 'K', 'F', 'S'):
                            self.val_input()
        else:
            self.user_input = cmd
            if len(self.user_input) > 0:
                if self.user_input[0] in ('I', 'C', 'L', 'V', 'H', 'K', 'F', 'S'):
                    self.val_input()

    def val_input(self):
        """
        Essa funcao valida a entrada de acordo com a string user_input e
        chama a funcao correspondente ao comando.
        """
        if self.user_input[0] == 'I':
            self.create()
        elif self.user_input[0] == 'C':
            self.clear()
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

    def create(self):
        """
        Funcao que cria uma matriz de acordo com os valores de entrada.
        Todos os elementos dessa matriz contem valor 0.
        """
        try:
            self.matrix = []
            s = self.user_input
            s = s.strip()
            list_s = s.split(' ', 2)
            m = int(list_s[1])
            n = int(list_s[2])
            for x in range(n):
                l = []
                for y in range(m):
                    l.append(0)
                self.matrix.append(l)
        except:
            print('Paramaters not enough to create matrix')

    def clear(self):
        """
        Funcao que limpa a matriz, percorrendo-a linha a linha e passando valor 0.
        Enumerate recebe uma lista e devolve o indice e o valor de cada elemento.
        """
        for i, item in enumerate(self.matrix):
            for j, _item in enumerate(item):
                item[j] = 0

    def color_pix(self):
        """
         Funcao que colore um pixel, de acordo com as coordenadas.
         x = coluna, y = linha, c = cor.
        """
        try:
            # o indice na matriz comeca com 0, subtrair 1 para localizar o elemento em sua posicao
            s = self.user_input
            s = s.strip()
            list_s = s.split(' ', 3)
            x = int(list_s[1]) - 1
            y = int(list_s[2]) - 1
            c = str(list_s[3])
            for i, item in enumerate(self.matrix):
                if i == y:
                    for j, _item in enumerate(item):
                        if j == x:
                            item[j] = c
                            break
        except:
            print('Paramaters not enough to update matrix')

    def draw_vert(self):
        """
        Funcao que desenha um segmento vertical na coluna x, da linha y1 ate a linha y2
        """
        try:
            # o indice na matriz comeca com 0, subtrair 1 para localizar o elemento em sua posicao
            s = self.user_input
            s = s.strip()
            list_s = s.split(' ', 4)
            x = int(list_s[1]) - 1
            y1 = int(list_s[2]) - 1
            y2 = int(list_s[3]) - 1
            c = str(list_s[4])

            for i, item in enumerate(self.matrix):
                # se o indice da linha estiver entre y1 e y2
                if y1 <= i <= y2:
                    for j, _item in enumerate(item):
                        # se o indice da coluna for igual a x
                        if j == x:
                            item[j] = c
        except:
            print('Paramaters not enough to update matrix')

    def draw_horiz(self):
        """
         Funcao que desenha um segmento horizontal na linha y, da coluna x1
         ate a coluna x2.
        """
        try:
            # o indice na matriz comeca com 0, subtrair 1 para localizar o elemento em sua posicao
            s = self.user_input
            s = s.strip()
            list_s = s.split(' ', 4)
            x1 = int(list_s[1]) - 1
            x2 = int(list_s[2]) - 1
            y = int(list_s[3]) - 1
            c = str(list_s[4])

            for i, item in enumerate(self.matrix):
                # se o indice da linha for igual a y
                if i == y:
                    for j, _item in enumerate(item):
                        # se o indice da coluna estiver entre x1 e x2
                        if x1 <= j <= x2:
                            item[j] = c
        except:
            print('Paramaters not enough to update matrix')

    def draw_rect(self):
        """
        Funcao que desenha um retangulo de cor C, x1,y1 e o canto superior esquerdo e
        x2, y2 eh o canto inferior direito
        x =  coluna, y = linha, c = cor.
        """
        try:
            # o indice na matriz comeca com 0, subtrair 1 para localizar o elemento em sua posicao
            s = self.user_input
            s = s.strip()
            list_s = s.split(' ', 5)
            x1 = int(list_s[1]) - 1
            y1 = int(list_s[2]) - 1
            x2 = int(list_s[3]) - 1
            y2 = int(list_s[4]) - 1
            c = str(list_s[5])

            for i, item in enumerate(self.matrix):
                # se o indice da linha estiver entre y1 e y2
                if y1 <= i <= y2:
                    for j, _item in enumerate(item):
                        # se o indice da coluna estiver entre x1 e x2
                        if x1 <= j <= x2:
                            item[j] = c
        except:
            print('Paramaters not enough to update matrix')

    def fill_region(self):
        """
        Preenche a regiao com a cor C de acordo com as coordenadas. Se houver outro pixel com a cor da
        regiao, e tiver pelo menos um lado em comum com um pixel pertencente a regiao, ele tambem
        fara parte da regiao.
        x = linha, y = coluna, c = cor, pos= lista de indices das linhas, old_c = valor antigo
        da coordenada, region = lista das linhas que serao alteradas na matriz.
        No primeiro for, cria-se uma lista com o indice de todas as linhas que contem pelo menos
        um elemento com o valor antigo, de acordo com as coordenadas (lista pos).
        No segundo for, cria-se uma variavel de controle, que contem a posicao da linha principal,
        de acordo com a coordenada y, dentro da lista pos.
        No terceiro for, compara-se a diferenca entre a posicao de cada item na lista pos e o seu valor,
        em relacao a posicao e valor da linha y dentro da lista pos.
        Como cada elemento na lista pos refere-se a um indice de linha na matriz, se houver diferenca
        entre a posicao e o valor, significa que o elemento esta fora da sequencia, em relacao a y.
        Nesse caso, a linha nao entra na regiao.
        No ultimo for, altera-se os valores de acordo com a lista region e a variavel old c.
        """
        try:
            # o indice na matriz comeca com 0, subtrair 1 para localizar o elemento em sua posicao
            s = self.user_input
            s = s.strip()
            list_s = s.split(' ', 3)
            x = int(list_s[1]) - 1
            y = int(list_s[2]) - 1
            c = str(list_s[3])
            old_c = self.matrix[x][y]
            pos = []
            control = -1  # verificar o que acontece se alguem digita algo fora do contexto
            region = []

            # para cada linha na matriz, se ao menos 1 elem igual a old_c, add indice na lista pos.
            for i, line in enumerate(self.matrix):
                for elem in line:
                    if elem == old_c:
                        pos.append(i)
                        break

            # Cria uma variavel de controle contendo o indice de y na lista pos, usado no prox for.
            for i, item in enumerate(pos):
                if item == y:
                    control = i
                    break

            # Para cada indice e valor na lista pos, se a diferenca em relacao a posicao de y
            # e o indice for igual a diferenca entre o valor de y e o valor, significa que
            # a linha esta dentro da sequencia de linhas e faz parte da regiao.
            for index, value in enumerate(pos):
                if value < y:
                    if (control - index) == (y - value):
                        region.append(value)
                elif value > y:
                    if (index - control) == (value - y):
                        region.append(value)
                elif value == y:
                    region.append(value)

            # Percorre a matriz alterando os valores de acordo com a lista region e old_c.
            for i, line in enumerate(region):
                for j, elem in enumerate(self.matrix[line]):
                    if elem == old_c:
                        self.matrix[line][j] = c
        except:
            print('Paramaters not enough to update matrix')

    def save_img(self):
        """
        Funcao que salva a imagem e imprime na tela a matriz atual.
        """
        try:
            s = self.user_input
            s = s.strip()
            list_s = s.split(' ', 2)
            img_nm = str(list_s[1])
            print(img_nm)
            print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.matrix]))
            c = np.asarray(self.matrix)
            img = Image.fromarray(c, 'RGB')
            img.save('../images/{}'.format(img_nm))
            img.show()
        except Exception as e:
            print('Paramaters not enough to create image')

if __name__ == '__main__':
    main()
