import random

# Solicita ao usuário que pense em uma pergunta
input("Pense em uma pergunta e pressione Enter para obter a sua resposta...")

num = random.randint(1, 7) 

if num == 1:
    print('Sim, vá em frente')
elif num == 2:
    print('Não, fica na tua!')
elif num == 3:
    print('Minhas fontes mágicas afirmam que sim!')
elif num == 4:
    print('Com toda certeza, não!')
elif num == 5:
    print('Não sei ao certo')
elif num == 6:
    print('Tenta novamente, deu interferência no sinal mágico!')
elif num == 7:
    print('Pode ser, mas está nebuloso')
else:  
    print('Número incorreto, tente novamente')
