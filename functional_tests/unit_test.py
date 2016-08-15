import unittest
from main.matrix import RunProgram as RP

class MatrixUnitTest(unittest.TestCase):

    def test_create_new_matrix(self):
        """
        Funcao de teste que cria duas matrizes, uma via classe RunProgram
        e outra via classe MatrixUnitTest, e compara se estao iguais.
        """
        cmd = "I 8 12"
        matrix = RP(prompt=False, cmd=cmd)
        matrix.create()
        matrix_eg = [[0 for x in range(8)] for y in range(12)]
        self.assertEquals(matrix.matrix, matrix_eg)

    def test_clear_matrix(self):
        """
         Funcao de teste que cria duas matrizes com todos elementos com valor = B,
         uma via classe RunProgram e outra via classe MatrixUnitTest,
         limpa e compara se estao iguais.
        """
        cmd = "C"
        matrix = [['B' for x in range(8)] for y in range(12)]
        RP(prompt=False, cmd=cmd, matrix=matrix)
        matrix_eg = [[0 for x in range(8)] for y in range(12)]
        self.assertEquals(matrix, matrix_eg)

    def test_color_a_pixel(self):
        """
        Funcao de teste que cria duas matrizes, uma via classe RunProgram e outra via
        classe MatrixUnitTest, colore um elemento em cada uma e compara se estao iguais.
        """
        cmd = "L 2 5 B"
        matrix = [[0 for x in range(8)] for y in range(8)]
        RP(prompt=False, cmd=cmd, matrix=matrix)
        matrix_eg = [[0 for x in range(8)] for y in range(8)]
        matrix_eg[4][1] = "B"
        self.assertEquals(matrix, matrix_eg)

    def test_color_a_pixel_not_equal(self):
        """
        Funcao de teste que cria duas matrizes, uma via classe RunProgram e outra via
        classe MatrixUnitTest, colore um elemento em cada uma, porem em posicoes diferentes,
        e compara se estao diferentes.
        """
        cmd = "L 2 5 B"
        matrix = [[0 for x in range(8)] for y in range(8)]
        RP(prompt=False, cmd=cmd, matrix=matrix)
        matrix_eg = [[0 for x in range(8)] for y in range(8)]
        matrix_eg[4][2] = "B"
        self.assertNotEquals(matrix, matrix_eg)

    def test_draw_vertical(self):
        """
        Funcao de teste que cria duas matrizes, uma via classe RunProgram e outra via
        classe MatrixUnitTest, desenha um segmento vertical em cada uma e compara
        se estao iguais.
        """
        cmd = "V 3 2 6 X"
        matrix = [[0 for x in range(8)] for y in range(8)]
        RP(prompt=False, cmd=cmd, matrix=matrix)
        matrix_eg = [[0 for x in range(8)] for y in range(8)]
        for i, line in enumerate(matrix_eg):
            # se o indice da linha estiver entre 1 e 5 (linhas 2 a 6)
            if i in range(1, 6):
                # coluna 3 recebe 'X'
                line[2] = 'X'
        self.assertEquals(matrix, matrix_eg)

    def test_draw_horizontal(self):
        """
        Funcao de teste que cria duas matrizes, uma via classe RunProgram e outra via
        classe MatrixUnitTest, desenha um segmento horizontal em cada uma e compara
        se estao iguais.
        """
        cmd = "H 1 8 4 P"
        matrix = [[0 for x in range(8)] for y in range(8)]
        RP(prompt=False, cmd=cmd, matrix=matrix)
        matrix_eg = [[0 for x in range(8)] for y in range(8)]
        # para cada elemento na linha 4
        for i, elem in enumerate(matrix_eg[3]):
            # se o elemento estiver entre 0 e 7 (colunas 1 a 8), elem recebe 'P'
            if i in range(0, 8):
                matrix_eg[3][i] = 'P'
        self.assertEquals(matrix, matrix_eg)

    def test_draw_rectangle(self):
        """
        Funcao de teste que cria duas matrizes, uma via classe RunProgram e outra via
        classe MatrixUnitTest, desenha um retangulo em cada uma e compara se estao iguais.
        """
        cmd = "K 3 6 7 7 Q"
        matrix = [[0 for x in range(8)] for y in range(8)]
        RP(prompt=False, cmd=cmd, matrix=matrix)
        matrix_eg = [[0 for x in range(8)] for y in range(8)]
        for i, line in enumerate(matrix_eg):
            # se o indice da linha estiver entre 5 e 6 (linhas 6 a 7)
            if i in range(5, 7):
                for j, elem in enumerate(line):
                    # se o indice do elem estiver entre 2 e 6 (colunas 3 a 7), recebe 'Q'
                    if j in range(2, 7):
                        line[j] = 'Q'
        self.assertEquals(matrix, matrix_eg)

    def test_fill_a_region(self):
        """
        Funcao de teste que cria duas matrizes, uma via classe RunProgram e outra via
        classe MatrixUnitTest, colore um elemento em cada uma, preenche a regiao e
        compara se estao iguais.
        """
        cmd = "I 2 2"
        matrix = RP(prompt=False, cmd=cmd)
        cmd = "L 1 1 A"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "F 1 1 B"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        matrix_eg = [[0 for x in range(2)] for y in range(2)]
        matrix_eg[0][0] = "B"
        self.assertEquals(matrix.matrix, matrix_eg)

if __name__ == '__main__':
    unittest.main()
