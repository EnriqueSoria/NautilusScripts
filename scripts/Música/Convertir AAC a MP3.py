#!/usr/bin/env python3
from shutil import move as mv
from os import remove as rm
from os import listdir as ls
from os import system as run
from os import path
from sys import exit

from multiprocessing import Pool

join=path.join

COMMAND = '''ffmpeg -i "{file}.aac" -acodec libmp3lame -ac 2 -b:a 192k "{file}.mp3"'''

def convert():
    filenames = [ COMMAND.format(file=file.replace('.aac', '')) for file in ls('.') ]
    with Pool(len(filenames)) as p:
        p.map(run, filenames)


def remove_aac():
    filenames = [ file for file in ls('.') if file.endswith('aac')]
    for file in filenames:
        rm( file )


def main():
    # TODO: check if conversion is OK
    #   a) ...by looking return code
    #   b) ...looking if mp3 is created
    convert()
    remove_aac()
            
            
    
    
if __name__=="__main__":
    main()




