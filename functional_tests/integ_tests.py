from main.matrix import RunProgram as RP
import unittest

class MatrixIntegTest(unittest.TestCase):

    def test_steps_one(self):
        cmd = "I 5 6"
        matrix = RP(prompt=False, cmd=cmd)
        cmd = "L 2 3 A"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "S one.bmp"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)

        matrix_eg = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 'A', 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
        self.assertEquals(matrix.matrix, matrix_eg)

    def test_steps_two(self):
        matrix = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 'A', 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
        cmd = "G 2 3 J"
        RP(prompt=False, cmd=cmd, matrix=matrix)
        cmd = "V 2 3 4 W"
        RP(prompt=False, cmd=cmd, matrix=matrix)
        cmd = "H 3 4 2 Z"
        RP(prompt=False, cmd=cmd, matrix=matrix)
        cmd = "F 3 3 J"
        RP(prompt=False, cmd=cmd, matrix=matrix)
        cmd = "S two.bmp"
        RP(prompt=False, cmd=cmd, matrix=matrix)

        matrix_eg = [['J', 'J', 'J', 'J', 'J'],
                     ['J', 'J', 'Z', 'Z', 'J'],
                     ['J', 'W', 'J', 'J', 'J'],
                     ['J', 'W', 'J', 'J', 'J'],
                     ['J', 'J', 'J', 'J', 'J'],
                     ['J', 'J', 'J', 'J', 'J']]
        self.assertEquals(matrix, matrix_eg)

    def test_steps_three(self):
        cmd = "I 10 9"
        matrix = RP(prompt=False, cmd=cmd)
        cmd = "L 5 3 A"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "G 2 3 J"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "V 2 3 4 W"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "H 1 10 5 Z"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "F 3 3 J"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "K 2 7 8 8 E"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "F 9 9 R"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        cmd = "S one.bmp"
        RP(prompt=False, cmd=cmd, matrix=matrix.matrix)
        matrix_eg = \
            [['J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J'],
             ['J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J'],
             ['J', 'W', 'J', 'J', 'A', 'J', 'J', 'J', 'J', 'J'],
             ['J', 'W', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J'],
             ['Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z'],
             ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
             ['R', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'R', 'R'],
             ['R', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'R', 'R'],
             ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']]
        self.assertEquals(matrix.matrix, matrix_eg)

if __name__ == '__main__':
    unittest.main()
