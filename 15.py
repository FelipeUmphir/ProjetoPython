#Declaração de Variáveis
CatA = 0
CatB = 0
Hip = 0

#Início
CatA = int(input('Digite o valor do cateto A:'))
CatB = int(input('Digite o valor do cateto B:'))
Hip = ((CatA ** 2) + (CatB ** 2)) ** 0.5
print('O valor da hipotenusa é:', Hip)
#Fim