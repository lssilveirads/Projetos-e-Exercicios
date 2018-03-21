from math import sqrt
# import math "Para importar toda a biblioteca
num = int(input("Digite um número: "))
raiz = sqrt(num) #math.sqrt para causa usa toda a biblioteca do import.math
print("A raiz quadrade de {} é {:.2f} ".format(num, raiz)) # para arredondar a raiz quadrada para cima se usa. Para baixo
                                                                                 # math.ceil(raiz)       math.floor(raiz)
