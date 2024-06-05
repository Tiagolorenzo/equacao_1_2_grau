'''
Crie um programa onde o usuário decide qual equação deseja calcular: equação do primeiro ou segundo grau.
'''
import math

# Equação do primeiro grau
eq_primeiro_grau = lambda a, b: -b / a

# Equação do segundo grau
eq_segundo_grau = lambda a, b, c: (
    (-b + math.sqrt(b**2 - 4*a*c)) / (2*a),
    (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
)

while True:
    print('Escolha a equação que deseja calcular: ')
    print('1. Equação do primeiro grau')
    print('2. Equação do segundo grau')
    print('3. Sair')
    escolha = input('Digite a sua escolha (1, 2 ou 3): ')

    if escolha == '1':
        a = float(input('Digite o valor de a: '))
        b = float(input('Digite o valor de b: '))
        if a == 0:
            print('a tem que ser maior que zero.')
        else:
            resultado = eq_primeiro_grau(a, b)
            print(f'A solução da equação {a}x + {b} = 0 é x = {resultado}')

    elif escolha == '2':
        a = float(input('Digite o valor de a: '))
        b = float(input('Digite o valor de b: '))
        c = float(input('Digite o valor de c: '))
        if a == 0:
            print('a tem que ser maior que zero.')
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                print('A equação não possui raízes reais.')
            elif delta == 0:
                resultado = eq_primeiro_grau(a, b)
                print(f'A solução da equação {a}x^2 + {b}x + {c} = 0 é x = {resultado}')
            else:
                resultado1, resultado2 = eq_segundo_grau(a, b, c)
                print(f'As soluções da equação {a}x^2 + {b}x + {c} = 0 são x1 = {resultado1} e x2 = {resultado2}')

    elif escolha == '3':
        print('Programa encerrado!')
        break

    else:
        print('Escolha inválida, tente outra vez!')