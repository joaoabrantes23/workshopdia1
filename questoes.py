#criando função exercicio1
def exercicio1():
    def maior(num1, num2):
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        return maior

    num1 = int(input("Digite um numero: "))
    num2 = int(input('Digite outro numero: '))

    print(maior(num1, num2))

#criando função exercicio2
def exercicio2():
    def multiplo(num1, num2):
        if num1 % num2 == 0:
            return True
        elif num1 or num2 == 0:
            return False
        else:
            return False

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    print(multiplo(num1, num2))

#criando uma função exercicio3
def exercicio3():
    def quadrado(lado):
        area = lado ** 2
        return area

    lado = int(input("Digite o lado do quadrado: "))

    print('A área do quadrado é: ', quadrado(lado))