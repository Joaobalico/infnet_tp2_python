# Exercício 6

""" Abaixo é apresentada a variável palavra. Com relação ao valor da variável palavra responda:

a) Quantas letras possui essa palavra?

b) Quantas vezes a letra 'o' aparece nessa palavra?

c) Qual a posição da letra v nessa palavra?

d) Escreva essa palavra de trás para frente.

e) Divida essa palavra em duas com a mesma quantidade de caracteres.

Você deve utilizar código python para ajudar a responder essas perguntas.
"""

palavra = "pneumoultramicroscopicossilicovulcanoconiotico"

# Item a
print("a) Número de letras na palavra:", len(palavra))

# Item b
print("b) Número de vezes que a letra 'o' aparece:", palavra.count('o'))

# Item c
print("c) Posição da letra 'v' na palavra:", palavra.index('v'))

# Item d
print("d) Palavra de trás para frente:", palavra[::-1])

# Item e
meio = len(palavra) // 2
primeira_metade = palavra[:meio]
segunda_metade = palavra[meio:]
print("e) Palavra dividida em duas partes:")
print("   Primeira metade:", primeira_metade, "(", len(primeira_metade), "letras)")
print("   Segunda metade:", segunda_metade, "(", len(segunda_metade), "letras)")
