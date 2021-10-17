from PIL import Image, ImageDraw
import math
from math import sin, cos, radians

# MAIN FEATURE
def threshold(input_image, coldepth, val):
    if coldepth != 25:
        input_image = input_image.convert('RGB')
        T = val
        output_image = Image.new('RGB', (input_image.size[0], input_image.size[1]))
        pixels = output_image.load()

    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            r, g, b = input_image.getpixel((i, j))
            if r and g and b < T:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

def negative(input_image, coldepth):
    if coldepth != 24:
        input_image = input_image.convert('RGB')

    output_image = Image.new('RGB', (input_image.size[0], input_image.size[1]))
    pixels = output_image.load()
    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            r, g, b = input_image.getpixel((i, j))
            pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

def brightness(input_image, coldepth, val):
    if coldepth != 25:
        input_image = input_image.convert('RGB')
        bright = val
        output_image = Image.new('RGB', (input_image.size[0], input_image.size[1]))
        pixels = output_image.load()
    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            r, g, b = input_image.getpixel((i, j))
            pixels[i, j] = (bright+r, bright+g, bright+b)
            if pixels[i, j] > (255, 255, 255):
                pixels[i, j] = (255, 255, 255)
            elif pixels[i, j] < (0, 0, 0):
                pixels[i, j] = (0, 0, 0)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

def rotate(input_image, coldepth, deg):
    if coldepth != 25:
        input_image = input_image.convert('RGB')

    # Load Image
    input_pixels = input_image.load()

    # create output image
    output_image = Image.new('RGB', input_image.size)
    draw = ImageDraw.Draw(output_image)

    angle = radians(deg)
    center_x = input_image.width / 2
    center_y = input_image.height / 2

    # Copy Pixels
    for x in range(input_image.width):
        for y in range(input_image.height):
            xp = int((x - center_x) * cos(angle) - (y - center_y) * sin(angle) + center_x)
            yp = int((x - center_x) * sin(angle) + (y - center_y) * cos(angle) + center_y)
            if 0 <= xp < input_image.width and 0 <= yp < input_image.height:
                draw.point((x, y), input_pixels[xp, yp])
    return output_image

def flipping(input_image, coldepth, flip):
    if coldepth != 25:
        input_image = input_image.convert('RGB')
        output_image = Image.new('RGB', (input_image.size[1], input_image.size[0]))
        pixels = output_image.load()
    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            if flip == "vertical":
                r, g, b = input_image.getpixel((i, input_image.size[1] - 1 - j))
            elif flip == "horizontal":
                r, g, b = input_image.getpixel((input_image.size[0] - 1 - i, j))
            elif flip == "ver-hor":
                r, g, b = input_image.getpixel((input_image.size[0] - 1 - i, input_image.size[1] - 1 -  j))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

# Zoom In & Zoom Out (Shinkring)
def zooming(input_image, coldepth, scale, type):
    if coldepth != 24:
        input_image = input_image.convert('RGB')

    if type == 'in':
        output_image = Image.new('RGB', (input_image.size[0]*scale, input_image.size[1]*scale))
        pixels = output_image.load()
        for i in range(output_image.size[0]):
            for j in range(output_image.size[1]):
                r, g, b = input_image.getpixel((int(i/scale), int(j/scale)))
                pixels[i, j] = (r, g, b)
    else:
        output_image = Image.new('RGB', (int(input_image.size[0]/scale), int(input_image.size[1]/scale)))
        pixels = output_image.load()
        for i in range(output_image.size[0]):
            for j in range(output_image.size[1]):
                r, g, b = input_image.getpixel((i*scale, j*scale))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

# ADDITIONAL FEATURE
def blending(input_image_1, input_image_2, coldepth):
    if coldepth != 25:
        input_image_1 = input_image_1.convert('RGB')
        input_pixels_1 = input_image_1.load()
        
        input_image_2 = input_image_2.convert('RGB')
        input_pixels_2 = input_image_2.load()

        output_image = Image.new("RGB", (input_image_1.size[0], input_image_1.size[1]))
        output_pixels = output_image.load()

    for x in range(input_image_1.size[0]):
        for y in range(input_image_1.size[1]):
            r = input_pixels_1[x,y][0] - input_pixels_2[x,y][0]
            g = input_pixels_1[x,y][1] - input_pixels_2[x,y][1]
            b = input_pixels_1[x,y][2] - input_pixels_2[x,y][2]
            output_pixels[x,y] = (r,g,b)

            # jika terdapat perbedaan antara pixel 1 & pixel 2,
            # gunakan pixel 2
            if(r > 0 or g > 0 or b >0):
                output_pixels[x,y] = input_pixels_2[x,y]

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")
        
    return output_image


def logarithmic(input_image, coldepth):
    if coldepth != 25:
        input_image = input_image.convert('RGB')
        C = 40
        output_image = Image.new('RGB', (input_image.size[0], input_image.size[1]))
        pixels = output_image.load()
    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            r, g, b = input_image.getpixel((i, j))
            pixels[i, j] = (int(C*math.log(1+r)),
                            int(C*math.log(1+g)), 
                            int(C*math.log(1+b)))
    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image

def translation(input_image, coldepth, shift):
    if coldepth != 25:
        input_image = input_image.convert("RGB")
        input_pixels = input_image.load()

        output_image = Image.new('RGB', (input_image.size[1], input_image.size[0]))
        output_pixels = output_image.load()

    start_m = shift[0]
    start_n = shift[1]

    if shift[0] < 0:
        start_m = 0
    if shift[1] < 0:
        start_n = 0

    for x in range(start_m, input_image.size[0]):
        for y in range(start_n, input_image.size[1]):
            new_x = x - shift[0]
            new_y = y - shift[1]

            if(new_x >= input_image.size[0] or new_y >= input_image.size[1] or new_x < 0 or new_y < 0):
                output_pixels[x,y] = (0,0,0)
            else:
                output_pixels[x,y] = input_pixels[new_x, new_y]

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")
        
    return output_image