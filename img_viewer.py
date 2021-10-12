import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from PySimpleGUI.PySimpleGUI import Cancel, Slider
from processing_list import *

sg.theme('DefaultNoMoreNagging')
file_list_column = [
    [
        sg.Text("Open Image Folder :"),
    ],
    [
        sg.In(size=(20, 1), enable_events=True, key="folderImage"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Choose an image from list :"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(25, 10), key="listImage"
        )
    ],
    [
        sg.Text("Image Information:"),
    ],
    [
        sg.Text(size=(20, 1), key="imageSize"),
    ],
    [
        sg.Text(size=(20, 1), key="imageColorDepth"),
    ],
]

image_viewer_column = [
    [
        sg.Text("Image Input :")
    ],
    [
        sg.Text(size=(40, 1), key="FilepathImgInput")
    ],
    [
        sg.Image(key="ImgInputViewer")
    ],
]

list_processing = [
    [
        sg.Text("List of Processing:"),
    ],
    [
        sg.Button("Image Negative", size=(20, 1), key="negativeImage"),
    ],
    [
        sg.Button("Image Threshold", size=(20, 1), key="thresholdImage"),
    ],
    [
        sg.Button("Image Brightness", size=(20, 1), key="imageBrightness"),
    ],
    [
        sg.Button("Image Logarithmic", size=(20, 1), key="imageLogarithmic"),
    ],
    [
        sg.Text("Image Flip: "),
    ],
    [
        sg.Button("Horizontal", size=(9, 1), key="Horizontal"),
        sg.Button("Vertical", size=(9, 1), key="Vertical")
    ],
    [
        sg.Button("Vertical Horizontal", size=(20, 1), key="VerticalHorizontal")
    ],
    [
        sg.Text("Image Rotate : ")
    ],
    [
        sg.Button("rotateImage", size=(20, 1), key="rotateImage")
    ],
    [
        sg.Text("Image Scalling: ")
    ],
    [
        sg.Button("Zoom In", size=(9, 1), key="zoomIn"),
        sg.Button("Zoom Out", size=(9, 1), key="ZoomOut")
    ],
    [
        sg.Slider(range=(0, 360), orientation='h', size=(19, 20), default_value=0, visible=False, key="sliderRotate"), 
        sg.Slider(range=(0, 255), orientation='h', size=(19, 20), default_value=0, visible=False, key="sliderBrightness"), 
        sg.Slider(range=(0, 255), orientation='h', size=(19, 20), default_value=0, visible=False, key="sliderThreshold"),
        sg.Slider(range=(2, 4), orientation='h', size=(19, 20),  visible=False, key="sliderZoom")
    ],
    [
        sg.Button("OK", size=(2, 1), key="submitValueDeg", visible=False), 
        sg.Button("OK", size=(2, 1), key="submitBrightness", visible=False), 
        sg.Button("OK", size=(2, 1), key="submitThreshold", visible=False),
        sg.Button("OK", size=(2, 1), key="submitZoom", visible=False),
        sg.Button("OK", size=(2, 1), key="submitZoomIn", visible=False)
    ],
    [
        sg.Button("CANCEL", size=(20,1), key="cancel")
    ]
]

val=0
image_viewer_column2 = [
    [sg.Text("Image Processing Output:")],
    [sg.Text(size=(40, 1), key="typeProcessing")],
    [sg.Image(key="ImgOutputViewer")],
]


layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeperator(),
        sg.Column(list_processing),
        sg.VSeperator(),
        sg.Column(image_viewer_column2),
    ]
]

window = sg.Window("Mini Image Editor", layout)
filename_out = "output.png"

while True:
    event, values = window.read()
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "folderImage":
        folder = values["folderImage"]

        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fname = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]

        window["listImage"].update(fname)

    elif event == "listImage":

        try:
            filename = os.path.join(
                values["folderImage"], values["listImage"][0]
            )
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)
            window["typeProcessing"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)

            img_width, img_height = img_input.size
            window["imageSize"].update(
                "Image Size : "+str(img_width)+" x "+str(img_height))

            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32,
                                "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
            coldepth = mode_to_coldepth[img_input.mode]
            window["imageColorDepth"].update("Color Depth : "+str(coldepth))
        except:
            pass

    elif event == "negativeImage":

        try:
            window["typeProcessing"].update("Image Negative")
            img_output = negative(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)

            window["submitZoomIn"].update(visible=False)
        except:
            pass

    elif event == "rotateImage":
        try:
            window["typeProcessing"].update("Image Rotate")

            window["sliderRotate"].update(visible=True)
            window["submitValueDeg"].update(visible=True)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)

            window["submitZoomIn"].update(visible=False)
        except:
            pass
    elif event == "submitValueDeg":
        try:
            val= int(values["sliderRotate"])
            window["typeProcessing"].update("Image Rotate")
            img_output = rotate(img_input, coldepth, val)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "thresholdImage":

        try:
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderThreshold"].update(visible=True)
            window["submitThreshold"].update(visible=True)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)

            window["submitZoomIn"].update(visible=False)
        except:
            pass
    
    elif event == "submitThreshold":
        try:
            val= int(values["sliderThreshold"])
            window["typeProcessing"].update("Image Brightness")
            img_output = threshold(img_input, coldepth, val)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "imageBrightness":
        
        try:
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=True)
            window["submitBrightness"].update(visible=True)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)

            window["submitZoomIn"].update(visible=False)
        except:
            pass

    elif event == "submitBrightness":
        try:
            val= int(values["sliderBrightness"])
            window["typeProcessing"].update("Image Brightness")
            img_output = brightness(img_input, coldepth, val)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass


    elif event == "imageLogarithmic":

        try:
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["typeProcessing"].update("Image logarithmic")
            img_output = logarithmic(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "Vertical":
        try:
            flip = "vertical"
            window["typeProcessing"].update("Image Flipping Vertical")
            img_output = flipping(img_input, coldepth, flip)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)

            window["submitZoomIn"].update(visible=False)
        except:
            pass

    elif event == "Horizontal":
        try:
            flip = "horizontal"
            window["typeProcessing"].update("Image Flipping Horizontal")
            img_output = flipping(img_input, coldepth, flip)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)

            window["submitZoomIn"].update(visible=False)
        except:
            pass
    
    elif event == "VerticalHorizontal":
        try:
            flip = "ver-hor"
            window["typeProcessing"].update("Image Flipping Vertical Horizontal")
            img_output = flipping(img_input, coldepth, flip)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)

            window["submitZoomIn"].update(visible=False)
        except:
            pass

    elif event == "ZoomOut":
        try:
            window["sliderZoom"].update(visible=True)
            window["submitZoom"].update(visible=True)

            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
        except:
            pass

    elif event == "submitZoom":
        try:
            ScaleFactor = int(values["sliderZoom"])
            window["typeProcessing"].update("Zoom Out")
            img_output = zoomOut(img_input, coldepth, ScaleFactor)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "zoomIn":
        try:
            window["sliderZoom"].update(visible=True)
            window["submitZoomIn"].update(visible=True)

            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)

            window["submitZoom"].update(visible=False)
        except:
            pass
    
    elif event == "submitZoomIn":
        try:
            ScaleFactor = int(values["sliderZoom"])
            window["typeProcessing"].update("Zoom Out")
            img_output = zoomIn(img_input, coldepth, ScaleFactor)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "cancel":
        try:
            window["typeProcessing"].update("")
            img_output = img_input
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)

            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)

            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)

            window["sliderZoom"].update(visible=False)
            window["submitZoom"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
        except:
            pass