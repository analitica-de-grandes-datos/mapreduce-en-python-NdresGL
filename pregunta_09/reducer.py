#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    lista=[]
    for line in sys.stdin:
        lista.append(str(line))
    c=0
    max = len(lista)^2
    while len(lista)>0:
        menor = int(str(lista[0]).replace('\n','').split('\t')[2])
        i = 0
        for line in lista:
            letra,fecha,numero = str(line).replace('\n','').split('\t')
            if menor>=int(numero):
                i =1
                menor = int(numero)
                fechamin = fecha
                letramin = letra
                borrar = line
        if c > 5:
            break
        if i == 1:
            lista.remove(borrar)
            sys.stdout.write('{}   {}   {}\n'.format(letramin,fechamin,menor))
            c+=1