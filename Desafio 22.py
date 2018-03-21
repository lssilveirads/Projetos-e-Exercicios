nome = str(input('Digite seu nome completo: '))


print('Este é seu nome em letras mínusculas:' + nome.lower())
print('Este é seu nome em letras maiúsculas:' + nome.upper())
print('Seu nome completo tem ao todo {} letras'.format(len(nome.strip())))#Strip serve para tirar os espaços
