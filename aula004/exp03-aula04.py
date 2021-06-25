#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lst_flt_numero = [0,0,0,0,0,0,0,0,0,0]
int_controle = 0
str_entrada_usuario = ''

while int_controle < len(lst_flt_numero):
    str_entrada_usuario = input('Digite um número com 2 casas decimais, utilize o ponto como separador: ')
    if str_entrada_usuario.count('.') > 1 or str_entrada_usuario.count('.') == 0:
        print('Valor digitado invalido, tente novamente')
        print('=================================')
    elif not str_entrada_usuario[(len(str_entrada_usuario) - (str_entrada_usuario.find('.')+1))*-1:].isdigit() and not str_entrada_usuario[0:str_entrada_usuario.find('.')].isdigit():             
        print('Valor digitado invalido, tente novamente')
        print('=================================')
    else:
        lst_flt_numero[int_controle] = float(str_entrada_usuario)
        int_controle += 1

for _ in lst_flt_numero:
    print(lst_flt_numero[int_controle])
    int_controle -= 1
