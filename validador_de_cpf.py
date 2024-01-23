import re
import sys


entrada = input('CPF [460.509.858-55]: ')
# Remove os caracteres que não são um número
cpf_usuário = re.sub(
    r'[^0-9]',
    '',
    entrada
    )

entrada_e_sequencial = entrada == entrada[0]*len(entrada)

if entrada_e_sequencial:
    print('CPF inválido')
    sys.exit()

# Cálculo do primeiro digito do CPF
nove_num_cpf = cpf_usuário[:9]
regressiva1 = 10
multiplic_digito1 = 0

for contagem1 in nove_num_cpf:
    multiplic_digito1 += int(contagem1) * regressiva1
    regressiva1 -= 1

primeiro_digito_cpf = (multiplic_digito1 * 10) % 11

if primeiro_digito_cpf > 9:
    primeiro_digito_cpf = 0
else:
    pass

# Cálculo do segundo digito do CPF
dez_num_cpf = nove_num_cpf + str(primeiro_digito_cpf)
regressiva2 = 11
multiplic_digito2 = 0

for contagem2 in dez_num_cpf:
    multiplic_digito2 += int(contagem2) * regressiva2
    regressiva2 -= 1

segundo_digito_cpf = (multiplic_digito2 * 10) % 11

if segundo_digito_cpf > 9:
    segundo_digito_cpf = 0
else:
    pass

# Verificando se o CPF é válido
cpf_gerado_pelo_calculo = f'{nove_num_cpf}{primeiro_digito_cpf}{segundo_digito_cpf}'

if cpf_usuário == cpf_gerado_pelo_calculo:
    print(f'{cpf_usuário} é válido')
else:
    print(f'CPF Inválido')