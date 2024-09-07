# Exercício 1
"""
Considere as seguintes atribuições nas variáveis abaixo e responda as perguntas que vem em seguida. (Caso sinta dúvida você pode usar a função type para conferir os tipos)
"""

a0 = 10
a1 = "10"
a2 = 10.0

b0 = a0 + a2
b1 = a2 + a2
b2 = 5 * a0
b3 = a0 // 2
b4 = a0 / 2

isso_eh_um_int = 10.0
isso_eh_um_float = "10"
isso_eh_uma_string = 10

###############################################
#                Perguntas
###############################################
"""
Qual o tipo das variáveis a0, a1 e a2?
"""
# Resposta
# a0 é int, a1 é str e a2 é float
"""
Qual o tipo das váriaveis b0, b1, b2, b3 e b4? 
"""
# Resposta
# b0 é int, b1 é float, b2 é int, b3 é int e b4 é float
"""
Qual o tipo das variaveis isso_eh_um_int, isso_eh_um_float e isso_eh_uma_string?
(Note que o nome da variável não influencia no seu tipo)
"""
# Resposta
# isso_eh_um_int é float, isso_eh_um_float é str e isso_eh_uma_string é int
"""
Caso existisse um código entrada_do_usuario = input(), qual seria o tipo da variável entrada_do_usuario? O que deveria ser feito caso você queira utilizar a entrada do usuário como um número inteiro?
"""
# Resposta
# Seria str, pois o input() retorna uma string. Para contornar isso, você pode converter a entrada do usuário para um número inteiro usando int(input()).
