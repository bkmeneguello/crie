nome = 'joão'

sobrenome = 'da silva'
menina = True
idade = input('qual a sua idade?')
print(idade)
criança = idade < 10
vamos_brincar = criança and menina
resposta = input('vamos brincar?')
if resposta == 'sim':
    print('oi!')
elif resposta == 'não':
    print('tchau!')
else:
    print('não entendi')

while resposta != 'não':
    resposta = input('vamos brincar?')
