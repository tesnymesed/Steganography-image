
from random import random
import math

#ALPHABET=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
#				"1","2","3","4","5","6","7","8","9","0",
#				" ","'","é","à",'"',"-","=","+","*","è","ç","#","&","<",">",",",".",";",":","!","?","@","(",")","{","}","/",'%',"[","]",'\\','\x11','ä',
#				"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'`','°','\r','\x9a','²','\n','\x0e','_','\x90']


# fonction de chiffrement affine

def chiffrementAffine(cle,L):

        
        #x=ALPHABET.index(L)
        x=ord(L)
        
        y=(x+cle)%(1114112)
        
        return chr(y)

# Calcul de l'inverse d'un nombre modulo (len(ALPHABET))

# Fonction de déchiffrement

def dechiffrementAffine(cle,L):

    #x=ALPHABET.index(L)
    x=ord(L)
    
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
    message = 'bentebbiche'
    cle = 5

    message_cry = crypt(message,cle)
    message_fin = decrypt(message_cry,cle)
    print(message_fin)


if __name__ == "__main__":
    main()