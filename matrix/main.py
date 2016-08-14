# !/usr/bin/python
# -*- coding: utf8 -*-


def main():
    RunProgram()


class RunProgram:
    def __init__(self):
        """
        Para padronizar a quantidade de espacos que o usuario poderia digitar entre os caracteres,
        foi criado uma string inp, que recebe a entrada, retira todos os espacos e depois coloca
        apenas um espaco entre cada caracter.
        """
        self.matrix = []
        while True:
            inp = input()
            inp = inp.replace(' ', '').replace('', ' ')
            # retirando os 2 espacos a mais em inp (um na pos 0 e um na ultima posicao).
            last_pos = len(inp) - 1
            inp = inp[1:last_pos]
            self.user_input = inp
            print(len(self.user_input))  # APAGAR

            if len(self.user_input) > 0:
                if self.user_input[0] == 'X':
                    break
                else:
                    if self.user_input[0] in ('I', 'C', 'L', 'V', 'H', 'K', 'F', 'S'):
                        self.val_input()

    def val_input(self):
        """
        Essa funcao valida a entrada de acordo com a string user_input e
        entao chama a funcao correspondente ao comando.
        """
        if self.user_input[0] == 'I' and len(self.user_input) == 5:
            self.create()
        elif self.user_input[0] == 'C' and len(self.user_input) == 1:
            self.clear()
        elif self.user_input[0] == 'L' and len(self.user_input) == 7:
            self.color_pix()
        elif self.user_input[0] == 'V' and len(self.user_input) == 9:
            self.draw_vert()
        elif self.user_input[0] == 'H' and len(self.user_input) == 9:
            self.draw_horiz()
        elif self.user_input[0] == 'K':
            self.draw_rect()
        elif self.user_input[0] == 'F' and len(self.user_input) == 7:
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
            m = int(self.user_input[2])
            n = int(self.user_input[4])
            for x in range(n):
                l = []
                for y in range(m):
                    l.append(0)
                self.matrix.append(l)
            # self.matrix = [[0 for x in range(m)] for y in range(n)]  # forma simplificada.
        except:
            print('Paramaters not enough to create a matrix')

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
            x = int(self.user_input[2]) - 1
            y = int(self.user_input[4]) - 1
            c = self.user_input[6]
            for i, item in enumerate(self.matrix):
                if i == y:
                    for j, _item in enumerate(item):
                        if j == x:
                            item[j] = c
        except:
            print('Paramaters not enough to update matrix')

    def draw_vert(self):
        """
        Funcao que desenha um segmento vertical na coluna x, da linha y1 ate a linha y2
        """
        try:
            # o indice na matriz comeca com 0, subtrair 1 para localizar o elemento em sua posicao
            x = int(self.user_input[2]) - 1
            y1 = int(self.user_input[4]) - 1
            y2 = int(self.user_input[6]) - 1
            c = self.user_input[8]
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
            x1 = int(self.user_input[2]) - 1
            x2 = int(self.user_input[4]) - 1
            y = int(self.user_input[6]) - 1
            c = self.user_input[8]
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
            x1 = int(self.user_input[2]) - 1
            y1 = int(self.user_input[4]) - 1
            x2 = int(self.user_input[6]) - 1
            y2 = int(self.user_input[8]) - 1
            c = self.user_input[10]

            for i, item in enumerate(self.matrix):
                # se o indice da linha estiver entre y1 e y2
                if y1 <= i <= y2:
                    for j, _item in enumerate(item):
                        # se o indice da coluna estiver entre x1 e x2
                        if x1 <= j <= x2:
                            item[j] = c

            print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.matrix]))
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
            x = int(self.user_input[2]) - 1
            y = int(self.user_input[4]) - 1
            c = self.user_input[6]
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

            print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.matrix]))
        except:
            print('Paramaters not enough to update matrix')

if __name__ == '__main__':
    main()
