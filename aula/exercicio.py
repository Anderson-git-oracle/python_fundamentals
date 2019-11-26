#!/usr/bin/python3

#Faça um programa que imprima o nome do seu time

# print('Flamengo')

#Faça um programa que peça um número e imprima esse número

# v1 = float(input('Digite um número:'))

# # print(v1)

# linguagem = 'python'

# if linguagem == 'python':
#     print('A linguagem é python')
# else:
#     print('Não é python')



# v1 = input('digite M ou F para o sexo:')

# if v1 == 'F':
#     print('Feminino')
# else:
#     print('Masculino')

# sexo = str(input('digite o sexo:'))
# sexo = sexo.capitalize()

# if sexo == 'F':
#     print('Feminino')
# elif sexo == 'M':
#     print('Masculino')
# else:
#     print('Outro')


#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

# valor = input('digite um valor:')

# if float(valor)>=0:
#     print('Positivo')
# elif float(valor)<0:
#     print('Negativo')
# else:
#     print('O valor digitado é texto')
    
#crie uma classe que represente uma automovel
# 
# com os atributos:
# 
# ano de fabricacao:
# marca:
# preco:
# 
# e os métodos:
# 
# get_ano;
# get_marca;
# get_preco;
# 
#   

class Automovel():

    def __init__(self, anofabricacao, marca, preco):
        self.anofabricacao = anofabricacao
        self.marca = marca
        self.preco = preco

    def get_anofabricacao(self):
        print(self.anofabricacao)

    def get_marca(self):
        print(self.marca)

    def get_preco(self):
        print(self.preco)


# carro = Automovel(2015, 'Audi', 'R$ 99.000,00')
# carro.get_anofabricacao()
# carro.get_marca()
# carro.get_preco()


#cria uma classe moto que terá:
#O atributo tipo e herdará os atribuitos/métodos da classe automovel

#e os métodos:

#obs. lembresse que a moto só pode ligar se estiver desligada e desligar quando ligada
# acelerar e frear também só ligada
#ligar, desligar, acelerar, frear

ligada = False

class Moto(Automovel):

    '''classe que representa uma moto'''

    def __init__(self, anofabricacao, marca, preco, tipo='moto'):
        super().__init__(anofabricacao, marca, preco)
        self.tipo = tipo

    def ligar(self):
        global ligada
        try:
            if ligada == False:
                print('Ligando...')
                print('Ligada...')
                self.ligada = True
            else:
                raise TypeError('Moto ligada')
        except TypeError as motoligada:
            print(motoligada)

    def desligar(self):
        global ligada
        try:       
            if self.ligada == True:
                print('Desligando...')
                print('Desligada...')
                ligada = False
            else:
                raise TypeError('Moto desligada')
        except TypeError as m:
            print(m)

    def acelerar(self):
        global ligada
        try:
            if self.ligada == True:
                print('Acelerando...')
                raise TypeError('')
        except TypeError as motoDesligada:
            print(motoDesligada)

    def frear(self):
        global ligada
        try:
            if self.ligada == True:
                print('Freando...')
                raise TypeError('')
        except TypeError as motoDesligada:
            print(motoDesligada)
            

    
mt = Moto(2010, 'Honda', 'R$ 15.000,00')
mt.ligar()
mt.acelerar()
mt.frear()
mt.desligar()
mt.get_anofabricacao()
mt.get_marca()
mt.get_preco()

    

