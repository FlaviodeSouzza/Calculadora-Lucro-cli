"""
Calculadora de Lucro Diario"""

# Mensagem de boas-vindas
print('\nOlá! Vamos calcular seu resultado diário.')
print('----' * 15)


def solicitar_valor(mensagem):
    """ Validação das variaveis de calculo"""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0 :
                print('Digite um valor maior ou igual a zero.\n')
                continue
            return valor
        except ValueError:
            print('Valor inválido!')

#A esrutura de repetição junto do comando 'try' testa o tipo primitivo
#do valor inserido pelo usuário.
#Se o valor inserido for diferente de float, o sistema denuncia o erro através do 'except'.
#O laço de repetição atua enquanto o valor inserido não corresponda ao tipo primitivo indicado.

Rt = solicitar_valor('\nQual o valor total de \033[34mENTRADAS\033[0m no dia de hoje? R$ ')
Ct = solicitar_valor('\nQual o valor total de \033[31mSAÍDAS\033[0m no dia de hoje? R$ ')
lucro = Rt - Ct
# Apresentação do resultado final
# Se o saldo final for positivo a mensagem aparece em azul
# Se o saldo final for negativo a mensagem aparece em vermelho

if lucro >= 0:
    print(f'\n\033[34mSeu resultado final no dia de hoje foi de R$ {lucro:.2f}!\033[0m\n')
else:
    print(f'\n\033[31mSeu resultado final no dia de hoje foi de R$ {lucro:.2f}!\033[0m\n')
