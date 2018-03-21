#Faça um programa que leia um numero inteiro e mostre
#o seu sucessor e o seu antecessor.
inteiro = int(input("Digite um número inteiro: "))
n1 = inteiro + 1
n2 = inteiro - 1
print("O sucessor de {} é {} . O antecessor de {} é {}".format(inteiro,n1,inteiro,n2))