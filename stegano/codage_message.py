
from random import random
import math

# fonction de chiffrement affine

def chiffrementAffine(cle,Lettre):

        
        x=ord(Lettre)
        
        y=(x+cle)%(1114112)
        
        return chr(y)



# Fonction de déchiffrement

def dechiffrementAffine(cle,Lettre):

    
    x=ord(Lettre)
    
    y=((int(x)-int(cle)))%(1114112)

    return chr(y)
                

# Affichage du mot chiffré

def crypt(message,cle):

    mot = []
    for i in range(0,len(message)):
        mot.append(chiffrementAffine(cle,message[i]))
    return mot
   
# Affichage du mot déchiffré

def decrypt(message,cle):
    mot = []
    for i in range(0,len(message)):
        mot.append(dechiffrementAffine(cle,message[i]))
    return "".join(mot)
    



def main():
    message = 'Les images vectorielles sont composées de formes géométriques qui vont pouvoir être décrites d’un point de vue mathématiques. Par exemple une droite sera définie par deux points, un cercle par un centre et un rayon. Le processeur est chargé de traduire ces formes par des informations interprétables par la carte graphique (voir figure I.2) [3].'
    cle = 5

    message_cry = crypt(message,cle)
    #message_fin = decrypt(message_cry,cle)
    #print(message_cry)
    message = "".join(message_cry)
    print(str(message))


if __name__ == "__main__":
    main()