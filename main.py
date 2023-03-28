import questoes

#Lista de questões Workshop
questao = int(input('1 - 2 - 3\nQual exercicio você deseja fazer: '))

#exercicio 1
if questao == 1:
    questoes.exercicio1()

#exercicio 2
elif questao == 2:
    questoes.exercicio2()

#exercicio 3
elif questao == 3:
    questoes.exercicio3()

else:
    print('Opção invalida')
