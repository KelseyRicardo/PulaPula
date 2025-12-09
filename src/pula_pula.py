from src.crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.fila = []
        self.nomes = []
        self.criancasPulando = []
        self.contas = dict()
        self.caixa = 0

    def getFilaDeEspera(self):
        return self.fila

    def getCriancasPulando(self):
        return self.criancasPulando

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        if nome in self.contas.keys():
            return self.contas[nome]

    def entrarNaFila(self, crianca: Crianca):
        if crianca.nome in self.nomes or crianca.nome in self.criancasPulando:
            return False
        self.nomes.append(crianca.nome)
        self.fila.append(crianca)
        return True

    def entrar(self):
        if len(self.criancasPulando) >= self.limiteMax or len(self.fila) == 0:
            return False

        nomes = self.fila[0].getNome()
        if nomes not in self.contas.keys():
            self.contas[nomes] = 0
        self.contas[nomes] += 2.5

        self.criancasPulando.append(self.fila[0])
        self.fila.pop(0)

        return True

    def sair(self):
        if len(self.criancasPulando)<=0:
            return False
        self.fila.append(self.criancasPulando[0])
        self.criancasPulando.pop(self.limiteMax-1)
        return True

    def papaiChegou(self, nome):
        for i in self.fila:
            if i.getNome() == nome:
                self.fila.remove(i)
                if nome in self.contas.keys():
                    self.caixa += self.contas[nome]
                return True
        for i in self.criancasPulando:
            if i.getNome() == nome:
                self.caixa += self.contas[nome]
                self.criancasPulando.remove(i)
                return True


        return False

    def fechar(self):
        for i in self.fila:
            self.papaiChegou(i.getNome())
        for i in self.criancasPulando:
            self.papaiChegou(i.getNome())
        self.fila = []
        self.criancasPulando = []
        self.contas = dict()
        return -1
