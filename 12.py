#Declaração de Variável
Ano_nasc = 0
Ano_atual = 0
Idade = 0
Idade_fut = 0

#Início
Ano_nasc = int(input('Digite o ano de nascimento:'))
Ano_atual = int(input('Digite o ano vigente:'))
Idade = Ano_atual - Ano_nasc
Idade_fut = Idade + 17
print('A idade atual é:', Idade)
print('A idade daqui 17 anos é:', Idade_fut)
#Fim