# #sintaxe while e ->continue<- pula a interação
# i= 0
# while(i<=25):
#     if (i == 15):
#         i+=1
#         continue
#     print(i)
#     i+=1


# #sintaxe do for
    
# for materia in('alg', 'novas', 'poo'):
#     print(f"materias[{i}] = {materia}")
#     i += 1
# #enumerate é uma classe 
# for i, materia in enumerate(('alg', 'novas', 'poo')):
#         print(f"materias[{i}] = {materia}")

# for i in range(21):#range é uma classeque gera um objeto e tb imprime a parada da posicão q vc deseja
#      print(i)
# for i in range(11):
#      print(i, end=" ")

#      for i in range(1, 31, 2):
#           print(i, end=' ')

#uma lista, por isso esta dentro de colchetes
lista = [e**2 for e in range(0,11)]
print(lista)