# Exercício 3
""" Escreva um programa que pede para o usuário entrar uma certa quantidade de minutos. O programa deve fazer a conversão dessa quantidade em minutos para o formato hora:minuto. Por exemplo, caso o usuário passe o valor de 80 o programa deve mostrar paro o usuário que isso é equivalente a 1h20m. O seu código deve conter comentários para explicar o que está fazendo nas principais linhas
"""

# Escreva seu código aqui
# guardando input do usuario
minutos_totais = int(input("Digite a quantidade de minutos: "))

# Calcula o número de horas usando divisão inteira
horas = minutos_totais // 60

# Calcula o número de minutos restantes
minutos = minutos_totais % 60

# Resultado no formato hora:minuto
print(f"{horas}h{minutos}m")