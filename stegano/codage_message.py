
from random import random
import math

ALPHABET=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
				"1","2","3","4","5","6","7","8","9","0",
				" ","'","é","à",'"',"-","=","+","*","è","ç","#","&","<",">",",",".",";",":","!","?","@","(",")","{","}","/",'%',
				"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

# fonction de chiffrement affine

def chiffrementAffine(a,b,L):
        
        x=ALPHABET.index(L)
        y=(a*x+b)%(len(ALPHABET))
        return ALPHABET[y]

# Calcul de l'inverse d'un nombre modulo (len(ALPHABET))

def inverse(a):
        x=0
        while (a*x%(len(ALPHABET))!=1):
                x=x+1
        return x

# Fonction de déchiffrement

def dechiffrementAffine(a,b,L):
    x=ALPHABET.index(L)
    y=(inverse(a)*(x-b))%(len(ALPHABET))
    return ALPHABET[y]
                

# Affichage du mot chiffré

def crypt(M,b):
    if (pgcd(1,(len(ALPHABET)))==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(chiffrementAffine(1,b,M[i]))
        return "".join(mot)
    else:
        return "Chiffrement impossible. Veuillez choisir un nombre a premier avec (len(ALPHABET))."

# Affichage du mot déchiffré

def decrypt(M,b):
    if (pgcd(1,(len(ALPHABET)))==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(dechiffrementAffine(1,b,M[i]))
        return "".join(mot)
    else:
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec (len(ALPHABET))."

if __name__ == "__main__":
	
	print("\n------ le message  -------")
	message = input("Enter le message a crypter : ")

	cle = int(random()*100)
	secret = crypt(message,cle)
	print("\n\nla clé secrete est :  ",cle,"  <<<<<<<<<<<<<<<<<<<<<<<<")
	print("\n\n------ le message crypté -------")
	print("le message crypté est :  ",secret)
	print("\n------ le message  -------")
	cle=int(input("Entrer la clé pour voir le message : "))
	print(decrypt(secret,cle))

