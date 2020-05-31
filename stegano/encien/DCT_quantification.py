import numpy
import math
import stegano.affichage
def quantization_table():
   quantization_matrix = numpy.array([[16,  11,  10,  16,  24,  40,  51,  61],
   [12,  12,  14,  19,  26,  58,  60,  55],
   [14,  13,  16,  24,  40,  57,  69,  56],
   [14,  17,  22,  29,  51,  87,  80,  62],
   [18,  22,  37,  56,  68, 109, 103,  77],
   [24,  35,  55,  64,  81, 104, 113,  92],
   [49,  64,  78,  87, 103, 121, 120, 101],
   [72,  92,  95,  98, 112, 100, 103,  99]])
   return quantization_matrix     




def DCT_coefficients_Y (matrix,position):
    
    shape=matrix.shape
    height=shape[0]
    width=shape[1]
    DCT_matrix =numpy.ones((height,width))
    for i in range(height):
        for j in range(width):
            #ci and cj depends on frequency as well as number of row and columns of specified matrix 
            if i==0 :
                ci=1/math.sqrt(height)

            else :
                ci = math.sqrt(2) / math.sqrt(height)

            if j==0 :
              cj = 1 / math.sqrt(width)

            else :
                cj = math.sqrt(2) / math.sqrt(width)

            sum=0 
            for k in range (height) :
                for l in range (width):
                 dct1= matrix[k][l][int(position)]*math.cos((2 * k + 1) * i * math.pi / (2 * width))*math.cos((2 * l + 1) * j * math.pi / (2 * width))
                
                 sum = sum + dct1

            DCT_matrix[i][j] = ci * cj * sum 
            

    return DCT_matrix                  



def IDCT_coefficients_Y (matrix):
    shape =matrix.shape
    height=shape[0]
    width=shape[1]
    IDCT_matrix=numpy.ones((8,8))
    for x in range (height):
        for y in range(width):
            sum=0
            for i in range(height):
                for j in range(width):
                    if i==0 :
                      ci=1/math.sqrt(height)

                    else :
                      ci = math.sqrt(2) / math.sqrt(height)

                    if j==0 :
                      cj = 1 / math.sqrt(width)

                    else :
                      cj = math.sqrt(2) / math.sqrt(width)

                    idct1= matrix[i][j]*math.cos((2 * x + 1) * i * math.pi / (2 * height))*math.cos((2 * y + 1) * j * math.pi / (2 * width))
                    sum=sum+idct1*cj*ci

            IDCT_matrix[x][y]=  sum

    return IDCT_matrix           

def copy (originale):
    height,width=originale.shape
    copie=numpy.ones((height,width))
    for i in range (height):
        for j in range(width):
            copie[i][j]=originale[i][j]

    return copie 


def copy3 (originale):
    height,width=originale.shape
    copie=numpy.ones((height,width,3))
    for i in range (height):
        for j in range(width):
            copie[i][j][0]=originale[i][j][0]
            copie[i][j][1]=originale[i][j][1]
            copie[i][j][2]=originale[i][j][2]

    return copie 
#entree: un array de blocs 8*8*3 en sortie array de 8*8
def quantized_dct_array(array,position,methode):
    if methode ==1 :

      quantization=quantization_table() 

    if methode ==2:
        quantization=table_quantification_modifie()


    bloc_height,bloc_width,height,width,prix=array.shape
    array_dct=numpy.ones((bloc_height,bloc_width,height,width))

    for i in range (bloc_height):
        for j in range (bloc_width):
            

            calcul_matrix=array[i][j]
            

            matrix_dct=DCT_coefficients_Y(calcul_matrix,position)   
            matrix_dct_quantized=numpy.ones((8,8)) 
           
            for k in range(8):
                for l in range (8):
                    matrix_dct_quantized[k][l]=round(matrix_dct[k][l]/quantization[k][l])


            array_dct[i][j]=matrix_dct_quantized   

    return array_dct     

def iquantized_dct_array(array,methode):
    if methode==1:

      quantization=quantization_table()

    if methode==2:
        quantization=table_quantification_modifie()

    bloc_height,bloc_width,height,width=array.shape
    array_idct = numpy.ones((bloc_height,bloc_width,height,width))

    for i in range(bloc_height):
        for j in range(bloc_width):
            

            matrix_calcul= copy(array[i][j])
            matrix_iquantized=numpy.ones((8,8))

            for k in range (8):
                for l in range (8):
                  matrix_iquantized[k][l]=matrix_calcul[k][l]*quantization[k][l]

            matrix_iquantized=IDCT_coefficients_Y(matrix_iquantized)
            array_idct[i][j]=matrix_iquantized
            
    return array_idct    

#elle retourne une matrice dans l'espace ycbcr
def dct_idct_image(result_matrix,one_bloc_2dim_y,position):
    shape=result_matrix.shape
    height=shape[0]
    width=shape[1]

    dct_idct_matrix=numpy.ones((height,width,shape[2]))
    if position==0 :
       for i in range (height):
           for j in range(width):
               y=one_bloc_2dim_y[i][j]
               cb=result_matrix[i][j][1]
               cr=result_matrix[i][j][2]
               dct_idct_matrix[i][j][0]=y
               dct_idct_matrix[i][j][1]=cb
               dct_idct_matrix[i][j][2]=cr

    if position ==1:
         for i in range (height):
           for j in range(width):
               cb=one_bloc_2dim_y[i][j]
               y=result_matrix[i][j][0]
               cr=result_matrix[i][j][2]
               dct_idct_matrix[i][j][0]=y
               dct_idct_matrix[i][j][1]=cb
               dct_idct_matrix[i][j][2]=cr

    if position==2 :
         for i in range (height):
           for j in range(width):
               cr=one_bloc_2dim_y[i][j]
               y=result_matrix[i][j][0]
               cb=result_matrix[i][j][1]
               dct_idct_matrix[i][j][0]=y
               dct_idct_matrix[i][j][1]=cb
               dct_idct_matrix[i][j][2]=cr




    return dct_idct_matrix   


def table_quantification_modifie():

   quantization_modifie = numpy.array([[16,  11,  10,  16,  1,  1,  1,  1],
   [12,  12,  14,  1,  1,  1,  1,  55],
   [14,  13,  1,  1,  1,  1,  69,  56],
   [14,  1,  1,  1,  1,  87,  80,  62],
   [1,  1,  1,  1,  68, 109, 103,  77],
   [1,  1,  1,  64,  81, 104, 113,  92],
   [1,  1,  78,  87, 103, 121, 120, 101],
   [1,  92,  95,  98, 112, 100, 103,  99]])

   return quantization_modifie



