# Exercício 4
"""
Analise o seguinte programa abaixo. E faça o que é pedido nos itens:

a) Substitua os comentários em cima de cada linha por uma explicação do que aquela linha faz.
b) Note que a mensagem tem três problemas. O primeiro é que existe um hífen em 'A - Ginasta'. O segundo é que a palavra ginasta aparece com letra maiuscula. E por último, existem dois espaços entre em '... de Andrade  ganhou'. Modifique os valores da variável nome e profissão para corrigir a mensagem.
"""

# Define uma string contendo o nome e profissão
nome_e_profissao = "Rebeca Rodrigues de Andrade - Ginasta"

# Encontra a posição do hífen na string
posicao_hifen = nome_e_profissao.find("-")

# Extrai o nome da string, do início até a posição do hífen
nome = nome_e_profissao[:posicao_hifen]

# Extrai a profissão da string, da posição do hífen até o final
profissao = nome_e_profissao[posicao_hifen:]

# Adicione código modificar os valores das variáveis nome e profissao de forma a corrigir a mensagem.
nome = nome.strip()  # Remove espaços em branco extras
profissao = profissao[2:].strip().lower()  # Remove espaços, o hifen e converte para minúsculas

# Imprime a mensagem formatada
print("A", profissao, nome, "ganhou medalha de ouro no solo e prata no individual geral nas olimpíadas de Paris 2024.")