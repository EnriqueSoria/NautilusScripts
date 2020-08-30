#!/usr/bin/env python3


from PIL import Image
from os import getenv
from os import listdir as ls
from os import remove as rm

def convert_to_jpg(filename):
    original = Image.open(filename)
    original = original.convert('RGB')
    original.save(filename.replace(filename.split('.')[-1], 'jpg'), "JPEG")


for filename in getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS','').splitlines():
    if filename.endswith(('.png', '.jpeg')):
        convert_to_jpg(filename)
        rm(filename)

