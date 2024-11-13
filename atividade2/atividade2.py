numeros = []
for _ in range(0,5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# variavel d a soma
soma = sum(numeros)
media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media}")
