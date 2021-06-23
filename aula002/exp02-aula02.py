#Faça um Programa que leia três números e mostre o maior e o menor deles.

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
int_primeiro_numero = 0.00
int_segundo_numero  = 0.00
int_terceiro_numero = 0.00
int_maior_numero    = 0.00
int_menor_numero    = 0.00

#============== ENTRADAS E ATRIBUIÇÕES ========================
int_primeiro_numero = int(input('Diigite um numero: '))
int_segundo_numero  = int(input('Diigite um novo numero: '))
int_terceiro_numero = int(input('Diigite um outro numero: '))

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================

#--------------> BLOCO D1 MAIOR
if int_primeiro_numero > int_segundo_numero > int_terceiro_numero:
    int_maior_numero = int_primeiro_numero
    int_menor_numero = int_terceiro_numero
elif int_primeiro_numero > int_segundo_numero < int_terceiro_numero:
    int_maior_numero = int_primeiro_numero
    int_menor_numero = int_segundo_numero

#--------------> BLOCO D2 MAIOR
if int_primeiro_numero < int_segundo_numero > int_terceiro_numero:
    int_maior_numero = int_segundo_numero
    if int_primeiro_numero > int_terceiro_numero:
        int_menor_numero = int_terceiro_numero
    else:
        int_menor_numero = int_primeiro_numero

#--------------> BLOCO D3 MAIOR
if int_primeiro_numero < int_terceiro_numero and int_segundo_numero < int_terceiro_numero:
    int_maior_numero = int_terceiro_numero
    if int_primeiro_numero > int_segundo_numero:
        int_menor_numero = int_segundo_numero
    else:
        int_menor_numero = int_primeiro_numero

#============== SAÍDA =========================================
print(f'O maior número informado foi {int_maior_numero} e o menor número foi {int_menor_numero}'.format(int_maior_numero,
                                                                                                        int_menor_numero))