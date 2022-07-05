#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
for line in sys.stdin:
    letra,fecha,numero=line.split('   ')
    dia,mes,ano=fecha.split('-')
    sys.stdout.write('{}\t1\n'.format(mes)) 