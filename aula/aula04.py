
#/usr/bin/python3
#
#while
#x = 1
#while x <= 10:
#    print(f"número: {x}")
#    x += 1
#print('O while acabou!')
#a = 500
#while a > 10:
#    print(a)
#    a -= 10
#while adicionando valores em uma lista
#x = 1
#lista = []
#while x < 1000:
#    lista.append(x)
#    x += 1
#print(lista)
#for
#l = [1, 2,3, 4, 5, 6, 7, 8, 9]
#for var in l:
#    print(var)
#frutas = ['abacaxi', 'banana', 'pera', 'maca', 'ameixa']
#for num,fruta in enumerate(frutas):
#    print(num ,fruta)
#for item in range(10, 2, -1):
#    print(item)
#cont = 0
#while cont < 10:
#    print(f'vezes de execução {cont + 1}')
#  
#    if cont == 2:
#        print('bloco de condição que interrompe o loop')
#        break
#    cont += 1
#  
#t = 0
#while t < 10:
#    print(t)
#    if t == 5:
#        continue
#    t += 1
#  
##erros e exceções
#try:
#    if 'mariana' == nome:
#        print('nome correto')
#    else:
#        print('nome errado')
#except Exception as e:
#    print(e)
#finally:
#    nome = 'mariana'
#    print(nome)
#try:
#    x = int(input('digite o primeiro numero: '))
#    y = int(input('digite o segundo numero: '))
#    print(x + y)
#except ValueError as v:
#    print('esse é um erro', v)
#while True:
#    try:
#        idade = int(input('Digite sua idade: '))
#        if idade < 16:
#            print('Você não pode comprar bebida alcolica e nem tirar titulo de eleitor ')
#            break
#        else:
#            if idade >= 16 and idade < 18:
#                print('Você pode ter titulo de eleitor')
#                break
#            else:
#                print('Você pode  comprar bebida e ter titulo de eleitor')
#                break
#            break
#      
#  
#    except Exception as e:
#        print('Isso não é um numero', e)
#        continue
##Raise Exeception
#hile True:
#   try:
#       login = input('Digite o login: ')
#
#       if login.lower() == 'bryan':
#           raise NameError('Bryan está banido! ')
#       else:
#           print(f'Bem vindo {login}, acesso permitido! ')
#           break
#   except NameError as e:
#       print(e)
#       continue

# try:
#     login = input('Digite seu login:')
#     if login == 'Caio':
#         raise NameError('Usuario banido!')
#     else:
#         print(f'Bem vindo(a) {login}!')
# except NameError as n:
#     print(n)

# finally:
#     print('finally!!!')


 