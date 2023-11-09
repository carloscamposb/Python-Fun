
# Loop com estrutura de repetição para gerar números de 1 a 100 e substituir:
# Múltiplos de 3 por 'Fizz' ; # Múltiplos de 5 por 'Buzz' ; # Múltiplos de 3 e 5 por 'FizzBuzz' ; 
for i in range ( 1, 101):
    if i%3==0 and i%5==1:
        print('Fizz')
    elif i%3==1 and i%5==0:
        print('Buzz')
    elif i%3==0 and i%5==0:
        print('FizzBuzz')
    else:
        print(i)            