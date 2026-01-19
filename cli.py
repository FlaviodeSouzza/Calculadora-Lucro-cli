"""
Calculadora de Lucro Diario"""

# Mensagem de boas-vindas
print('Olá! Vamos calcular seu resultado diário')

# Criação, captação e validação das variaveis para o calculo.

# A esrutura de repetição junto do comando 'try' testa o tipo primitivo
#  do valor inserido pelo usuário.
while True:
    try:
        Rt = float(input('Qual o valor total de ENTRADAS no dia de hoje? '))
        break
# Se o valor inserido for diferente de float, o sistema denuncia o erro através do 'except'.
# O laço de repetição atua enquanto o valor inserido não corresponda ao tipo primitivo indicado.
    except ValueError:
        print('Valor inválido!')

while True:
    try:
        Ct = float(input('Qual o valor total de SAÍDAS no dia de hoje? '))
        break
    except ValueError:
        print('Valor inválido!')

# Apresentação do resultado final
print(f'Seu resultado final no dia de hoje foi de R$ {Rt-Ct:.2f} ')
