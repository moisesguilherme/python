# encoding: utf-8
#Usando forech e arrays
carros = ['Fiat 500', 'Gol', 'Fiesta', 'Fusca']
motoristas = ['João', 'Maria', 'José', 'Carlos']
count = 0

for c in carros:
    print('Carro {} pertence a {}'.format(c, motoristas[count]))
    count+=1