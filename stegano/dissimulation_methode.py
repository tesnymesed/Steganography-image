import stegano.redimension, stegano.conversion, stegano.DCT_quantification, stegano.dissimulation, stegano.psnr_mse, stegano.extraction_methode

from PIL import Image

def dissimulation_methode1(image_cover, message):

    image_stego=stegano.redimension.redimensioner(image_cover)  
    image_YCbCr=stegano.conversion.convert_RGB_to_YCbCr(image_stego)
    list_8x8=stegano.redimension.bloc_partition(image_YCbCr,8)
    list_8x8_quantized_Y=stegano.DCT_quantification.quantized_dct_array(list_8x8,0,int(1))
    list_8x8_quantized_Cb=stegano.DCT_quantification.quantized_dct_array(list_8x8,1,int(1))
    list_8x8_quantized_Cr=stegano.DCT_quantification.quantized_dct_array(list_8x8,2,int(1))
    msg_binaire=stegano.conversion.octet_to_bit(message)
    taille_message=len(msg_binaire)
    
    cle=taille_message #calculé pour lextractiion

    list_8x8_quantized_insertion_Y =stegano.dissimulation.insertion(list_8x8_quantized_Y,msg_binaire)
    list_8x8_quantized_insertion_Cb =stegano.dissimulation.insertion(list_8x8_quantized_Cb,msg_binaire)
    list_8x8_quantized_insertion_Cr =stegano.dissimulation.insertion(list_8x8_quantized_Cr,msg_binaire)

    idct_iquantized_Y=stegano.DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion_Y,int(1))
    idct_iquantized_Cb=stegano.DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion_Cb,int(1))
    idct_iquantized_Cr=stegano.DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion_Cr,int(1))
    one_bloc_2dim_y_Y=stegano.redimension.i_bloc_partition_1dim(idct_iquantized_Y)
    one_bloc_2dim_y_Cb=stegano.redimension.i_bloc_partition_1dim(idct_iquantized_Cb)
    one_bloc_2dim_y_Cr=stegano.redimension.i_bloc_partition_1dim(idct_iquantized_Cr)


    image_result_dct_idct_Y=stegano.DCT_quantification.dct_idct_image(image_YCbCr,one_bloc_2dim_y_Y,int(0))
    image_result_dct_idct_Cb=stegano.DCT_quantification.dct_idct_image(image_YCbCr,one_bloc_2dim_y_Cb,int(1))
    image_result_dct_idct_Cr=stegano.DCT_quantification.dct_idct_image(image_YCbCr,one_bloc_2dim_y_Cr,int(2))

    image_stego_Y=stegano.conversion.convert_YCbCr_to_RGB(image_result_dct_idct_Y)
    image_stego_Cb=stegano.conversion.convert_YCbCr_to_RGB(image_result_dct_idct_Cb)
    image_stego_Cr=stegano.conversion.convert_YCbCr_to_RGB(image_result_dct_idct_Cr)

    psnr_Y=stegano.psnr_mse.calculate_psnr(image_stego,image_stego_Y)
    psnr_Cb=stegano.psnr_mse.calculate_psnr(image_stego,image_stego_Cb)
    psnr_Cr=stegano.psnr_mse.calculate_psnr(image_stego,image_stego_Cr)

    if psnr_Y >= psnr_Cb and psnr_Y>psnr_Cr : return image_stego_Y, 0, cle
    if psnr_Cb >= psnr_Y and psnr_Cb > psnr_Cr : return image_stego_Cb,1, cle
    return image_stego_Cr,2, cle

def dissimulation_methode2(image_cover, message, bit) :

    image_stego=stegano.redimension.redimensioner(image_cover)  
    image_YCbCr=stegano.conversion.convert_RGB_to_YCbCr(image_stego)
    list_8x8=stegano.redimension.bloc_partition(image_YCbCr,8)
    list_8x8_quantized_Y=stegano.DCT_quantification.quantized_dct_array(list_8x8,0,int(2))
    list_8x8_quantized_Cb=stegano.DCT_quantification.quantized_dct_array(list_8x8,1,int(2))
    list_8x8_quantized_Cr=stegano.DCT_quantification.quantized_dct_array(list_8x8,2,int(2))
    msg_binaire=stegano.conversion.octet_to_bit(message)
    taille_message=len(msg_binaire)

    list_8x8_quantized_insertion_Y =stegano.dissimulation.insertion_methode2(list_8x8_quantized_Y,msg_binaire, bit)
    list_8x8_quantized_insertion_Cb =stegano.dissimulation.insertion_methode2(list_8x8_quantized_Cb,msg_binaire, bit)
    list_8x8_quantized_insertion_Cr =stegano.dissimulation.insertion_methode2(list_8x8_quantized_Cr,msg_binaire, bit)

    
    idct_iquantized_Y=stegano.DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion_Y,int(2))
    idct_iquantized_Cb=stegano.DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion_Cb,int(2))
    idct_iquantized_Cr=stegano.DCT_quantification.iquantized_dct_array(list_8x8_quantized_insertion_Cr,int(2))
    one_bloc_2dim_y_Y=stegano.redimension.i_bloc_partition_1dim(idct_iquantized_Y)
    one_bloc_2dim_y_Cb=stegano.redimension.i_bloc_partition_1dim(idct_iquantized_Cb)
    one_bloc_2dim_y_Cr=stegano.redimension.i_bloc_partition_1dim(idct_iquantized_Cr)


    image_result_dct_idct_Y=stegano.DCT_quantification.dct_idct_image(image_YCbCr,one_bloc_2dim_y_Y,int(0))
    image_result_dct_idct_Cb=stegano.DCT_quantification.dct_idct_image(image_YCbCr,one_bloc_2dim_y_Cb,int(1))
    image_result_dct_idct_Cr=stegano.DCT_quantification.dct_idct_image(image_YCbCr,one_bloc_2dim_y_Cr,int(2))

    image_stego_Y=stegano.conversion.convert_YCbCr_to_RGB(image_result_dct_idct_Y)
    image_stego_Cb=stegano.conversion.convert_YCbCr_to_RGB(image_result_dct_idct_Cb)
    image_stego_Cr=stegano.conversion.convert_YCbCr_to_RGB(image_result_dct_idct_Cr)

    psnr_Y=stegano.psnr_mse.calculate_psnr(image_stego,image_stego_Y)
    psnr_Cb=stegano.psnr_mse.calculate_psnr(image_stego,image_stego_Cb)
    psnr_Cr=stegano.psnr_mse.calculate_psnr(image_stego,image_stego_Cr)

    if psnr_Y >= psnr_Cb and psnr_Y>psnr_Cr : return image_stego_Y, 0, taille_message, psnr_Y
    if psnr_Cb >= psnr_Y and psnr_Cb > psnr_Cr : return image_stego_Cb, 1, taille_message, psnr_Cb
    return image_stego_Cr, 2, taille_message, psnr_Cr


