meu_dicionario = {}

quantidade = int(input("Quanto pares chaves-valor você quer adcionar? "))

for i in range(quantidade): 
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    meu_dicionario[chave] = valor

print("Dicionario resultante: ", meu_dicionario)