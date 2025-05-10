def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero} NÃO pertence à sequência.")