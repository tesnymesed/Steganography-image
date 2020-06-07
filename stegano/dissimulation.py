import stegano.conversion
import numpy
import stegano.DCT_quantification
import math
#from codage_message import crypt,decrypt
import stegano.codage_message

# def cle_insertion(bits_len,nb_matrix):
#     x=math.ceil(bits_len/nb_matrix)
#     rest = bits_len%nb_matrix
#     return x,rest

# #fonction d'insertion
# def insertion (array , msg_binaire):
#     octet= msg_binaire #elle retourne un tableau qui va contenir tous les bits 
#     bloc_height,bloc_width,height,width=array.shape
#     nb_bits_a_inserer=len(octet)
#     nb_bits_par_bloc, rest=cle_insertion(nb_bits_a_inserer,bloc_height*bloc_width)
#     pos=0
#     bit_inserer=0
    
#     nbr_bloc_a_inseret = (bloc_height*bloc_width) - rest
#     h = math.ceil(nbr_bloc_a_inseret/bloc_width)
#     #array_insertion=numpy.ones((bloc_height,bloc_width,height,width)) #ce tableau va contenir toutes les sous-matrice apres insertion
#     for  i in range (h):
#         for  j in range (bloc_width) :
#             #calcul_matrix=stegano.DCT_quantification.copy(array [i][j])
            
            

#             cpt=0
      
#             for  k  in range(height) :
#                 for l in range(width) :
#                     if  array [i][j][k][l]!=0 and array [i][j][k][l]!=1 and array [i][j][k][l]!=-1 and bit_inserer<nb_bits_a_inserer:
#                         if cpt<nb_bits_par_bloc:
#                             break

#                         x=bin(int(array [i][j][k][l]))
#                         z=x[0:len(x)-1]+str(octet[pos])
#                         y=int(z,2)
#                         array [i][j][k][l]=y
#                         pos=pos+1
#                         cpt=cpt+1
#                         bit_inserer=bit_inserer+1

#                 if cpt<nb_bits_par_bloc:
#                     break

#             nbr_bloc_a_inseret=nbr_bloc_a_inseret-1
#             if nbr_bloc_a_inseret == 0:
#                 break

   
#             #array_insertion[i][j]=array [i][j]   
         


#     return array #array_insertion   

# def extraction (data,cle1):

#     bloc_height,bloc_width,height,width=data.shape
#     bits=[]
#     nb_bits_par_bloc, rest=cle_insertion(cle1,bloc_height*bloc_width)
#     nb_bits_extrait=0
#     nb_bits_a_extraire=cle1
#     nbr_bloc_a_inseret = (bloc_height*bloc_width) - rest
#     h = math.ceil(nbr_bloc_a_inseret/bloc_width)
#     for  i in range(h) :
#         for j in range(bloc_width) :
            
#            # matrix_extraction=data[i][j]
            
                
#             cpt=0
            
#             for k in range (height) :
#                 for l in  range(width) :
#                     if data[i][j][k][l]!=0 and data[i][j][k][l]!=1  and data[i][j][k][l]!=-1 and nb_bits_extrait<nb_bits_a_extraire :
#                         if cpt<nb_bits_par_bloc:
#                             break
#                         x=int(data[i][j][k][l])
#                         y=bin(x)
#                         bits.append(y[len(y)-1])
#                         nb_bits_extrait=nb_bits_extrait+1
#                         cpt=cpt+1
                
#                 if cpt<nb_bits_par_bloc:
#                     break


#             nbr_bloc_a_inseret=nbr_bloc_a_inseret-1
#             if nbr_bloc_a_inseret == 0:
#                 break


#     return stegano.conversion.bit_to_string(bits)

def cle_insertion(bits_len,nb_matrix):
    x=int(bits_len/nb_matrix)+1
    return x

#fonction d'insertion
def insertion (array , msg_binaire):
    octet= msg_binaire #elle retourne un tableau qui va contenir tous les bits 
    bloc_height,bloc_width,height,width=array.shape
    nb_bits_a_inserer=len(octet)
    nb_bits_par_bloc=cle_insertion(nb_bits_a_inserer,bloc_height*bloc_width)
    pos=0
    bit_inserer=0
    
    
    array_insertion=numpy.ones((bloc_height,bloc_width,height,width)) #ce tableau va contenir toutes les sous-matrice apres insertion
    n=0
    for  i in range (bloc_height):
        for  j in range (bloc_width) :
            calcul_matrix=stegano.DCT_quantification.copy(array [i][j])
            
            

            cpt=0
            for  k  in range(height) :
                for l in range(width) :
                    if  calcul_matrix[k][l]!=0 and calcul_matrix[k][l]!=1 and calcul_matrix[k][l]!=-1 and bit_inserer<nb_bits_a_inserer and cpt<nb_bits_par_bloc :

                        x=bin(int(calcul_matrix[k][l]))
                        z=x[0:len(x)-1]+str(octet[pos])
                        y=int(z,2)
                        calcul_matrix[k][l]=y
                        pos=pos+1
                        cpt=cpt+1
                        bit_inserer=bit_inserer+1
                    
                    if  calcul_matrix[k][l]!=0 and calcul_matrix[k][l]!=1 and calcul_matrix[k][l]!=-1:
                        n += 1 
                

   
            array_insertion[i][j]=calcul_matrix   
         

    print('\n ----------\n nombre de bit inserer qui peut etre inseret : '+str(n))
    return array_insertion   

def extraction (data,cle1):

    bloc_height,bloc_width,height,width=data.shape
    bits=[]
    nb_bits_par_bloc=cle_insertion(cle1,bloc_height*bloc_width)
    nb_bits_extrait=0
    nb_bits_a_extraire=cle1

    for  i in range(bloc_height) :
        for j in range(bloc_width) :
            
            matrix_extraction=data[i][j]
            
                
            cpt=0
            
            for k in range (height)   :
                for l in  range(width) :
                    if matrix_extraction[k][l]!=0 and matrix_extraction[k][l]!=1  and matrix_extraction[k][l]!=-1 and nb_bits_extrait<nb_bits_a_extraire and cpt<nb_bits_par_bloc  :

                        
                        x=int(matrix_extraction[k][l])
                        y=bin(x)
                        bits.append(y[len(y)-1])
                        nb_bits_extrait=nb_bits_extrait+1
                        cpt=cpt+1


    return stegano.conversion.bit_to_string(bits)




def case_insertion ():
    cases=numpy.array([[0,4],[0,5],[0,6],[0,7],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[5,0],[5,1],[5,2],[6,0],[6,1],[7,0]])
    return  cases 

def insertion_methode2(array , msg_binaire, bit):

    octet= msg_binaire #elle retourne un tableau qui va contenir tous les bits 
    bloc_height,bloc_width,height,width=array.shape
    
    pos=0
    bit_inserer=0
    nb_bits_a_inserer=len(msg_binaire)
    cases= case_insertion()
    i=0
    j=0

    array_insertion=numpy.ones((bloc_height,bloc_width,height,width))
   

 
    
    for i in range(bloc_height):
        for j in range(bloc_width):

            calcul_matrix =stegano.DCT_quantification.copy(array [i][j])
            
            k=0
            cpt=0
        
            

            while k<26 and nb_bits_a_inserer>bit_inserer  :
                position=cases[k]
                coef=calcul_matrix[position[0]][position[1]]
                x=bin(int(coef))

                if nb_bits_a_inserer - bit_inserer !=1 :
                    z=x[0:len(x)-2]+str(msg_binaire[pos])
                
                    pos=pos+1

                    z=z[0:len(z)]+str(msg_binaire[pos])
                    cpt=cpt+2
                    bit_inserer=bit_inserer+2
                    pos=pos+1

                else:
                       
                    z=x[0:len(x)-1]+str(msg_binaire[pos])
                    pos=pos+1
                    cpt=cpt+1
                    bit_inserer=bit_inserer+1
                    

               
                y=int(z,2)
                calcul_matrix[position[0]][position[1]]=y
                k=k+1



            array_insertion[i][j]=calcul_matrix   
           
    


    return array_insertion



def extraction_methode2(array,taille_message,bit):
    bloc_height,bloc_width,height,width=array.shape
    bits=[]
    
    nb_bits_extrait=0
    nb_bits_a_extraire=taille_message
    cases=case_insertion()
    

    for i in range(bloc_height):
        for j in range(bloc_width):
            extraction_matrix=array[i][j]
            cpt=0
            k=0
            
            while k<26  and nb_bits_extrait<nb_bits_a_extraire :
                position=cases[k]
                x=int(extraction_matrix[int(position[0])][int(position[1])])
                
                y=bin(x)
               
                if nb_bits_a_extraire-nb_bits_extrait!=1:

                   bits.append(y[len(y)-2])
                   bits.append(y[len(y)-1])
                   nb_bits_extrait=nb_bits_extrait+2
                   cpt=cpt+2

                else:
                    bits.append(y[len(y)-1])
                    nb_bits_extrait=nb_bits_extrait+1
                    cpt=cpt+1

                k=k+1

    stegano.conversion.b(bits)
  
    message = stegano.conversion.bit_to_string(bits)
    print('le message apres déchifrement :'+str(message))
    msg_dechiffrer=stegano.codage_message.decrypt(message,bit)
    print(' message dechiffrer : '+str(msg_dechiffrer))
    return msg_dechiffrer           







           

    