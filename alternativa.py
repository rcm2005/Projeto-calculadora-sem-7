 #Substitui todos os dígitos 7 por 0 em um número.
resultado = 0       
multi = 1                
while x > 0:
        digito = x % 10
        if digito == 7:
            digito = 0       
        resultado += digito * multi #resultado
        multi = 10 * multi
        x //= 10 # x = x//10
return resultado
while True:
    print("__Team: Pontes__")
    print("-    checkpoint 1 with python     -")
    print("__")
    print("\nuse numeros entre 0 a 99")
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    if n1 < 0 or n1 > 99 or n2 < 0 or n2 > 99: #num pertencente 0 a 99
        print("\n Erro:")
        print("\n Os numeros devem estar entre 0 a 99")
        print("---Tente novamente!---")
    else:
        n1 = troca_sete(n1)
        n2 = troca_sete(n2)
        soma = n1 + n2
        soma = troca_sete(soma)

        print(f"Soma dos numeros: {soma}")
        break
