##classes é um molde, que define o que um objeto(atributo) e fazer (metodos)



#objetos é uma instancia da classe 
# é como criar carros diferentes a partir do mesmo molde


# conceitos usados
#classe: ContaBancaria
#objeto: conta dos clientes
#encapsulamento: proteger o saldo
#metodos: Sacar, Depositar, transferir
#herança(depois)ContaCorrente e ContaPoupança


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo #atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"depósito de R${valor} realizado para {self.titular}")
        else:
            print("valor invalido para depósito")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"saque de R${valor} realizado por {self.titular}")
        else:
            print("valor inválido")

    def ver_saldo(self):
        print(f"Saldo de {self.titular}:R${self.__saldo}")

    def transferir(self, valor, destino):
        if valor <= self.__saldo:
            self.__saldo -= valor
            destino.depositar(valor)
            print(f"Transferência de R${valor} para {destino.titular} realizada.")
        else:
            print("Saldo insuficiente para transferência.")

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self._ContaBancaria__saldo + self.limite:
            self._ContaBancaria__saldo -= valor
            print(f"Saque com limite: R${valor} realizado.")
        else:
            print("Limite excedido.")


        
conta1 = ContaBancaria("Neto", 1000)
conta2 = ContaBancaria("Dhiego", 500)

conta1.ver_saldo()
conta1.depositar(500)
conta1.sacar(200)
conta1.ver_saldo()
conta1.transferir(300, conta2)

conta2.ver_saldo()
conta2.transferir(200, conta1)
conta1.ver_saldo()
