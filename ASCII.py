from PIL import Image
# String ordered according to how dense the character is
ASCII_characters = ' .:co?9W#'

def resize(image, new_width=148):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.42)

    return image.resize((new_width, new_height))

def greyscale(image):
    return image.convert('L')

def color_diff(pixel1, pixel2):
    diff = ((pixel1[0]-pixel2[0])**2+(pixel1[1]-pixel2[1])**2+(pixel1[2]-pixel2[2])**2)**(1/2)
    return diff
    
def assign_border(square):
    if color_diff(square[0], square[3])>30 and color_diff(square[0], square[1])<30 and color_diff(square[0], square[2])<30:
        return '/'
    elif color_diff(square[1], square[2])>30 and color_diff(square[0], square[1])<30 and color_diff(square[3], square[1])<30:
        return '\\'
    elif color_diff(square[0], square[2])>30 and color_diff(square[0], square[1])<30 and color_diff(square[3], square[2])<30:
        return '-'
    elif color_diff(square[0], square[1])>30 and color_diff(square[0], square[2])<30 and color_diff(square[3], square[1])<30:
        return '|'
    else:
        return ' '
    
def square_to_border(image):
    pixels = image.getdata()
    border_list = []
    print(list(pixels))
    for i in range(image.size[0]*image.size[1]//4):
        border_list.append(assign_border([pixels[i*2], pixels[1+i*2], pixels[image.size[0]//2+i*2], pixels[1+image.size[0]//2+i*2]]))
    #print(border_list)
    return border_list
    
def pixel_to_ascii(image):
    pixels = image.getdata()
    # getdata() returns a list with values for each starting from the top left pixel and going right and then down
    ascii_str = ''.join(ASCII_characters[pixel // 30] for pixel in pixels) 
    # Maps to ASCII depending upon how high the value is
    return ascii_str

def image_to_ascii(image_path, output_width=148):
    try:
        image = Image.open(image_path)
    # return None ensures the lines after the except block are not executed in case of an error
    except Exception as error:
        print(f'Error opening image: {error}')
        return None
    
    image = resize(image, output_width*2)
    border_list = square_to_border(image)
    #print(border_list)
    image = resize(image, output_width)
    image = greyscale(image)
    ascii_str = pixel_to_ascii(image)
    
    ascii_list = list(ascii_str)
    
    ascii_str = ''
    for i in range(len(ascii_list)):
        try:
            if border_list[i] == ' ':
                ascii_str+=ascii_list[i]
            else:
                ascii_str+=border_list[i]
        except IndexError:    
            ascii_str+=ascii_list[i]
            
    # Formatting the ASCII string
    ascii_str = '\n'.join(ascii_str[i:i+output_width] for i in range(0, len(ascii_str), output_width))
    
    print(ascii_str)
    # Writes the .txt file
    #file_name = input('Making sure to include the .txt extension, \n Please enter a file name for the .txt file: ')
    #    f.write(ascii_str)

image_path = 'half.png'#input('Please enter the image path: ')
image_to_ascii(image_path)
