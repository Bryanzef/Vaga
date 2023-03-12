numero = int(input("Digite um número: "))

# Inicializa as variáveis para o primeiro e o segundo valores da sequência
fibonacci_anterior = 0
fibonacci_atual = 1

# Verifica se o número informado é igual a um dos primeiros dois valores da sequência
if numero == 0 or numero == 1:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    # Realiza o cálculo da sequência até que o próximo valor seja maior que o número informado
    while fibonacci_atual < numero:
        fibonacci_proximo = fibonacci_anterior + fibonacci_atual
        fibonacci_anterior = fibonacci_atual
        fibonacci_atual = fibonacci_proximo
    
    # Verifica se o último valor calculado é igual ao número informado
    if fibonacci_atual == numero:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
