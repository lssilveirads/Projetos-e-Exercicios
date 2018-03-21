velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocida que é de 80KM/H')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de de R${:.2f}!'.format(multa))
else:
    print('ÓTIMO! Você está dentro do limite de velocidade')
print('Tenha um bom dia! Dirija com segurança!')
