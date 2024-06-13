p=float(input('Digite seu peso em kg:'))
h=float(input('Digite sua altura em m:'))

s=(p/(h*h))

print('Seu IMC é:', s)
print('')

if s <= 18.5:
    print('Abaixo do peso')
    print('Busque uma dieta de superávit calórico para ganho de massa')
elif s <= 24.9:
    print('Peso ideal')
    print('Parabéns!')
elif s <= 29.9:
    print('Levemente acima do peso:')
    print('Busque uma dieta de déficit calórico para perda de gordura')
elif s <= 34.9:
    print('Obesidade grau 1')
    print('Procure acompanhamento médico')
elif s <= 39.9:
    print('Obesidade grau 2')
    print('Procure acompanhamento médico')
else:
    print('Obesidade mórbida')
    print('Procure acompanhamento médico com urgência')