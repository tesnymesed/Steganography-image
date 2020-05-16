from PIL import Image, ImageFilter, ImageFont


def gaussian_blur(chemain, radius):

    image1 = Image.open(chemain) 
    image1.show()
    image2 = image1.filter(ImageFilter.GaussianBlur(50))
    image2.show()

    return image2

def writeonImage(baseImage, description):

    baseImage = baseImage.convert('RGBA')

    txtImage = Image.new('RGBA', baseImage.size, (255,255,255,0))

 

    # Select a font

    font = ImageFont.truetype("/opt/X11/share/fonts/TTF/Vera.ttf", 150)

    draw = ImageDraw.Draw(txtImage)

    draw.text((20,60), description, font=font, fill=(255,255,255,255))

    return Image.alpha_composite(baseImage, txtImage)

def median_filter(chemain, radius):

    image1 = Image.open(chemain) 
    image1.show()
    image2 = image1.filter(ImageFilter.MedianFilter)
    output1 = writeonImage(image2, "Median Filter - 1X")
    output1.show()
    
    return output1

if __name__ == "__main__":
    median_filter('D:\Documents\isil L3\S2\PFE\web page\static\img\code1.jpg', 10)

