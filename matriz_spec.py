import unittest
from should_dsl import should
from matriz import Matriz, Superior, Inferior, MatrixError


class TestInstanciarMatriz(unittest.TestCase):


    def setUp(self):
        self.matriz = Matriz(ordem=3)

    def test_matriz_ordem_3(self):
        self.matriz.representacao_matriz |should| equal_to([[],[],[]])

    def test_matriz_preenchida(self):
        self.matriz.set_matriz(a11=3, a12=1, a13=0, 
                               a21=0, a22=2, a23=-1, 
                               a31=0, a32=0, a33=3) \
                 |should| equal_to([[3, 1, 0],
                                    [0, 2,-1],
                                    [0, 0, 3]])

    def test_termo_independente(self):
        self.matriz.termo_independente(b1=4, b2=2, b3=0) |should| equal_to([4,2,0])

class TestMatrizTriangularSuperior(unittest.TestCase):


    def test_calculo_matriz_triangular_superior(self):
        self.superior = Superior(ordem=3)
        self.superior.set_matriz(a11=3, a12=1, a13=0, 
                                 a21=0, a22=2, a23=-1, 
                                 a31=0, a32=0, a33=3) 

        self.superior.termo_independente(b1=4, b2=2, b3=0)
        self.superior.calcular() |should| equal_to([1,1,0])

    def test_calculo_matriz_triangular_superior_eduardo(self):
        self.superior = Superior(ordem=3)
        self.superior.set_matriz(a11=1, a12= 1, a13=1, 
                                 a21=0, a22=-1, a23=2, 
                                 a31=0, a32= 0, a33=5) 

        self.superior.termo_independente(b1=10, b2=0, b3=5)
        self.superior.calcular() |should| equal_to([7,2,1])

    def test_erro_matriz_nao_triangular_superior(self):
        self.superior = Superior(ordem=3)
        (lambda: \
        self.superior.set_matriz(a11=3, a12=1, a13=0,
                                 a21=1, a22=2, a23=-1, 
                                 a31=0, a32=0, a33=3))\
                                 |should| throw(MatrixError, message="A Matriz instanciada nao e Triangular Superior")

class TestMatrizTriangularInferior(unittest.TestCase):


    def test_calculo_matriz_triangular_inferior(self):
        self.inferior = Inferior(ordem=3)
        self.inferior.set_matriz(a11=2 ,a12=0 ,a13=0,
                                 a21=1 ,a22=4 ,a23=0,
                                 a31=1 ,a32=1 ,a33=1)

        self.inferior.termo_independente(b1=2 ,b2=-3 , b3=1 )
        self.inferior.calcular() |should| equal_to([1, -1, 1])

    def test_calculo_matriz_triangular_inferior_inventada(self):
        self.inferior = Inferior(ordem=3)
        self.inferior.set_matriz(a11=-2 ,a12=0 ,a13=0,
                                 a21= 3 ,a22=1 ,a23=0,
                                 a31= 2 ,a32=1 ,a33=2)

        self.inferior.termo_independente(b1=2 ,b2=-3 , b3=1 )
        self.inferior.calcular() |should| equal_to([-1, -6, -4])

    def test_erro_matriz_nao_triangular_inferior(self):
        self.inferior = Inferior(ordem=3)
        (lambda:
        self.inferior.set_matriz(a11=-2 ,a12=0 ,a13=1,
                                 a21= 3 ,a22=1 ,a23=0,
                                 a31= 2 ,a32=1 ,a33=2))\
                                 |should| throw(MatrixError, message="A Matriz instanciada nao e Triangular Inferior")

