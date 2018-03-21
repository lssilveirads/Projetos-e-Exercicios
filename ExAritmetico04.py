#Faça um programa que leia um valor em metro
# e a exiba em centimetros e milímetros.
valor = float(input("Digite um valor:"))
n1 = valor*100
n2 = valor*1000
print("O valor convertido em centimetros é {} e em melímetros é {}".format(n1,n2))