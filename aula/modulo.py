# import aula07

# from aula07 import Pai

# joao = aula07.Pai()


# joao = Pai()
# joao.trabalhar()

import os, pwd, sys, datetime


os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]

print(os.getlogin())

# print(os.listdir('/home/developer'))

# print(os.rename('./base.py','pandas.py'))

# os.system('ls -la')

# os.system('echo $USER')

# print(sys.platform)

# print(sys.builtin_module_names)

# print(sys.argv)

# for i in range(len(sys.argv)):
#     if i == 0:
#         print(f'Function name: {sys.argv[0]}')
#     else:
#         print(f'{i}. argument: {sys.argv[1]}')

# print(datetime.datetime.now())
# print(datetime.timedelta(7))
# print(datetime.time(14, 0, 0))
# print(datetime.date(2017, 1, 1))

import csv

with open('../arquivos/salarios.csv', 'w', newline='') as csvfile:
    arquivo = csv.writer(csvfile, delimiter=',')
    arquivo.writerow(['Teste']*5)
    arquivo.writerow(['4linux', 'Python'])