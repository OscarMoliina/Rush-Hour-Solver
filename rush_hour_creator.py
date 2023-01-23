import sys

def generar_juego(r:list, horizontales: dict, verticales: dict, n: int):
    with open('problem1.pddl', 'w') as f:
        f.write('(define (problem rush_hour) (:domain rush_hour)\n')

        # ---- OBJECTS ---- 
        
        #Horizontales
        f.write('(:objects\n')
        f.write('\tR')
        for i in range(1,len(horizontales)+1):
            f.write(f' H{i}')
        f.write(' - hor\n')

        #Verticales
        if len(verticales) > 0:
            f.write('\t')
            for i in range(1,len(verticales)+1):
                f.write(f'V{i} ')
            f.write('- ver\n')
        else:
            f.write('\n')

        #Casillas
        for i in range(n,0,-1):
            f.write('\t')
            for j in range(1,n+1):
                f.write(f'C{i}{j} ')
            f.write('- casilla\n')
        f.write(')\n\n')
        
        # ---- INIT ----
        f.write('(:init\n\t')

        #ArribaDe
        for j in range(1,n+1):
            for i in range(1,n):
                f.write(f'(ArribaDe C{i+1}{j} C{i}{j}) ')
            f.write('\n\t')
        f.write('\n')
        
        #DerechaDe
        for j in range(1,n):
            f.write('\t')
            for i in range(1,n+1):
                f.write(f'(DerechaDe C{i}{j+1} C{i}{j}) ')
            f.write('\n')
        f.write('\n')

        #ExtremoNS
        f.write('\t')
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==1 or i==6:
                    f.write(f'(ExtremoNS C{i}{j}) ')
        f.write('\n')

        #ExtremoEO
        f.write('\t')
        for j in range(1,n+1):
            for i in range(1,n+1):
                if j==1 or j==6:
                    f.write(f'(ExtremoEO C{i}{j}) ')
        f.write('\n')

        #Rojo
        f.write('\t')
        for i in r:
            f.write(f'(En R C{i}) ')
        f.write(f'(CabezaEn R C{r[-1]}) (ColaEn R C{r[0]})')
        f.write('\n')

        #Coches H
        for c in horizontales.keys():
            f.write('\t')
            for casilla in horizontales[c]:
                f.write(f'(En H{c} C{casilla}) ')
            f.write(f'(CabezaEn H{c} C{horizontales[c][-1]}) (ColaEn H{c} C{horizontales[c][0]})\n')
        
        for c in verticales.keys():
            f.write('\t')
            for casilla in verticales[c]:
                f.write(f'(En V{c} C{casilla}) ')
            f.write(f'(CabezaEn V{c} C{verticales[c][-1]}) (ColaEn V{c} C{verticales[c][0]})\n')

        #Libre
        f.write('\t')
        casillas = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                casillas.append(int(str(i)+str(j)))
        for i in horizontales.values():
            for j in i:
                if j in casillas:
                    casillas.remove(j)
        for i in verticales.values():
            for j in i:
                if j in casillas:
                    casillas.remove(j)
        for i in r:
            if i in casillas:
                casillas.remove(i)
        for i in casillas:
            f.write(f'(Libre C{i}) ')

        f.write('\n)\n')

        # ---- GOAL ----
        f.write('\n(:goal (and\n\t')
        f.write(f'(CabezaEn R C{n-2}{n})')
        f.write('\n))')

        f.write('\n)')
    f.close()

#r, hor, ver, n = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

generar_juego([41,42],{1:[12,13],2:[33,34,35],3:[25,26],4:[65,66]},{1:[11,21],2:[51,61],3:[22,32],4:[43,53,63],5:[14,24],6:[54,55],7:[36,46,56]},6)
