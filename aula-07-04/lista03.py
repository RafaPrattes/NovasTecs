#Lista sobre coleções em python 

#q2
#a chave de um dicionario esta sempre em tuplas
# palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

# anagramas = {}

# for palavra in palavras:
#     chave = tuple(sorted(palavra))
#     print(chave)
#     if chave in anagramas:
#         anagramas[chave].append(palavra)
#     else:
#         anagramas[sorted(palavras)] = [palavra]
# print(anagramas)

#q8

expressao = input('Digite a sequencia de parentesis: ')

pilha = []

for char in expressao:
    if char == '(':
        pilha.append(')')
    else:
        pilha.pop()

        if len(pilha) == 0:
            print("Correta")
            
