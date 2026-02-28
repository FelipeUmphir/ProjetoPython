#Declaração de Variável
Litros = 0
Tempo = 0
Vm = 0
V = 0

#Início
Tempo = float(input('Digite o tempo da viagem:'))
Vm = float(input('Digite o valor da velocidade média do automóvel:'))
V = Vm * Tempo
Litros = V / 12
print('A quantidade de litros gastos na viagem é:', Litros)
#Fim