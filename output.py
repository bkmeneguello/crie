from crie.stdlib import *
escreva('olá')
vamos_brincar = pergunte('vamos brincar?')
if vamos_brincar == 'sim':
    nome = pergunte('qual o seu nome?')
    idade = pergunte('oi ', nome, ' qual a sua idade?')
    idade = converta_para_numero(idade)
    tipo = pergunte('você é menina ou menino')
    if tipo == 'menino':
        escreva('O ', nome, ' é um ', tipo)
    elif tipo == 'menina':
        escreva('A ', nome, ' é uma ', tipo)
    while idade > 0:
        escreva(idade)
        idade = idade - 1
elif vamos_brincar == 'não':
    escreva('tá bom, tchau!')
else:
    escreva('não entendi.')


def conte(numero):
    numero_atual = 0
    while numero_atual <= numero:
        escreva(numero_atual)
        numero_atual = numero_atual + 1

conte(10)

lista = nova_lista()
lista.adicione('teste')
registro = lista.retorne(0)
