# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

#================ DECLARAÇÕES E ATRIBUIÇÕES INICIAIS ============================
str_nome_usuario = ''
str_senha_usuario = ''
str_mensagem      = ''
bol_senha_igual_nome = True
lista_bol_verificacao = list()

#================ PROCESSAMENTOS ================================================
while bol_senha_igual_nome:
      str_nome_usuario = input('Digite o nome do usuário: ')
      str_senha_usuario = input('Digite a senha do usuário: ')
      
      for indice, letra in enumerate(str_nome_usuario):
            if(str_nome_usuario[indice] == str_senha_usuario[indice].upper() or str_nome_usuario[indice] == str_senha_usuario[indice].lower()):
                  lista_bol_verificacao.append(True)
            else:
                  lista_bol_verificacao.append(False)
                  
      for igualdade in lista_bol_verificacao:
            if not igualdade:
                  bol_senha_igual_nome = False
                  break
            else:
                  break
            
      print('Senha igual ao nome de usuário, digite novamente.')
      print('================================')
                  
#================ SAIDAS ========================================================
