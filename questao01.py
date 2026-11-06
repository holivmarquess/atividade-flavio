lista = []
for i in range(1,6):
    numero = int(input(f"{i} - Digite um número inteiro: "))
    lista.append(numero)

media = sum(lista)/5


print(f"Seus números são: {lista}")
print(f"O maior valor da sua lista é: {max(lista)}")
print(f"A soma dos valoes nessa lista é: {sum(lista)}")
print(f"A média total da sua lista é: {media} ")

lista.sort()

print(f"E sua lista em roll fica: {lista}")










