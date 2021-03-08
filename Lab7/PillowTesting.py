from PIL import Image, ImageFilter
input1 = input("Enter the name of the .png in the folder this script is running in: ")
input2 = input("Input if you would like to BLUR, EMBOSS, or SHARPEN: ")
originalimage = Image.open(input1)
originalimage.load()

if input2 == "BLUR":
    blurredimage = originalimage.filter(ImageFilter.BLUR)
    originalimage.show()
    blurredimage.show()
    
elif input2 == "EMBOSS":
    embossimage = originalimage.filter(ImageFilter.EMBOSS)
    originalimage.show()
    embossimage.show()
    
elif input2 == "SHARPEN":
    sharpenimage = originalimage.filter(ImageFilter.SHARPEN)
    originalimage.show()
    sharpenimage.show()
    

















