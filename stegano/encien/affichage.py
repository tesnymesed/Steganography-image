from PIL import Image 
import numpy
def afficher_image(image) :
    print("**VOICI L'IMAGE EN RGB**\n")
    matrixels = list(image.getdata())
    print(matrixels)
    width, height = image.size
    matrixels1 = [matrixels[i * width:(i + 1) * width] for i in range(height)]
    print(matrixels1)

def show_image_with_blocs(list_pixels, bloc_to_show=-1):
        if(bloc_to_show==-1):
            bloc_to_show=len(list_pixels)
        i=0
        s=0
        for i in range(bloc_to_show):
            j=0
            for j in range(len(list_pixels[i])):
                print(list_pixels[i][j] , end="")
                s=s+1
                if s%8==0:
                    print('|| \n')
                    if s%64==0:
                        print('-----------------------------------------------------------------------------------------------------------------------')
                        print('-----------------------------------------------------------------------------------------------------------------------')


def afficher_premier_8x8(image,pos):
    matrice = numpy.ones((8,8))
    for i in range(8,1):
        for j in range():
            matrice[i][j]=image[i][j][pos]
            
    print(matrice)        

          



def afficher_bloc(bloc_8x8):
    matrice=numpy.ones((8,8))
    for j in range(8):
        for k in range(8):
            matrice[j][k]=bloc_8x8[j][k]

    print(matrice)        

