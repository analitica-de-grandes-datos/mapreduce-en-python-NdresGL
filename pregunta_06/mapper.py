#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        renglon = line.split('   ')
        letra =  renglon[0]
        fecha =  renglon[1]
        numero = renglon[2].replace("\n", "")
        sys.stdout.write("{}\t{}\n".format(letra,numero))