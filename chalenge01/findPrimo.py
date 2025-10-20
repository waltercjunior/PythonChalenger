# Escrever função encontrar fatores primos que compõe um número
# Recebe um número inteiro positivo n
# Retorna uma lista com os fatores primos de n
# O racional para encontrar os números primos para encontar o valor deve ser:
# Recebe 630 como entrada
# Retorna a lista [2, 3, 3, 5, 7] pois 2 * 3 * 3 * 5 * 7 = 630
# Outro exemplo:
# recebe 13 como entrada
# deve retornar 13, pois é número primo

#exemplo de uso:
# recebe 60 como entrada
# divide 60 / 2 = 30   lista 
# divide 30 / 2 = 15  lista [2, 2]
# divide 15 / 3 = 5   lista [2, 2, 3]
# divide 5 / 5 = 1    lista [2, 2, 3, 5]

import sys


def encontrar_fatores_primos(n):
    fatores = []
    divisor = 2

    if type(n) == int and n > 0:
        while n > 1:
            while n % divisor == 0:
                fatores.append(divisor)
                n //= divisor
            divisor += 1
        
        return fatores
    else:
        
        return "Valor inválido"


print(encontrar_fatores_primos(int(sys.argv[1])))