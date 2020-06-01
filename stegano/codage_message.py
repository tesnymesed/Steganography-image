
from random import random
import math

ALPHABET=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
				"1","2","3","4","5","6","7","8","9","0",
				" ","'","é","à",'"',"-","=","+","*","è","ç","#","&","<",">",",",".",";",":","!","?","@","(",")","{","}","/",'%',"[","]",'\\','\x11','ä',
				"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

# fonction de chiffrement affine

def chiffrementAffine(a,cle,L):

        
        #x=ALPHABET.index(L)
        x=ord(L)
        
        y=(a*x+cle)%(len(ALPHABET))
        if ALPHABET[y] == '\\':
            return ALPHABET[y]+'\\'
        return ALPHABET[y]

# Calcul de l'inverse d'un nombre modulo (len(ALPHABET))

def inverse(a):
        x=0
        while (a*x%(len(ALPHABET))!=1):
                x=x+1
        return x

# Fonction de déchiffrement

def dechiffrementAffine(a,cle,L):

    #x=ALPHABET.index(L)
    x=ord(L)
    
    y=(inverse(a)*(int(x)-int(cle)))%(len(ALPHABET))

    return ALPHABET[y]
                

# Affichage du mot chiffré

def crypt(message,cle):
    if (pgcd(1,(len(ALPHABET)))==1):
        mot = []
        for i in range(0,len(message)):
                mot.append(chiffrementAffine(1,cle,message[i]))
        return "".join(mot)
    else:
        return "Chiffrement impossible. Veuillez choisir un nombre a premier avec (len(ALPHABET))."

# Affichage du mot déchiffré

def decrypt(message,cle):
    if (pgcd(1,(len(ALPHABET)))==1):
        mot = []
        for i in range(0,len(message)):
                mot.append(dechiffrementAffine(1,cle,message[i]))
        return "".join(mot)
    else:
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec (len(ALPHABET))."

