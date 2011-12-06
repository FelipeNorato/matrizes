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

    def _verificar_matriz(self):
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
            posicao = ''.join(map(str,['a' , linha, coluna]))
            self[linha - 1].append(kwargs[posicao])
        self._verificar_matriz()
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

    def _verificar_matriz(self):
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
            resultado = round((self.repr_termos[linha - 1] - somatorio) / self[linha - 1][linha -1],3) 
            somatorio = 0
            self.result_x.insert(0, resultado)
            self._value[linha -1] = resultado
        return self.result_x

class Inferior(Matriz):

    def _verificar_matriz(self):
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
            resultado = round((self.repr_termos[linha -1] + (somatorio * -1)) /self[linha -1][linha -1],3)
            self.result_x.append(resultado) 
            somatorio = 0
        return self.result_x

class LU(Matriz):

    def _verificar_matriz(self):
        pass
    def _decompor(self):
        matriz_l = Inferior(ordem=self.ordem)
        matriz_u = Superior(ordem=self.ordem)
        lista_u = {} 
        lista_l = {}
        somatorio = 0
        pos = lambda p,i,j:"%s%i%i"%(p,i,j)
        for linha, coluna in self.todas_as_posicoes:
            if linha > coluna:
                somatorio = 0
                for k in range(1,coluna):
                    somatorio += lista_l[pos('a',linha,k)] * lista_u[pos('a',k,coluna)]
                lista_l[pos('a',linha,coluna)] = round((1./lista_u[pos('a',coluna,coluna)]) * (self[linha-1][coluna-1] - somatorio),3)
                lista_u[pos('a',linha,coluna)] = 0
            elif linha <= coluna:
                somatorio = 0
                for k in range(1,linha):
                    somatorio += (lista_l[pos('a',linha,k)] * lista_u[pos('a',k,coluna)])
                lista_u[pos('a',linha,coluna)] = round(self[linha-1][coluna-1] - somatorio,3)
                if linha == coluna:
                    lista_l[pos('a',linha,coluna)] = 1
                else:
                    lista_l[pos('a',linha,coluna)] = 0
        matriz_u.set_matriz(**lista_u)
        matriz_l.set_matriz(**lista_l)
        return matriz_u.representacao_matriz,matriz_l.representacao_matriz


    def calcular(self):
        matriz_u = Superior(ordem=self.ordem)
        matriz_l = Inferior(ordem=self.ordem)
        matriz_u.representacao_matriz = self._decompor()[0]
        matriz_l.representacao_matriz = self._decompor()[1]
        matriz_l.repr_termos = self.repr_termos
        matriz_u.repr_termos = matriz_l.calcular()
        return matriz_u.calcular()

class MatrixError(Exception):
    pass

