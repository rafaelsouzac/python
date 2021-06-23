# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual nÚmero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada do 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
int_valor_tabuada = 0
str_valor_digitado = ''
bol_valor_valido   = False

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================
while not bol_valor_valido:
    # ============== ENTRADA E ATRIBUIÇÃO =========================================
    str_valor_digitado = input('Digite o valor entre 1 e 10 para ver a tabuada: ')
    if str_valor_digitado.isdigit():
        int_valor_tabuada = int(str_valor_digitado)
        # ============== SAÍDA =========================================
        print(f'Tabuada do {int_valor_tabuada}'.format(int_valor_tabuada))
        for int_valor in range(1,11):
            int_multiplicacao = int_valor_tabuada * int_valor
            # ============== SAÍDA =========================================
            print(f'{int_valor_tabuada} x {int_valor} = {int_multiplicacao}')
        bol_valor_valido = True
    else:
        # ============== SAÍDA =========================================
        print('Valor digitado invalido')
