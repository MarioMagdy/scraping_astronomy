import cv2
import numpy as np
import positions
import os
import deal_with_files
import time
from bing_functions import *
import video_functions
import moviepy.editor as mpy

import concurrent

############## For the first video only ###############

img_list = deal_with_files.getListOfFiles(r"images\0")
print(img_list)

audio_path = r'audios\0.mp3'
audio = mpy.AudioFileClip(audio_path)

print(audio.duration)

audio.write_audiofile("aduioooo.mp3")
vid_parts_dur = int(audio.duration/len(img_list))+1
print("We are redering the parts")


# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = executor.map(video_functions.make_vid_material, img_list,[0 for i in range(len(img_list))],[vid_parts_dur for i in range(len(img_list))],[(1380,1920) for i in range(len(img_list))])



video_functions.make_vid_material(img_list,0,vid_parts_dur,(1380,1920))

print("done with the parts, Now the final video:")

video_functions.make_final_video_I_give_audio(0,audio)
print("""   ALL DONE
        FINALLY !!!""")