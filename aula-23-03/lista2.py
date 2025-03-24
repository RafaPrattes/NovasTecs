#Q1:  Crie um programa que some todos os números pares entre 1 e N , onde N é fornecido pelo
#usuário

# N = input(int('Insira um numero: '))
# soma = 0

# for i in range(1, N, 2):

n = int(input('Digite um numero: '))

soma = 0

for par in range(0, n+1, 2):
    soma+=par
print(f'A soma dos pares de 1 até {n} é {soma}')
