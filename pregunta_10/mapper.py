#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        renglon = str(line).replace('\n','').split('\t')
        fila =  float(renglon[0])/10
        texto =  renglon[1]
        sys.stdout.write("{}\t{}\n".format(fila,texto))