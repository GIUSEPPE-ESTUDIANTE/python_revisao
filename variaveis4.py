alimentos = ["Maçã","Arroz","Feijão"]
categoria = ("Grãos","Frutas","Legumes")
pessoa = {"Nome":"Paula","Idade":"38","Altura":"1.65"}

print(alimentos)
print(type(alimentos))
print(len(alimentos))
#  adicionar mais um alimento
alimentos.append("Mararrão")
print(alimentos)
print(len(alimentos))

print(categoria)
print(type(categoria))
print(len(categoria))

print(pessoa)
print(type(pessoa))
print(len(pessoa))
# Adicionar um item a pessoa
# adicionar uma nova chave como seu respectivo valor
# esta sendo adicionado a chave email com o valor 
# email da pessoa
pessoa["email"]="Paula@gmail.com"
print(pessoa)
print(len(pessoa))