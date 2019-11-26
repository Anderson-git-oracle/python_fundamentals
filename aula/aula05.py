# manipulando arquivos

#arq1 = open('arquivo/sherlock.txt', 'r')
#arq1 = 'arquivo/sherlock.txt'
#print(arq1.read()) # mostra conteúdo do arquivo
#print(arq1.tell())
#arq1.seek(3,2)
#arq1.close()

# with open('arquivo01.txt', 'x') as f:
#     f.write('Abrindo arquivos em python')

#with open(arq1, 'r+') as f:
#    print(f.readlines())

# def soma(x, y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)

# soma(10, 5)
# soma(2, 6)
# soma(4, 7)

# produtos = []

# def cadastraproduto(produto):
#     produtos.append(produto)

# def listarproduto():
#     for p in produtos:
#         print(p)

# produto = ""

# i = 0

# while produto != "sair":
#     produto = input('digite o produto:')
#     cadastraproduto(produto)
#     print('produto cadastrado')
#     listarproduto
#     i = i + 1
#     print(i)
#     print(produtos[0:i-1])


# def printa(*valores):
#     print(valores)

# printa('nome', 'sobrenome', 'outro')

# def printa2(**valores):
#     print(valores)

# printa2(v1='nome', v2='sobrenome', v3='outro')

# nome = 'Joao'

# def mudanome(novo_nome):
#     nome = novo_nome
#     return nome

# print(mudanome('Bruno'))

texto = 'Eu sou um cérebro, Watson. O resto é mero apêndice.'

def split_texto(text):
    return text.split(' ')

def uppertexto(text):
    return text.upper()



arquivo_novo = split_texto(texto)

print(arquivo_novo)

print(uppertexto(texto))
