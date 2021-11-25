from layouting import *
import os.path
from PIL import Image
from processing_list import *

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "folder_images":
        folder = values["folder_images"]

        try:
            list_file = os.listdir(folder)
        except:
            list_file = []

        file_name = [
            f
            for f in list_file
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["list_image"].update(file_name)

    if event == "list_image":
        try:
            filename = os.path.join(values["folder_images"],
                                    values["list_image"][0])
            window["image_path"].update(filename)
            window["preview_input_image"].update(filename)
            window["type_processing"].update(filename)
            window["preview_output_image"].update(filename)

            input_image = Image.open(filename)
            image_width, image_height = input_image.size
            window["image_size"].update(
                "Image Size : "+str(image_width)+" x "+str(image_height))

            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32,
                                "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
            color_depth = mode_to_coldepth[input_image.mode]
            window["image_color_depth"].update(
                "Color Depth : "+str(color_depth))
        except:
            pass

    elif event == "image_thresholding":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Thresholding")
            # Thresholding
            window["text_thresholding"].update(visible=True)
            window["slider_thresholding"].update(visible=True)
            window["submit_thresholding"].update(visible=True)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass

    elif event == "image_negative":
        try:
            window["cancel"].update(visible=True)
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)

            window["type_processing"].update("Image Negative")
            output_image = negative(input_image, color_depth)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "image_brigtness":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Brigtness")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=True)
            window["slider_brightness"].update(visible=True)
            window["submit_brightness"].update(visible=True)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass

    elif event == "image_rotating":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Negative")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=True)
            window["slider_rotating"].update(visible=True)
            window["submit_rotating"].update(visible=True)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass

    elif event == "image_flipping":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Negative")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=True)
            window["submit_horizontal"].update(visible=True)
            window["submit_vertical"].update(visible=True)
            window["submit_vertical_horizontal"].update(visible=True)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass

    elif event == "image_zooming":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Negative")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=True)
            window["slider_zooming"].update(visible=True)
            window["submit_zooming"].update(visible=True)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass

    elif event == "image_shringking":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Shringking")
            # Shringking
            window["text_shringking"].update(visible=True)
            window["slider_shringking"].update(visible=True)
            window["submit_shringking"].update(visible=True)
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass

    elif event == "image_blending":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Negative")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=True)
            window["input_image_2"].update(disabled=False)
            window["browse_input_image_2"].update(disabled=False)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass

    elif event == "image_logarithmic":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Logaritmic")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)

            output_image = logarithmic(input_image, color_depth)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "image_translation":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Logaritmic")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=True)
            window["text_translate_x"].update(visible=True)
            window["input_x_translation"].update(visible=True)
            window["text_translate_y"].update(visible=True)
            window["input_y_translation"].update(visible=True)
            window["submit_translation"].update(visible=True)
        except:
            pass

    elif event == "median_filter":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Median Filter")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)

            output_image = median_filter(input_image, color_depth)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "mean_filter":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Mean Filter")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # Blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)

            output_image = blur(input_image, color_depth)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_thresholding":
        try:
            value = int(values["slider_thresholding"])
            output_image = thresholding(input_image, color_depth, value)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_brightness":
        try:
            value = int(values["slider_brightness"])
            window["type_processing"].update("Image Brightness")
            output_image = brightness(input_image, color_depth, value)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_rotating":
        try:
            deg = int(values["slider_rotating"])
            output_image = rotating(input_image, color_depth, deg)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass
    elif event == "submit_horizontal":
        try:
            type = "horizontal"
            window["type_processing"].update("Image Flipping Horizontal")
            output_image = flipping(input_image, color_depth, type)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_vertical":
        try:
            type = "vertical"
            window["type_processing"].update("Image Flipping Vertical")
            output_image = flipping(input_image, color_depth, type)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_vertical_horizontal":
        try:
            type = "vertical_herizontal"
            window["type_processing"].update(
                "Image Flipping Vertical Horizontal")
            output_image = flipping(input_image, color_depth, type)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_zooming":
        try:
            scale = int(values["slider_zooming"])
            window["type_processing"].update("Zoom In")
            output_image = zooming(input_image, color_depth, scale)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_shringking":
        try:
            scale = int(values["slider_shringking"])
            window["type_processing"].update("Image Shringking")
            output_image = shringking(input_image, color_depth, scale)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_blending":
        try:
            filename = values['input_image_2']
            input_image2 = Image.open(filename)

            window["type_processing"].update("Image Blending")
            output_image = blending(input_image, input_image2, color_depth)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_translation":
        try:
            x = int(values["input_x_translation"])
            y = int(values["input_y_translation"])
            shift = [x, y]
            window["type_processing"].update("Image Translation")
            output_image = translation(input_image, color_depth, shift)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "cancel":
        try:
            output_image = input_image
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)

            window["cancel"].update(visible=False)
            window["type_processing"].update("")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)
            # Rotating
            window["text_rotating"].update(visible=False)
            window["slider_rotating"].update(visible=False)
            window["submit_rotating"].update(visible=False)
            # Flipping
            window["text_flipping"].update(visible=False)
            window["submit_horizontal"].update(visible=False)
            window["submit_vertical"].update(visible=False)
            window["submit_vertical_horizontal"].update(visible=False)
            # Zooming
            window["text_zooming"].update(visible=False)
            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)
            # Shringking
            window["text_shringking"].update(visible=False)
            window["slider_shringking"].update(visible=False)
            window["submit_shringking"].update(visible=False)
            # submit blending
            window["submit_blending"].update(visible=False)
            window["input_image_2"].update(disabled=True)
            window["browse_input_image_2"].update(disabled=True)
            # Translation
            window["text_translation"].update(visible=False)
            window["text_translate_x"].update(visible=False)
            window["input_x_translation"].update(visible=False)
            window["text_translate_y"].update(visible=False)
            window["input_y_translation"].update(visible=False)
            window["submit_translation"].update(visible=False)
        except:
            pass
