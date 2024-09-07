# Exercício 8
"""
Escreva um programa que inicialize uma variável com o valor 5 para representar o número de milhas. Depois, converta esse valor para quilômetros e depois para metros, usando km = milhas / 0.62137 e metros = 1000 * km. Imprima o resultado na seguinte forma:

milhas
5
km
8.04672
metros
8046.72
"""

# Inicializa a variável com o valor de milhas
milhas = 5

# Converte milhas para quilômetros
km = milhas / 0.62137

# Converte quilômetros para metros
metros = 1000 * km

# Imprime os resultados no formato especificado
print("milhas")
print(milhas)
print("km")
print(f"{km:.5f}")
print("metros")
print(f"{metros:.2f}")
