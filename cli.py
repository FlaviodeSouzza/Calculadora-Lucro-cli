"""
Calculadora de Lucro Diario"""

# Mensagem de boas-vindas
print('Olá! Vamos calcular seu resultado diário')

# Criação e captação das variaveis para o calculo.
Rt = float(input('Qual o valor total de ENTRADAS no dia de hoje? '))
Ct = float(input('Qual o valor total de SAÍDAS no dia de hoje? '))

# Apresentação do resultado final
print(f'Seu resultado final no dia de hoje foi de R$ {Rt-Ct:.2f} ')
