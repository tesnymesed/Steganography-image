from PIL import Image 
import numpy

#cette fonction permet de redimensioner l'image pour quelle soit divisible en blocs de 8*8
def redimensioner(image):
     image_width =image.width 
     image_height=image.height 
     rest_division_width8= int(image_width%8)
     rest_division_height8 =int(image_height%8)
     print("reste de la division de la largeur par 8 = ",rest_division_width8)
     print("reste de la division de lhauteur par 8 =",rest_division_height8)
     image_width-= rest_division_width8
     image_height-=rest_division_height8
     print("les nouvelle coordonnée de limage :\n width = ",image_width,"\n height =",image_height) 
     image_new_size=image.resize((image_width,image_height))
     #image_new_size.save('stegano\\static\\img'+'\\'+'lena2.jpg')
     return image_new_size

def redimensioner2(image, image_width ,image_height):
    image_new_size=image.resize((image_width,image_height))
    return image_new_size

# diviser limage en blocs de 8*8
def bloc_partition(array,bloc_size):
    
    shape =array.shape
    height=shape[0]
    width=shape[1]
    print(height)
    print(width)
    height_bloc = int(height/bloc_size)
    width_bloc = int(width/bloc_size)
    array_data=numpy.reshape(array,(height_bloc,width_bloc,8,8,3))
    return array_data


def i_bloc_partition(array):
    print(array.shape)
    bloc_width,bloc_height,width,height,pix=array.shape
    new_array=numpy.reshape(array,(width*bloc_width,height*bloc_height,3))
    print(new_array.shape)

    return new_array 

#de plusieurs blocs de dimension 2 vers un bloc de dimension deux 
def i_bloc_partition_1dim(array):
    bloc_height,bloc_width,height,width=array.shape
    new_array=numpy.reshape(array,(bloc_height*height,bloc_width*width))
    return new_array 


