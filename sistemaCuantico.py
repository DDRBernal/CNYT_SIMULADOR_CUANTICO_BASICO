import calculadora.cnyt_Calculadora as cal
from sys import stdin
def probaTransitarVector(ket1,ket2):
    ket=cal.transpuestaM([ket1])
    bra=cal.conjugadaM([ket2])
    mat=cal.multiplicacionM(bra,ket)
    normaBra=cal.normaM(bra)
    normaKet=cal.normaM(ket)
    mut=normaBra*normaKet
    print(mat[0][0],(mut,0))
    return cal.divisionC(mat[0][0],mut)
def detectParticle(ket,pos):
    normaKet= cal.normaM([ket])
    normaNumComplejo=cal.normaM([[ket[pos]]])
    return (normaNumComplejo**2)/(normaKet**2)

def main():
    print("Ingrese el vector ket")
    'ej: 1 -1,1 2,0 2,3 1,1 5 sera el vector [(1,-1),(1,2),(0,2),(3,1),(1,5)]'
    
    ket=[tuple(map(int,i.split(' '))) for i in stdin.readline().strip().split(',')]
    print(ket)
    accion='a'
    while accion:
        print("Seleccione una opcion marcando solo el numero")
        print("1. Probabilidad de transitar vector a vector")
        print("2. Probabilidad de encontrar particula en una posicion dada")
        accion = (input())
        if (accion=="1"):
            print("Ingrese segundo vector ket")
            ket2=[tuple(map(int,i.split(' '))) for i in stdin.readline().strip().split(',')]
            print(ket2)
            print(probaTransitarVector(ket,ket2))
        elif (accion=="2"):
            print("Ingresa la posicion ")
            pos= int(input())
            print(detectParticle(ket,pos))
