nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/altura**2
est_civil = input("""Digite seu estado civil: 
                  S-Solteiro
                  C-Casado(a)
                  D-Divorciado
                  V-Viúvo \n""").upper()

if imc<17:
    pimc = "Muito abaixo do peso ideal!"
elif imc>=17 and imc<18.5:
    pimc = "Abaixo do peso ideal"
elif imc>=18.5 and imc<25:
    pimc = "Peso normal!"
elif imc>=25 and imc<30:
    pimc = "Acima do peso ideal!"
elif imc>=30 and imc<35:
    pimc = "Obesidade I"
elif imc>=35 and imc<40:
    pimc = "Obesidade severa!"
else:
    pimc = "Obesidade mórbida :("


match est_civil:
    case 'S':
        pcivil= "Solteiro"
    case 'C':
        pcivil = "Casada"
    case 'D':
        pcivil = "Divorciado"
    case 'V':
        pcivil = "Viúvo"
    case _:
        pcivil = "Estado civil não identificado ou inserido!"

print(f"""

*****************************
*   Formulário de usuário   *
*                           *
* Nome:   {nome}              *
* Idade: {idade} anos            *                 
* IMC:   {imc:.2f}              *
* {pimc}              *
* {pcivil}                    *
*****************************
""")
