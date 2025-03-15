from PIL import Image

ASCII_characters = ' ..::!ilkUQRZW$&#@'

def resize(image, new_width=149):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.42)

    return image.resize((new_width, new_height))

def greyscale(image):
    return image.convert('L')

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join(ASCII_characters[pixel // 15] for pixel in pixels) 
        #Maps to ASCII
    return ascii_str

def image_to_ascii(image_path, output_width=149):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f'Error opening image: {e}')
        return

    image = resize(image, output_width)
    image = greyscale(image)
    ascii_str = pixel_to_ascii(image)

    #Format the ASCII string
    ascii_str = '\n'.join(ascii_str[i:i+output_width] for i in range(0, len(ascii_str), output_width))

    print(ascii_str)

#    with open('ascii_art.txt', 'w') as f:
#        f.write(ascii_str)

image_path = input()
image_to_ascii(image_path)
