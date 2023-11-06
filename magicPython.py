# Declara variáveis e inicializa
Grifinoria = 0
LufaLufa = 0
Corvinal = 0
Sonserina = 0

# Faz a primeira pergunta e armazena a resposta em questão1
questao1 = int(input('Você prefere 1-Alvorecer ou 2-Crepúsculo? '))

# Estrutura de Repetição para armazenamento de pontos
if questao1 == 1:
    Grifinoria += 1
    Corvinal += 1
elif questao1 == 2:
    LufaLufa += 1
    Sonserina += 1
else:
    print('Resposta Incorreta')

print('------------------------')

# Faz a segunda pergunta e armazena a resposta em questão2
questao2 = int(input('Quando eu morrer, Quero que as pessoas lembrem de mim como: 1-O bom /A boa; 2-O melhor/ A melhor; 3-O sábio/ A sábia; 4-O ousado/A ousada:  '))

# Estrutura de Repetição para armazenamento de pontos
if questao2 == 1:
    LufaLufa += 2
elif questao2 == 2:
    Sonserina += 2
elif questao2 == 3:
    Corvinal += 2
elif questao2 == 4:
    Grifinoria += 2
else:
    print('Resposta incorreta')

print('------------------------')

# Faz a segunda pergunta e armazena a resposta em questão3
questao3 = int(input(
    'Qual tipo de instrumento você gosta mais de ouvir? 1-Violino; 2-Trumpete; 3-Piano; 4-Bateria: '))

# Estrutura de Repetição para armazenamento de pontos
if questao3 == 1:
    Sonserina += 4
elif questao3 == 2:
    LufaLufa += 4
elif questao3 == 3:
    Corvinal += 4
elif questao3 == 4:
    Grifinoria += 4
else:
    print('Resposta incorreta')

print('------------------------')

# Estrutura de Repetição para Decisão da casa selecionada
if Grifinoria > Corvinal and Grifinoria > Sonserina and Grifinoria > LufaLufa:
    print('Bravura, Ousadia e Nobreza: Você é da GRIFINÓRIA 🦁!')
elif Corvinal > Grifinoria and Corvinal > Sonserina and Corvinal > LufaLufa:
    print('Inteligência, Perspicacia e Criatividade: Você é da CORVINAL 🦅 !')
elif Sonserina > Grifinoria and Sonserina > Corvinal and Sonserina > LufaLufa:
    print('Astúcia, Ambição e Engenhosidade: Você é da SONSERINA 🐍!')
elif LufaLufa > Grifinoria and LufaLufa > Corvinal and LufaLufa > Sonserina:
    print('Dedicação, paciência e Lealdade: Você é da LUFA-LUFA 🦡!')
else:
    print('Muitas dúvidas...melhor refazermos!')

print("-------------------------")

# Total de pontos atribuidos por casa
print("Total de pontos obtidos: ")
print('🦁 Grifinória: ', Grifinoria)
print('🦅 Corvinal:  ', Corvinal)
print('🐍 Sonserina:  ', Sonserina)
print('🦡 Lufa-Lufa: ', LufaLufa)
