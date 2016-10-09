def escreva(*args):
    print(''.join((str(arg) for arg in args)))


def pergunte(*args):
    return input(''.join((str(arg) for arg in args)) + '\n')


def converta_para_numero(numeric):
    try:
        return int(numeric)
    except ValueError:
        return float(numeric)


class Lista(object):

    def __init__(self):
        self.lista = []

    def adicione(self, valor):
        self.lista.append(valor)

    def retorne(self, indice):
        return self.lista[indice - 1]


def nova_lista():
    return Lista()
