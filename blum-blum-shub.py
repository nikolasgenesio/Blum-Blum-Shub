import random
from sympy import isprime

# Algoritmo Blum Blum Shub para geração de números pseudo-aleatórios
def blum_blum_shub(bits=10):
    # Dois números primos grandes p e q tais que ambos congruentes a 3 (mod 4)
    p = numero_primo()
    q = numero_primo()

    # Calculando n = p * q
    n = p * q

    # Escolhendo x0 como um número inteiro aleatório entre 1 e n-1
    x = random.randint(1, n-1)

    # Gerando os bits
    bitstream = ""
    for _ in range(bits):
        # Calculando x = (x^2) mod n
        x = (x * x) % n
        
        # Bit menos significativo de x
        bitstream += str(x % 2)
    
    return bitstream

# Função para obter um número primo grande congruente com 3 módulo 4
def numero_primo():
    while True:
        # Gerando um número aleatório maior que 10.000
        num = random.randint(10000, 100000)
        
        # Verificando se o número é primo e congruente com 3 módulo 4
        if isprime(num) and num % 4 == 3:
            return num

# Fluxo de bits usando o algoritmo Blum Blum Shub
bitstream = blum_blum_shub(bits=10)

# Impressão na tela
print("Bits:", bitstream)
