# Exercício 14
"""
Alice e Bob são dois amigos e querem se comunicar através de mensagens escritas de maneira que outras pessoas que eventualmente peguem suas mensagens não consigam decifrar. Assim, eles criam uma criptografia com o seguinte algoritmo:

1) Escrever a mensagem original de trás para frente.

Por exemplo, a mensagem "Olá Alice." seria transformada em: ".ecilA álO"
Escreva um código com comentários explicando para desencriptar a mensagem definida na variável mensagem_encriptada.
"""

mensagem_encriptada = ".ogidóc osson o rarbeuq airiugesnoc nohtyp serodamargorp sod rohlem o meN .odnacinumoc son somatse omoc árebas méugnin aifargotpirc asse moc euq azetrec ohneT !boB álO"

# Desencriptar a mensagem
mensagem_desencriptada = mensagem_encriptada[::-1]

# Imprimir a mensagem desencriptada
print("Mensagem desencriptada:")
print(mensagem_desencriptada)