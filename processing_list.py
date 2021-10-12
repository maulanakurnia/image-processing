from PIL import Image, ImageOps, ImageDraw
import math
from math import sin, cos, pi, radians

def negative(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


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

def threshold(img_input, coldepth, val):
    if coldepth != 25:
        img_input = img_input.convert('RGB')
        T = val
        img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
        pixels = img_output.load()
        #bg_r,bg_g, bg_b = pixels[0,0]

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if r and g and b < T:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def brightness(img_input, coldepth, val):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        bright = val
        img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
        pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (bright+r, bright+g, bright+b)
            if pixels[i, j] > (255, 255, 255):
                pixels[i, j] = (255, 255, 255)
            elif pixels[i, j] < (0, 0, 0):
                pixels[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def logarithmic(img_input, coldepth):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        C = 40
        img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
        pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            #pixels[i, j] = (C * math.log(1+r),C * math.log(1+g),C * math.log(1+b))
            #pixels[i, j] = (C*r, C*g, C*b)
            pixels[i, j] = (int(C*math.log(1+r)),
                            int(C*math.log(1+g)), int(C*math.log(1+b)))
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def flipping(img_input, coldepth, flip):

    if coldepth != 25:
        img_input = img_input.convert('RGB')

        img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
        pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if flip == "vertical":
                r, g, b = img_input.getpixel((i, img_input.size[1] - 1 - j))
            elif flip == "horizontal":
                r, g, b = img_input.getpixel((img_input.size[0] - 1 - i, j))
            elif flip == "ver-hor":
                r, g, b = img_input.getpixel((img_input.size[0] - 1 - i, img_input.size[1] - 1 -  j))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def zoomOut(img_input, coldepth, ScaleFactor):
    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    if ScaleFactor == 2:
        n = 2
        img_output = Image.new('RGB', (int(img_input.size[0]/n), int(img_input.size[1]/n)))
        pixels = img_output.load()
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                r, g, b = img_input.getpixel((i*n, j*n))
                pixels[i, j] = (r, g, b)
    elif ScaleFactor == 3:
        n = 3
        img_output = Image.new('RGB', (int(img_input.size[0]/n), int(img_input.size[1]/n)))
        pixels = img_output.load()
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                r, g, b = img_input.getpixel((i*n, j*n))
                pixels[i, j] = (r, g, b)
    elif ScaleFactor == 4:
        n = 4
        img_output = Image.new('RGB', (int(img_input.size[0]/n), int(img_input.size[1]/n)))
        pixels = img_output.load()
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                r, g, b = img_input.getpixel((i*n, j*n))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

def zoomIn(img_input, coldepth, ScaleFactor):
    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    if ScaleFactor == 2:
        n = 2
        img_output = Image.new('RGB', (img_input.size[0]*n, img_input.size[1]*n))
        pixels = img_output.load()
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                r, g, b = img_input.getpixel((int(i/n), int(j/n)))
                pixels[i, j] = (r, g, b)
    elif ScaleFactor == 3:
        n = 3
        img_output = Image.new('RGB', (img_input.size[0]*n, img_input.size[1]*n))
        pixels = img_output.load()
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                r, g, b = img_input.getpixel((int(i/n), int(j/n)))
                pixels[i, j] = (r, g, b)
    elif ScaleFactor == 4:
        n = 4
        img_output = Image.new('RGB', (img_input.size[0]*n, img_input.size[1]*n))
        pixels = img_output.load()
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                r, g, b = img_input.getpixel((int(i/n), int(j/n)))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output