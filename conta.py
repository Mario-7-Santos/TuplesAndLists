# se você tem um método que você quer definir na sua classe mãe
# e que todo mundo seja forçado a implementar,
#  coloque um @abstractmethod nela,
#  defina ela como uma classe abstrata através da meta classe ABCmeta.

from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "Codigo {} Saldo {}".format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.deposita(1000)


conta17 = ContaPoupanca(17)
conta17.deposita(1000)


contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)
