import stegano.dissimulation, stegano.conversion, stegano.redimension, stegano.DCT_quantification
from PIL import Image
#import numpy

def extraction_methode1(image_stego, taille_msg, canal):

    image_ycbcr=stegano.conversion.convert_RGB_to_YCbCr(image_stego)
    image_bloc_8x8=stegano.redimension.bloc_partition(image_ycbcr,8)
    image_dct=stegano.DCT_quantification.quantized_dct_array(image_bloc_8x8,canal,1)
    texte_extraction=stegano.dissimulation.extraction(image_dct,taille_msg)

    return texte_extraction

def extraction_methode2 (image_stego, taille_msg, canal, bit):
    image_ycbcr=stegano.conversion.convert_RGB_to_YCbCr(image_stego)
    image_bloc_8x8=stegano.redimension.bloc_partition(image_ycbcr,8)
    image_dct=stegano.DCT_quantification.quantized_dct_array(image_bloc_8x8,canal,2)
    texte_extraction=stegano.dissimulation.extraction_methode2(image_dct,taille_msg,bit)

    return texte_extraction
