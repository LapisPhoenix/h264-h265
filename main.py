# Coded By Lapis Pheonix
# Made for Redblaise
import cv2
import threading

from os.path import abspath, exists, isdir
from utils.error import VideoCodecError, LoadingSettingsError, DirectoryError, MinThreadError, MaxThreadError, CodecError
from utils.load import load
from colorama import Fore, init

init()

red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

try:
    settings = load("settings.json")
except Exception:
    raise LoadingSettingsError(red + f"Failed to load settings!" + reset)
else:
    input_directory = settings[0]
    end_directory = settings[1]
    threads = settings[2]
    codec = settings[3]

    if input_directory:
        if exists(input_directory):
            if isdir(input_directory):
                inpdir = abspath(input_directory)
            else:
                raise DirectoryError(red + "Input Directory is not an folder" + reset)
        else:
            DirectoryError(red + "Input Directory does not exist." + reset)
    else:
        LoadingSettingsError(red + "Input Directory is required!" + reset)
    
    if end_directory:
        if exists(end_directory):
            if isdir(end_directory):
                enddir = abspath(end_directory)
            else:
                raise DirectoryError(red + "End Directory is not an folder" + reset)
        else:
            DirectoryError(red + "End Directory does not exist." + reset)
    else:
        LoadingSettingsError(red + "End Directory is required!" + reset)
    
    if threads:
        if threads <= 0:
            raise MinThreadError(red + f"Minimum threads is 1, but got {reset}{threads}")
        elif threads >= 24:
            raise MaxThreadError(red + f"Maximum threads is 23, but got {reset}{threads}")
    else:
        raise LoadingSettingsError(red + "Threads invalid or not found!" + reset)

    if codec:
        if codec == "x265" or "x264":
            pass
        else:
            raise CodecError(red + "Invalid or Unsupported Codec" + reset)
    else:
        LoadingSettingsError(red + "Codec not found!" + reset)



def convert():
    global codec
    global inpdir
    global enddir
    if codec == "x265":
        fourcc = cv2.VideoWriter_fourcc(*'x265')
    elif codec == "x264":
        fourcc = cv2.VideoWriter_fourcc(*'x264')
    else:
        raise VideoCodecError(red + "Unknown codec" + reset)
    cap = cv2.VideoCapture(inpdir)    # TODO: Add input
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    out = cv2.VideoWriter(enddir, fourcc, fps, frame_size, True)  # TODO: Add output
    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    cap.release()
    out.release()

print("Working on videos")
for thread in range(threads):
    threading.Thread(target=convert).start()
