# class Pai():
#     '''classe pai'''

#     def __init__(self):
#         self.sobrenome = 'Pereira'

#     def get_sobrenome(self):
#         print(self.sobrenome)

# class Filho(Pai):

#     def __init__(self):
#         super().__init__()

# joao = Pai()
# joaquim = Filho()

# joaquim.get_sobrenome()

# class Animal():

#     def __init__(self, raca, idade):
#         self.raca = raca
#         self.idade = idade
#         self.olhos = True
#         self.orgaos = True

#     def Nascer(self):
#         print('Nasceu...')
#     def AlimentarSe(self):
#         print('Se alimentando...')
#     def Morrer(self):
#         print('Morreu...')

#     def get_raca(self):
#         print(self.raca)

#     def get_idade(self):
#         print(self.idade)


# class Mamifero(Animal):

#     def __init__(self, raca, idade):
#         super().__init__(raca, idade)
#         self.leite = True
#         self.mamilos = True



# class Humano(Mamifero):
    
#     def __init__(self, nome, idade, pensa=True):
#         super().__init__()
#         self.nome = nome
#         self.idade = idade
#         self.pensa = pensa
#         self.bracos = 2
#         self.pernas = 2
#         self.cabeca = 1
#         self.tronco = 1

    # def Pensar(self):
    #     print('pensando...')

# humano1 = Humano('Joao', '33')
# print(humano1.nome, humano1.idade, humano1.pensa)

# cachorro = Mamifero('Pastor', 7)
# cachorro.get_idade()

# joao.Nascer()
# joao.AlimentarSe()
# joao.Morrer()
# print(joao.bracos)
# joao.Pensar()


#polimorfismmo

class Pai():

    def trabalhar(self):
        print('Trabalhando de Engenheiro...')

class Filho(Pai):

    def fazerNada(self):
        print('Fazendo nada...')

    # def trabalhar(self):
    #     print('Trabalhando de Programador...')

# usa no modulo
if __name__ == "__main__":

    joao = Pai()
    joao.trabalhar()

# joaquim = Filho()
# joaquim.trabalhar()

