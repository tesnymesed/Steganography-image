from PIL import Image 
import numpy



#convertir l'image  vers l'espace ycbcr en luminance seulement
def YCbCr_image_Black(image):
    image_ycbcr=Image.new('RGB',(image.width,image.height))
    for i in range(image.height):
        for j in range(image.width):
            pixel=image.getpixel((j,i))
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            y=0.299*r+0.587*g+0.114*b
            image_ycbcr.putpixel((j,i),(round(y),round(y),round(y)))
    return image_ycbcr      

#la meme que la precedante  mais elle est en couleur
def YCbCr_image_color(image):
    image_ycbcr=Image.new('RGB',(image.width,image.height))
    for i in range(image.height):
        for j in range(image.width):
           
            pixel=image.getpixel((j,i))
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            y=0.299*r+0.587*g+0.114*b
            cb=-0.1687*r-0.03313*g+0.5*b+128
            cr=0.5*r-0.4187*g-0.0813*b+128
            image_ycbcr.putpixel((j,i),(round(y),round(cb),round(cr)))

    return image_ycbcr   

#elle retourne une matrice a 3 dimensions
def convert_RGB_to_YCbCr(image):
    
    
    img=numpy.ones((image.height,image.width,3) )
    for i in range(image.height):
        for j in range(image.width):
            pixel =image.getpixel((j,i))
            #print('\n-----------------------\n'+str(pixel))
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]
            y=0.299*r+0.587*g+0.114*b
            cb=-0.1687*r-0.3313*g+0.5*b+128
            cr=0.5*r-0.4187*g-0.0813*b+128
            
            img[i][j][0]=y
            img[i][j][1]=cb
            img[i][j][2]=cr

    return  img

#elle retourne une image en RGB
def convert_YCbCr_to_RGB(matrice):
    shape =matrice.shape
    height=shape[0]
    width=shape[1]
    image=Image.new('RGB',(width,height))
    for i in range (height) :
        for j in range(width):
            y=matrice[i][j][0]
            cb=matrice[i][j][1]
            cr=matrice[i][j][2]
            r=round(y+1.402*(cr-128))
            g=round(y-0.34414*(cb-128)-0.71414*(cr-128))
            b=round(y+1.772*(cb-128))
            image.putpixel((j,i),(int(r),int(g),int(b)))

    return image   

#elle retourne un array d'octet
def string2bits(s=""):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bit2strings (b=None):
    return ''.join([chr(int(x,2) for x in b)])


def bits_sequence_len(s):
    return  len(s)*8

#elle retourne un array de bits
def octet_to_bit (texte):
    octet=string2bits(texte)
    array=[]
    for i in range (len(octet)):
        byte=octet[i]
        for k in range(8):
            array.append(str(byte[k]))
            

    return array     

def bit_to_string(bits):
    lettre=[]
    i=0
    while i<len(bits):
        x=bits[i:i+8]
        y=[''.join(j for j in x)]
        char=int(y[0],2)
        letre=chr(char)
        lettre.append(letre)
        i=i+8

    return ''.join(j for j in lettre)  

def b(array):
    for i in range(len(array)):
        if array[i]=='b':
            array[i]='0'
            