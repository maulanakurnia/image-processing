import PySimpleGUI as sg
import os.path
from PIL import Image
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
        sg.Text("Main Feature :"),
    ],
    [
        sg.Button("Image Threshold", size=(20, 1), key="thresholdImage"),
    ],
    [
        sg.Button("Image Negative", size=(20, 1), key="negative_image"),
    ],
    [
        sg.Button("Image Brightness", size=(20, 1), key="imageBrightness"),
    ],
    [
        sg.Button("Image Rotating", size=(20, 1), key="rotateImage")
    ],
    [
        sg.Button("Image Flipping", size=(20, 1), key="imageFlipping"),
    ],
    [
        sg.Button("Image Zooming", size=(20, 1), key="zoomIn"),
    ],
    [
        sg.Button("Image Shringking", size=(20, 1), key="ZoomOut")
    ],
    [
        sg.Text("Additional Feature : ")
    ],
    [
        sg.Button("Image Logarithmic", size=(20, 1), key="imageLogarithmic"),
    ],
    [
        sg.Button("Translation", size=(20, 1), key="translateImage")
    ],
    [
        sg.Button("Image Blending", size=(20, 1), key="imageBlending"),
    ],
    [
        sg.In(size=(15, 1), enable_events=True, key="inputImage2", disabled=True),
        sg.FileBrowse(key="browseInputImage2", disabled=True),
    ],
    [
        sg.Text(text="Image Thresholde : ", key="textThresholde", visible=False),
        sg.Text(text="Image Brigness : ", key="textBrigness", visible=False),
        sg.Text(text="Image Zooming : ", key="textZooming", visible=False),
        sg.Text(text="Image Shrinking : ", key="textShrinking", visible=False),
        sg.Text(text="Image Rotating : ", key="textRotating", visible=False),
        sg.Text(text="Image Translation : ", key="textTranslation", visible=False),
        sg.Slider(range=(0, 360), orientation='h', size=(19, 20), default_value=0, visible=False, key="sliderRotate"), 
        sg.Slider(range=(0, 255), orientation='h', size=(19, 20), default_value=0, visible=False, key="sliderBrightness"), 
        sg.Slider(range=(0, 255), orientation='h', size=(19, 20), default_value=0, visible=False, key="sliderThreshold"),
        sg.Slider(range=(2, 4), orientation='h', size=(19, 20),  visible=False, key="sliderZoom"),
        sg.Text(text="Flipping: ", key="textFlipping", visible=False),
        sg.Button("Horizontal", size=(20, 1), key="Horizontal", visible=False),
        sg.Button("Vertical", size=(20, 1), key="Vertical", visible=False),
        sg.Button("Vertical Horizontal", size=(20, 1), key="VerticalHorizontal", visible=False),
        sg.Text(text="x value:", visible=False, key="textTranslateX"),
        sg.In(default_text=0, size=(9, 1),enable_events=True, visible=False, key="inputXImage"),
        sg.Text(text="y value:", visible=False, key="textTranslateY"),
        sg.In(default_text=0, size=(9, 1),enable_events=True, visible=False, key="inputYImage"),
        sg.Button("OK", size=(20, 1), key="submitValueDeg", visible=False), 
        sg.Button("OK", size=(20, 1), key="submitBrightness", visible=False), 
        sg.Button("OK", size=(20, 1), key="submitThreshold", visible=False),
        sg.Button("OK", size=(20, 1), key="submitZoomOut", visible=False),
        sg.Button("OK", size=(20, 1), key="submitZoomIn", visible=False),
        sg.Button("OK", size=(20, 1), key="submitTranslation", visible=False),
        sg.Button("OK", size=(20, 1), key="submitBlending", visible=False),
    ],
    [
        sg.Button("CANCEL", size=(20,1), key="cancel", visible=False)
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

    elif event == "negative_image":
        try:
            window["cancel"].update(visible=True)
            window["textThresholde"].update(visible=False)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["ImgOutputViewer"].update(filename=filename_out)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["sliderZoom"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)

            window["typeProcessing"].update("Image Negative")
            img_output = negative(img_input, coldepth)
            img_output.save(filename_out)
        except:
            pass

    elif event == "rotateImage":
        try:
            window["cancel"].update(visible=True)
            window["typeProcessing"].update("Image Rotate")
            window["textThresholde"].update(visible=False)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=True)
            window["textTranslation"].update(visible=False)
            window["sliderRotate"].update(visible=True)
            window["submitValueDeg"].update(visible=True)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["sliderZoom"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
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

    elif event == "imageFlipping":
        try:
            window["cancel"].update(visible=True)
            window["textFlipping"].update(visible=True)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["Horizontal"].update(visible=True)
            window["Vertical"].update(visible=True)
            window["textThresholde"].update(visible=False)
            window["VerticalHorizontal"].update(visible=True)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderZoom"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
        except:
            pass

    elif event == "thresholdImage":
        try:
            window["cancel"].update(visible=True)
            window["textThresholde"].update(visible=True)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderThreshold"].update(visible=True)
            window["submitThreshold"].update(visible=True)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderZoom"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
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
            window["cancel"].update(visible=True)
            window["textThresholde"].update(visible=False)
            window["textBrigness"].update(visible=True)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderBrightness"].update(visible=True)
            window["submitBrightness"].update(visible=True)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["sliderZoom"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
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
            window["cancel"].update(visible=True)
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
            window["cancel"].update(visible=True)
            flip = "vertical"
            window["typeProcessing"].update("Image Flipping Vertical")
            img_output = flipping(img_input, coldepth, flip)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Horizontal":
        try:
            window["cancel"].update(visible=True)
            flip = "horizontal"
            window["typeProcessing"].update("Image Flipping Horizontal")
            img_output = flipping(img_input, coldepth, flip)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "VerticalHorizontal":
        try:
            window["cancel"].update(visible=True)
            flip = "ver-hor"
            window["typeProcessing"].update("Image Flipping Vertical Horizontal")
            img_output = flipping(img_input, coldepth, flip)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ZoomOut":
        try:
            window["cancel"].update(visible=True)
            window["textThresholde"].update(visible=False)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=True)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["sliderZoom"].update(visible=True)
            window["submitZoomOut"].update(visible=True)
            window["submitZoomIn"].update(visible=False)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
        except:
            pass

    elif event == "submitZoomOut":
        try:
            ScaleFactor = int(values["sliderZoom"])
            window["typeProcessing"].update("Zoom Out")
            img_output = zooming(img_input, coldepth, ScaleFactor, 'out')
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "zoomIn":
        try:
            window["cancel"].update(visible=True)
            window["textThresholde"].update(visible=False)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=True)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["sliderZoom"].update(visible=True)
            window["submitZoomIn"].update(visible=True)
            window["submitZoomOut"].update(visible=False)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
        except:
            pass
    
    elif event == "submitZoomIn":
        try:
            scaleFactor = int(values["sliderZoom"])
            window["typeProcessing"].update("Zoom In")
            img_output = zooming(img_input, coldepth, scaleFactor, 'in')
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "imageBlending":
        try:
            window["cancel"].update(visible=True)
            window["textThresholde"].update(visible=False)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["sliderZoom"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["inputImage2"].update(disabled=False)
            window["browseInputImage2"].update(disabled=False)
            window["submitBlending"].update(visible=True)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
        except:
            pass

    elif event == "submitBlending":
        try:
            filename = values['inputImage2']
            img_input2 = Image.open(filename)

            window["typeProcessing"].update("Image Blending")
            img_output = blending(img_input, img_input2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "translateImage":
        try:
            window["cancel"].update(visible=True)
            window["textThresholde"].update(visible=False)
            window["textBrigness"].update(visible=False)
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=True)
            window["sliderZoom"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textTranslateX"].update(visible=True)
            window["inputXImage"].update(visible=True)
            window["textTranslateY"].update(visible=True)
            window["inputYImage"].update(visible=True)
            window["submitTranslation"].update(visible=True)
        except:
            pass

    elif event == "submitTranslation":
        try:
            x = int(values["inputXImage"])
            y = int(values["inputYImage"])
            shift = [x,y]
            window["typeProcessing"].update("Translation")
            output_image = translation(img_input, coldepth, shift)
            output_image.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "cancel":
        try:
            window["cancel"].update(visible=False)
            window["typeProcessing"].update("")
            window["textZooming"].update(visible=False)
            window["textShrinking"].update(visible=False)
            window["textThresholde"].update(visible=False)
            window["textRotating"].update(visible=False)
            window["textTranslation"].update(visible=False)
            window["textBrigness"].update(visible=False)
            window["textFlipping"].update(visible=False)
            window["Horizontal"].update(visible=False)
            window["Vertical"].update(visible=False)
            window["VerticalHorizontal"].update(visible=False)
            window["sliderRotate"].update(visible=False)
            window["submitValueDeg"].update(visible=False)
            window["sliderBrightness"].update(visible=False)
            window["submitBrightness"].update(visible=False)
            window["sliderThreshold"].update(visible=False)
            window["submitThreshold"].update(visible=False)
            window["sliderZoom"].update(visible=False)
            window["submitZoomOut"].update(visible=False)
            window["submitZoomIn"].update(visible=False)
            window["submitBlending"].update(visible=False)
            window["inputImage2"].update(disabled=True)
            window["browseInputImage2"].update(disabled=True)
            window["textTranslateX"].update(visible=False)
            window["inputXImage"].update(visible=False)
            window["textTranslateY"].update(visible=False)
            window["inputYImage"].update(visible=False)
            window["submitTranslation"].update(visible=False)
            img_output = img_input
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass