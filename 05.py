#Declaração de Variável 
A = 0
B = 0
C = 0
R1 = 0
R2 = 0
D = 0

#Início
A = int(input('Digite o valor do coeficiente a:'))
B = int(input('Digite o valor do coeficiente b:'))
C = int(input('Digite o valor do coeficiente c:'))
D = (B ** 2) - (4 * A * C)
R1 = (-B + D ** 0.5) / 2 * A
R2 = (-B - D ** 0.5) / 2 * A
print('O valor das raízes é:', R1, "e", R2)
#Fim