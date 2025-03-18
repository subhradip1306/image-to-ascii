from PIL import Image
# String ordered according to how dense the character is
ASCII_characters = ' .:co?9W#'

def resize(image, new_width=180):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.47)

    return image.resize((new_width, new_height))

def greyscale(image):
    return image.convert('L')

def diff(pixel1, pixel2):
    difference = ((pixel1[0]-pixel2[0])**2+(pixel1[1]-pixel2[1])**2+(pixel1[2]-pixel2[2])**2)**(1/2)
    return difference

def pixel_to_ascii(image, grey_image):
    pixels = image.getdata()
    grey_pixels = grey_image.getdata()
    # getdata() returns a list with values for each starting from the top left pixel and going right and then down
    ascii_str = ''
    for i in range(len(list(pixels))):
            try:
                if diff(pixels[i], pixels[i+1])>90:
                    ascii_str += '|' 
		            # Enters a vertical border when two consecutive pixels have a very different color
                elif diff(pixels[i], pixels[i+180])>90:
                    ascii_str += '-'
                else:
	                ascii_str += ASCII_characters[grey_pixels[i] // 30] 
                    # Maps to ASCII depending upon how high the value is

            except TypeError:
                ascii_str += ASCII_characters[pixels[i] // 30]

            except IndexError:
                continue

    return ascii_str

def image_to_ascii(image_path, output_width=180):
    try:
        image = Image.open(image_path)
    # return None ensures the lines after the except block are not executed in case of an error
    except Exception as error:
        print(f'Error opening image: {error}')
        return None
    
    image = resize(image, output_width)
    grey_image = greyscale(image)
    ascii_str = pixel_to_ascii(image, grey_image)

    # Formatting the ASCII string
    ascii_str = '\n'.join(ascii_str[i:i+output_width] for i in range(0, len(ascii_str), output_width))
    
    print(ascii_str)
    # Writes the .txt file
    #file_name = input('Making sure to include the .txt extension, \n Please enter a file name for the .txt file: ')
    #with open(file_name, 'w') as f:
    #    f.write(ascii_str)

image_path =input('Please enter the image path: ')
image_to_ascii(image_path)
