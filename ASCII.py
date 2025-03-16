from PIL import Image
# String ordered according to how dense the character is
ASCII_characters = ' .:co?9W#'

def resize(image, new_width=149*4):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.42)

    return image.resize((new_width, new_height))

#def greyscale(image):
 #   return image.convert('L')

def pixel_to_ascii(image):
    pixels = image.getdata()
    print(list(pixels))
    # getdata() returns a list with values for each starting from the top left pixel and going right and then down
    #ascii_str = ''.join(ASCII_characters[pixel // 30] for pixel in pixels) 
        # Maps to ASCII depending upon how high the value is
    return None#ascii_str

def image_to_ascii(image_path, output_width=149*4):
    try:
        image = Image.open(image_path)
    # return None ensures the lines after the except block are not executed in case of an error
    except Exception as error:
        print(f'Error opening image: {error}')
        return None
    
    image = resize(image, output_width)
    #image = greyscale(image)
    ascii_str = pixel_to_ascii(image)

    # Formatting the ASCII string
    #ascii_str = '\n'.join(ascii_str[i:i+output_width] for i in range(0, len(ascii_str), output_width))
    
    #print(ascii_str)
    # Writes the .txt file
    #file_name = input('Making sure to include the .txt extension, \n Please enter a file name for the .txt file: ')
    #    f.write(ascii_str)

image_path = input('Please enter the image path: ')
image_to_ascii(image_path)
