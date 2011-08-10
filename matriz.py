class Matriz(object):


    def __init__(self, ordem):
        self.ordem = ordem
        self.representacao_matriz = [[] for lista_matriz in range(1 , ordem + 1)]
        self.repr_termos = []
        self.result_x = []
        self._value = [None, None, None]

    def set_matriz(self, **kwargs):
        """ O valor sera vinculada a uma chave em um dicionario da seguinte maneira:
                    a[linha][coluna]=valor, (a11=1, a12=3..)
        """
        for linha in range(1, self.ordem + 1):
            for coluna in range(1, self.ordem +1):
                posicao = ''.join(map(str,['a', linha, coluna]))
                self.representacao_matriz[linha - 1].append(kwargs[posicao])
        return self.representacao_matriz

    def termo_independente(self, **kwargs):
        """ O valor sera vinculada a uma chave em um dicionario da seguinte maneira:
                    b[linha]=valor, (b1=1, b2=3..)
        """
        for coluna in range(1, self.ordem +1):
            posicao = ''.join(map(str,['b', coluna]))
            self.repr_termos.append(kwargs[posicao])
        return self.repr_termos

class Superior(Matriz):

    def calcular(self):
        somatorio = 0
        for linha in range(self.ordem , 0 , -1):
            for coluna in range(self.ordem, 0, -1):
                if linha >= coluna:
                    somatorio +=0
                else:
                    somatorio += self.representacao_matriz[linha -1 ][coluna -1] * self._value[coluna -1]
            resultado = (self.repr_termos[linha - 1] - somatorio) / self.representacao_matriz[linha - 1][linha -1] 
            somatorio = 0
            self.result_x.insert(0, resultado)
            self._value[linha -1] = resultado
        return self.result_x

class Inferior(Matriz):

    def calcular(self):
        somatorio = 0
        for linha in range(1, self.ordem + 1):
            for coluna in range(1, self.ordem + 1):
                if coluna >= linha:
                    somatorio +=0
                else:
                    somatorio += self.representacao_matriz[linha-1][coluna-1] * self.result_x[coluna - 1]
            resultado = (self.repr_termos[linha -1] + somatorio) /self.representacao_matriz[linha -1][linha -1]
            self.result_x.append(resultado) 
            somatorio = 0
        return self.result_x

