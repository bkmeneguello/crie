def escreva(*args):
    print(''.join((str(arg) for arg in args)))


def pergunte(*args):
    return input(''.join((str(arg) for arg in args)) + '\n')


def converta_para_numero(numeric):
    try:
        return int(numeric)
    except ValueError:
        return float(numeric)
