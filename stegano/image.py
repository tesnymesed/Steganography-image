from PIL import Image 
import numpy
import math 
import stegano.affichage ,stegano.conversion,stegano.DCT_quantification,stegano.dissimulation,stegano.redimension,stegano.psnr_mse


# def dissimulation_fct(chemain, secret_text, position, UPLOAD_FOLDER, bit = 0):
#     print("**OUR APPLICATION**\n")
#     #open the image that we will work with
   
#     #methode=int(input("entrer la methode"))

#     if bit != 0:
#        methode = 2
#     else:
#        methode = 1


#     message= secret_text
#     image1 =Image.open(chemain)
#     image1.show()
#     image2=redimension.redimensioner(image1)  
#     result_matrix=conversion.convert_RGB_to_YCbCr(image2)
#     list_8x8=redimension.bloc_partition(result_matrix,8)  
    
#     list_8x8_quantized=DCT_quantification.quantized_dct_array(list_8x8,position,int(methode))
   
#     binaire=conversion.string2bits(message)
#     cle2=len(binaire)*8
#     bloc_height,bloc_width,height,width=list_8x8_quantized.shape
#     cle=dissimulation.cle_insertion(cle2,bloc_height*bloc_width)
#     print("cle2=",cle2,"cle1",cle)
#     texte=conversion.octet_to_bit(message)
#     print("voici le nombre de matrices",bloc_height*bloc_width)

#     if methode==1:

#        list_8x8_quantized_insertion =dissimulation.insertion(list_8x8_quantized,message,cle)
#        print(dissimulation.extraction(list_8x8_quantized_insertion,cle2,cle))

#     else:
#        #bit=input("entrer un bit")

#        list_8x8_quantized_insertion =dissimulation.insertion_methode2(list_8x8_quantized,message,bit)  
#        print(dissimulation.extraction_methode2(list_8x8_quantized_insertion,cle2,bit))


    
    

#     idct_iquantized=DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion,int(methode))
    
#     one_bloc_2dim_y=redimension.i_bloc_partition_1dim(idct_iquantized)

#     image_result_dct_idct=DCT_quantification.dct_idct_image(result_matrix,one_bloc_2dim_y,position)
    
#     image3=conversion.convert_YCbCr_to_RGB(image_result_dct_idct)
#     #image3.save('image_transform.jpg')
#     image3.show()
#     psnr=psnr_mse.calculate_psnr(image2,image3)
#     print("qualité d'image 2  ", psnr)   
#     return psnr, image3


# def extraction_fct(chemain,position, UPLOAD_FOLDER, bit = 0):


#     image3 =Image.open(chemain)
#     image3_ycbcr=conversion.convert_RGB_to_YCbCr(image3)
#     image3_bloc_8x8=redimension.bloc_partition(image3_ycbcr,8)
    
#     if bit != 0:
#        methode = 2
#     else:
#        methode = 1


#     image3_dct=DCT_quantification.quantized_dct_array(image3_bloc_8x8,position,int(methode))

#     print("voici le nombre de bits ",cle2,"voici le nombre de de bits par matrice ",cle)
#     if methode==1:

#        texte_extraction=dissimulation.extraction(image3_dct,cle2,cle)

#     else:
#         texte_extraction=dissimulation.extraction_methode2(image3_dct,cle2,bit)

#     print("voici le texte apres extraction \n")
#     print(texte_extraction) 
#     return texte_extraction


def pfe(chemain, secret_text, position, UPLOAD_FOLDER, bit = 0):

    print("**OUR APPLICATION**\n")
    #open the image that we will work with
   
    #methode=int(input("entrer la methode"))

    if bit != 0:
       methode = 2
    else:
       methode = 1


    message= secret_text
    image1 =Image.open(UPLOAD_FOLDER+'\\'+chemain)
    image1.show()
    image2=stegano.redimension.redimensioner(image1)  
    result_matrix=stegano.conversion.convert_RGB_to_YCbCr(image2)
    list_8x8=stegano.redimension.bloc_partition(result_matrix,8)  
    
    list_8x8_quantized=stegano.DCT_quantification.quantized_dct_array(list_8x8,position,int(methode))
   
    binaire=stegano.conversion.string2bits(message)
    cle2=len(binaire)*8
    bloc_height,bloc_width,height,width=list_8x8_quantized.shape
    cle=stegano.dissimulation.cle_insertion(cle2,bloc_height*bloc_width) #ici nous calculons combient de bloc on a besoin
    print("cle2=",cle2,"cle1",cle)
    texte=stegano.conversion.octet_to_bit(message)#on a pas besoin de cette ligne
    print("voici le nombre de matrices",bloc_height*bloc_width)

    if methode==1:

       list_8x8_quantized_insertion =stegano.dissimulation.insertion(list_8x8_quantized,message,cle)
       print(stegano.dissimulation.extraction(list_8x8_quantized_insertion,cle2,cle))

    else:
       #bit=input("entrer un bit")

       list_8x8_quantized_insertion =stegano.dissimulation.insertion_methode2(list_8x8_quantized,message,bit)  
       print(stegano.dissimulation.extraction_methode2(list_8x8_quantized_insertion,cle2,bit))


    
    

    idct_iquantized=stegano.DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion,int(methode))
    
    one_bloc_2dim_y=stegano.redimension.i_bloc_partition_1dim(idct_iquantized)

    image_result_dct_idct=stegano.DCT_quantification.dct_idct_image(result_matrix,one_bloc_2dim_y,position)
    
    image3=stegano.conversion.convert_YCbCr_to_RGB(image_result_dct_idct)
    #image3.save('image_transform.jpg')
    image3.show()
    
    print("-------------------------------------------------------------------------------\n\n")
    image3_ycbcr=stegano.conversion.convert_RGB_to_YCbCr(image3)
    image3_bloc_8x8=stegano.redimension.bloc_partition(image3_ycbcr,8)
    
    
    image3_dct=stegano.DCT_quantification.quantized_dct_array(image3_bloc_8x8,position,int(methode))
    
    print("voici le nombre de bits ",cle2,"voici le nombre de de bits par matrice ",cle)
    if methode==1:

       texte_extraction=stegano.dissimulation.extraction(image3_dct,cle2,cle)

    else:
        texte_extraction=stegano.dissimulation.extraction_methode2(image3_dct,cle2,bit)

    print("voici le texte apres extraction \n")
    print(texte_extraction) 
    psnr=stegano.psnr_mse.calculate_psnr(image2,image3)
    print("qualité d'image 2  ", psnr)   
    return psnr, image3


