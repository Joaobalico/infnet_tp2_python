# Exercício 11
"""
Dado o texto na variável mensagem, faça um programa que conta a porcentagem de vogais em relação a todos os caracteres da string (espaços e pontuações devem ser contabilizado na porcentagem). Seu programa deve ter comentários. (Cuidado com as vogais maiúsculas)"""

mensagem = "A importancia da persistencia no aprendizado de programacao nao pode ser subestimada. Assim como em qualquer outra habilidade, a pratica constante e a dedicacao sao fundamentais para alcançar a proficiencia. Inicialmente, a complexidade de certas linguagens e conceitos pode parecer desafiadora, mas com o tempo e a experiencia, o aprendizado se torna mais intuitivo e gratificante."

# Definindo as vogais
vogal_a = "a"
vogal_e = "e"
vogal_i = "i"
vogal_o = "o"
vogal_u = "u"

# Transforme a mensagem em minúsculas
mensagem = mensagem.lower()

# Contando o número total de caracteres na mensagem
total_caracteres = len(mensagem)

# Contando o número de vogais na mensagem
total_vogais = mensagem.count(vogal_a) + mensagem.count(vogal_e) +\
mensagem.count(vogal_i) + mensagem.count(vogal_o) + mensagem.count(vogal_u)

# Calculando a porcentagem de vogais
porcentagem_vogais = (total_vogais / total_caracteres) * 100

# Exibindo o resultado
print(f"A porcentagem de vogais na mensagem é: {porcentagem_vogais:.2f}%")