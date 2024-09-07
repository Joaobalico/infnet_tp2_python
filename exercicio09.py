# Exercício 9

"""
Abaixo são apresentadas algumas frases da forma
  Se [sentenca0] então [sentenca1] 

Para cada uma dessas frases transforme elas em variáveis booleanas no python e mostra um exemplo em que a [sentenca1] é verdadeira e outra que ela é falsa. A primeira frase está resolvida como exemplo.

"""

# Exemplo
print("Se é fim de semana e meus amigos estão disponíveis então eu vou a praia")

# Verdadeira
e_fim_de_semana = True
amigos_disponiveis = True
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia = ", vou_a_praia)

# Falsa
e_fim_de_semana = True
amigos_disponiveis = False
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia = ", vou_a_praia)

# Item a
print("\nSe eu estudar e fazer os exercícios então eu passo na prova")

# Verdadeira
estudei = True
fiz_exercicios = True
passo_na_prova = estudei and fiz_exercicios
print("Verdadeira - passo_na_prova =", passo_na_prova)

# Falsa
estudei = True
fiz_exercicios = False
passo_na_prova = estudei and fiz_exercicios
print("Falsa - passo_na_prova =", passo_na_prova)

# Item b
print("\nSe eu tenho um carro ou tenho uma bicicleta então eu posso viajar")

# Verdadeira
tenho_carro = False
tenho_bicicleta = True
posso_viajar = tenho_carro or tenho_bicicleta
print("Verdadeira - posso_viajar =", posso_viajar)

# Falsa
tenho_carro = False
tenho_bicicleta = False
posso_viajar = tenho_carro or tenho_bicicleta
print("Falsa - posso_viajar =", posso_viajar)

# Item c
print("\nSe estou cansado ou é tarde então eu vou dormir")

# Verdadeira
estou_cansado = True
e_tarde = False
vou_dormir = estou_cansado or e_tarde
print("Verdadeira - vou_dormir =", vou_dormir)

# Falsa
estou_cansado = False
e_tarde = False
vou_dormir = estou_cansado or e_tarde
print("Falsa - vou_dormir =", vou_dormir)

# Item d
print("\nSe eu tenho dinheiro e tempo então eu vou viajar")

# Verdadeira
tenho_dinheiro = True
tenho_tempo = True
vou_viajar = tenho_dinheiro and tenho_tempo
print("Verdadeira - vou_viajar =", vou_viajar)

# Falsa
tenho_dinheiro = True
tenho_tempo = False
vou_viajar = tenho_dinheiro and tenho_tempo
print("Falsa - vou_viajar =", vou_viajar)

