H_t = 0
V_h = 0
Desc = 0
N_d = 0
S = 0
S_liq = 0
S_rec = 0

H_t = float(input('Digite o valor de horas trabalhadas:'))
V_h = float(input('Digite o valor por hora:'))
Desc = float(input('Digite o valor do desconto em %:'))
N_d = int(input('Digite o número de dependentes:'))
S = H_t * V_h
S_liq = S - (S * Desc / 100)
S_rec = S_liq + (N_d * 100)
print('O salário a receber é de:', S_rec)