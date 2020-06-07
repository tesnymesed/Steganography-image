from PIL import Image, ImageFilter, ImageFont, ImageDraw
from stegano.redimension import redimensioner


def gaussian_blur(chemain, radius):

    image1 = Image.open(chemain) 
    image2 = image1.filter(ImageFilter.GaussianBlur(radius))
    #image2.show()
    image3 = redimensioner(image2)

    return image3

def writeonImage(baseImage, description):

    baseImage = baseImage.convert('RGBA')

    txtImage = Image.new('RGBA', baseImage.size, (255,255,255,0))

 

    # Select a font

    font = ImageFont.truetype("/opt/X11/share/fonts/TTF/Vera.ttf", 150)

    draw = ImageDraw.Draw(txtImage)

    draw.text((20,60), description, font=font, fill=(255,255,255,255))

    return Image.alpha_composite(baseImage, txtImage)

def median_filter(chemain,nbr,size=5):
    """ size doit etre 3 ou 5"""

    image1 = Image.open(chemain) 
    i=0
    for i in range(nbr):
        image2 = image1.filter(ImageFilter.MedianFilter(size))
        image1=image2
    #image2.show()
    image3 = redimensioner(image1)
    return image3

if __name__ == "__main__":
    median_filter('..\static\img\\test2.jpg',3,1)
    

