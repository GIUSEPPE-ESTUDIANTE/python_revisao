numeros = []
for _ in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media}")
