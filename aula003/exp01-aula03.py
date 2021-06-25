# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.

#================ DECLARAÇÕES E ATRIBUIÇÕES INICIAIS ============================
int_valor_digitado = -1
bol_valor_valido  = False
str_saida         = ''

#================ PROCESSAMENTOS ================================================
while not bol_valor_valido:
    #================ ENTRADAS DE DADOS =========================================
    int_valor_digitado = input('Digite um valor entre 0 e 10: ')
    
    #================ PROCESSAMENTOS ============================================
    if int_valor_digitado.isdigit() and (int(int_valor_digitado) > -1 and int(int_valor_digitado) < 11):
            bol_valor_valido = True
            print('====================================================')
            print(f'O valor digitado {int_valor_digitado} esta entre 0 e 10'.format(int_valor_digitado))
    else:
        #================ SAIDAS ================================================
        print('====================================================')
        print('Valor digitado invalido. Por favor digite novamente.')

#================ SAIDAS ========================================================

