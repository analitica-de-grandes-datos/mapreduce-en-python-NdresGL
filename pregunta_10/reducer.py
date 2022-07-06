#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from asyncore import write
import sys
if __name__ == '__main__':
    #Crear un string con todas las letras
    cadena = 'A'
    lista = []
    letras = []
    datos = []
    for line in sys.stdin:
        cadena += ',' + str(line).replace('\n','').split('\t')[1]
        datos.append(str(line).replace('\n','').split('\t')[0] + ' ' + str(line).replace('\n','').split('\t')[1])
    #Conseguir los valores únicos de las letras
    lista = cadena.split(',')
    lista.sort()
    key = None
    for i in lista:
        if key != i and key is not None:
            letras.append(key)
        key = i
    letras.append(i)
    fila = []
    #Encontrar las locaciones de las letras
    for letra in letras:
        ubicacion = ''
        locacion = 0
        for line in datos:
            fila = str(line).replace('\n','').split(' ')[1].split(',')
            for l in fila:
                if l == letra:
                    locacion = int(float(str(line).replace('\n','').split(' ')[0])*10)
                    ubicacion += str(locacion) + ','
        sys.stdout.write('{}\t{}\n'.format(letra,ubicacion.rstrip(',')))