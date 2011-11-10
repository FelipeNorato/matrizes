class Matriz(object):


    def __init__(self, ordem):
        self.ordem = ordem
        self.representacao_matriz = [[] for lista_matriz in range(1 , ordem + 1)]
        self.repr_termos = []
        self.result_x = []
        self._value = [None for lista_matriz in range(1 , ordem +1)]

    def __getitem__(self, i):
        return self.representacao_matriz[i]

    def __eq__(self, representacao_matriz):
        return self.representacao_matriz == representacao_matriz

    def verificar_matriz(self):
        pass

    @property
    def todas_as_posicoes(self):
        for linha in range(1, self.ordem + 1):
            for coluna in range(1, self.ordem +1):
                yield linha, coluna

    def set_matriz(self, **kwargs):
        """ O valor sera vinculada a uma chave em um dicionario da seguinte maneira:
                    a[linha][coluna]=valor, (a11=1, a12=3..)
        """
        for linha, coluna in self.todas_as_posicoes:
            posicao = ''.join(map(str,['a', linha, coluna]))
            self[linha - 1].append(kwargs[posicao])
        self.verificar_matriz()
        return self

    def termo_independente(self, **kwargs):
        """ O valor sera vinculada a uma chave em um dicionario da seguinte maneira:
                    b[linha]=valor, (b1=1, b2=3..)
        """
        for coluna in range(1, self.ordem +1):
            posicao = ''.join(map(str,['b', coluna]))
            self.repr_termos.append(kwargs[posicao])
        return self.repr_termos

class Superior(Matriz):

    def verificar_matriz(self):
        for linha, coluna in self.todas_as_posicoes:
            if linha > coluna and self[linha-1][coluna-1] != 0:
                raise MatrixError("A Matriz instanciada nao e Triangular Superior")

    def calcular(self):
        somatorio = 0
        for linha in range(self.ordem , 0 , -1):
            for coluna in range(self.ordem, 0, -1):
                if linha >= coluna:
                    somatorio +=0
                else:
                    somatorio += self[linha -1 ][coluna -1] * self._value[coluna -1]
            resultado = (self.repr_termos[linha - 1] - somatorio) / self[linha - 1][linha -1] 
            somatorio = 0
            self.result_x.insert(0, resultado)
            self._value[linha -1] = resultado
        return self.result_x

class Inferior(Matriz):

    def verificar_matriz(self):
        for linha, coluna in self.todas_as_posicoes:
            if linha < coluna and self[linha-1][coluna-1] != 0:
                raise MatrixError("A Matriz instanciada nao e Triangular Inferior")

    def calcular(self):
        somatorio = 0
        for linha in range(1, self.ordem + 1):
            for coluna in range(1, self.ordem + 1):
                if coluna >= linha:
                    somatorio +=0
                else:
                    somatorio += self[linha-1][coluna-1] * self.result_x[coluna - 1]
            resultado = (self.repr_termos[linha -1] + somatorio) /self[linha -1][linha -1]
            self.result_x.append(resultado) 
            somatorio = 0
        return self.result_x

class MatrixError(Exception):
    pass

