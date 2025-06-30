# AmBank - Sistema Bancário em Python com POO

AmBank é um projeto simples desenvolvido com Python que simula um sistema bancário utilizando os conceitos de Programação Orientada a Objetos (POO). O objetivo é praticar e demonstrar o uso de classes, objetos, encapsulamento, herança e métodos.

## Funcionalidades

- Criação de contas bancárias
- Depósito de valores
- Saque de valores
- Transferência entre contas
- Herança de classe para Conta Corrente com limite

## Conceitos de POO aplicados

- **Classe**: moldes para criação de contas (`ContaBancaria`, `ContaCorrente`)
- **Objeto**: instâncias das contas criadas
- **Encapsulamento**: o saldo é protegido por atributo privado (`__saldo`)
- **Métodos**: ações como `depositar`, `sacar`, `ver_saldo` e `transferir`
- **Herança**: `ContaCorrente` herda da classe `ContaBancaria` e adiciona um limite

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/am-bank-poo.git
cd am-bank-poo
```

Execute o código em Python 3:
```bash
python3 ambank.py
```

Exemplo de uso no terminal interativo (ou script):
```bash
conta1 = ContaBancaria("Neto", 1000)
conta2 = ContaBancaria("Dhiego", 500)

conta1.depositar(300)
conta1.sacar(100)
conta1.transferir(200, conta2)

conta1.ver_saldo()
conta2.ver_saldo()
```

Estrutura

    ContaBancaria: classe principal com operações básicas

    ContaCorrente: herda ContaBancaria e permite saque com limite

Requisitos

    Python 3.6 ou superior
