from veed_functions import *
import moviepy.editor as mpy
ind = 0
l = False


time.sleep(3)

################# BETTER NOT TO USE OPEN VEED IN THE SMAE ALGO IF YOU WANT A SPECIFIC TYPE OR STYLE OF SUBTITLES USE THE FUNCTION THEN EDIT THE STYLE MANUALLY ####################
open_Veed()
###################################################################################################################################################################################


time.sleep(2)
###################### if you will use ann already open website to keep ur settings skip to here but make sure you empty the timeline manually hence it hasn't been added yet
upload_video(path=r'H:\SPEAMMMM DeepScope\me as tech\TikTok\try4\final_videos')

time.sleep(15)

###########################################################

while not l:
    get_subtitles()

    for i in range(5):

        human_mouse_move2(20)

        l = check_sub_fin()
        print(l)
        if l:
            print("subtitles done") 
            break

    if l:
        print("subtitles done") 
        break

    cancel_sub_load()


###########################################################

time.sleep(10)

pa.moveTo(input_menu_pos)
time.sleep(.35)
pa.click()


###########################################################

lis = deal_with_files.getListOfFiles(dirName=  r'H:\SPEAMMMM DeepScope\me as tech\TikTok\try4\final_videos')

video = mpy.VideoFileClip(lis[0])

record_veed_with_win2(dur=video.duration)
time.sleep(4)


###########################################################


move_win_recorded_video_to_final(ind= ind)

video = mpy.VideoFileClip( fr'H:\SPEAMMMM DeepScope\me as tech\TikTok\try4\from_win_videos\{ind}.mp4')


croped_vid = crop_video(video)

croped_vid.write_videofile(fr'try4\Videos\{ind}.mp4')

###########################################################
# print(pa.position())