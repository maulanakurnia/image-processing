import PySimpleGUI as sg

sg.theme("DefaultNoMoreNagging")
file_list_column = [
    [sg.Text("Open Image Folder :")],
    [sg.In(size=(20, 1), enable_events=True, key="folder_images"),
     sg.FolderBrowse()],
    [sg.Text("Choose an image from list : ")],
    [sg.Listbox(values=[], size=(25, 10),
                key="list_image", enable_events=True)],

    [sg.Text("Image Information : ")],
    [sg.Text(size=(20, 1),
             key="image_size")],
    [sg.Text(size=(20, 1),
             key="image_color_depth")],
]

input_image_preview = [
    [sg.Text("Image Input :")],
    [sg.Text(size=(40, 1), key="image_path")],
    [sg.Image(key="preview_input_image")],
]
list_processing = [
    [sg.Text("Main Feature : ")],
    [sg.Button("Image Thresholding", size=(20, 1), key="image_thresholding")],
    [sg.Button("Image Negative", size=(20, 1), key="image_negative")],
    [sg.Button("Image Brightness", size=(20, 1), key="image_brigtness")],
    [sg.Button("Image Rotating", size=(20, 1), key="image_rotating")],
    [sg.Button("Image Flipping", size=(20, 1), key="image_flipping")],
    [sg.Button("Image Zooming", size=(20, 1), key="image_zooming")],
    [sg.Button("Image Shringking", size=(20, 1), key="image_shringking")],

    [sg.HSeparator()],

    [sg.Text("Additional Feature : ")],
    [sg.Button("Image Logarithmic", size=(20, 1), key="image_logarithmic")],
    [sg.Button("Image Translation", size=(20, 1), key="image_translation")],
    [sg.Button("Image Blending", size=(20, 1), key="image_blending")],
    [
        sg.In(size=(15, 1), enable_events=True,
              key="input_image_2", disabled=True),
        sg.FileBrowse(key="browse_input_image_2", disabled=True)
    ],

    [sg.HSeparator()],
    [sg.Text("Filter : ")],

    [sg.Button("Media Filter", size=(20, 1), key="image_blur")],
    
    [sg.HSeparator()],
    [
        # TEXT LABEL
        sg.Text("Image Thresholding : ",
                key="text_thresholding", visible=False),
        sg.Text("Image Brightness : ", key="text_brightness", visible=False),
        sg.Text("Image Rotating : ", key="text_rotating", visible=False),
        sg.Text("Image Flipping : ", key="text_flipping", visible=False),
        sg.Text("Image Zooming : ", key="text_zooming", visible=False),
        sg.Text("Image Shringking : ", key="text_shringking", visible=False),
        sg.Text("Image Translation : ", key="text_translation", visible=False),
        sg.Text("x value:", visible=False, key="text_translate_x"),
        sg.Text("y value:", visible=False, key="text_translate_y"),

        # Input
        sg.In(default_text=0, size=(9, 1),
              visible=False, key="input_x_translation"),
        sg.In(default_text=0, size=(9, 1),
              visible=False, key="input_y_translation"),

        # Slider
        sg.Slider(range=(0, 260), size=(19, 20),
                  orientation='h',
                  key="slider_thresholding",
                  default_value=0, visible=False),
        sg.Slider(range=(0, 255), size=(19, 20),
                  orientation='h',
                  key="slider_brightness",
                  default_value=0, visible=False),
        sg.Slider(range=(0, 360), size=(19, 20),
                  orientation='h',
                  key="slider_rotating",
                  default_value=0, visible=False),
        sg.Slider(range=(2, 4), size=(19, 20),
                  orientation='h',
                  key="slider_zooming", visible=False),
        sg.Slider(range=(2, 4), size=(19, 20),
                  orientation='h',
                  key="slider_shringking", visible=False),

        # Button
        sg.Button("Horizontal", size=(20, 1),
                  key="submit_horizontal", visible=False),
        sg.Button("Vertical", size=(20, 1),
                  key="submit_vertical", visible=False),
        sg.Button("Vertical Horizontal", size=(20, 1),
                  key="submit_vertical_horizontal", visible=False),

        sg.Button("Apply", size=(20, 1),
                  key="submit_thresholding", visible=False),
        sg.Button("Apply", size=(20, 1),
                  key="submit_brightness", visible=False),
        sg.Button("Apply", size=(20, 1), key="submit_rotating", visible=False),
        sg.Button("Apply", size=(20, 1), key="submit_zooming", visible=False),
        sg.Button("Apply", size=(20, 1),
                  key="submit_shringking", visible=False),
        sg.Button("Apply", size=(20, 1), key="submit_blending", visible=False),
        sg.Button("Apply", size=(20, 1),
                  key="submit_translation", visible=False),
    ],
    [sg.Button("Cancel", size=(20, 1), key="cancel", visible=False)]
]

output_image_preview = [
    [sg.Text("Image Output:")],
    [sg.Text(size=(40, 1), key="type_processing")],
    [sg.Image(key="preview_output_image")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(input_image_preview),
        sg.VSeperator(),
        sg.Column(list_processing),
        sg.VSeperator(),
        sg.Column(output_image_preview),
    ]
]

window = sg.Window("Mini Image Editor", layout)
filename_out = "output.png"
