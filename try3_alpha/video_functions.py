import math
from PIL import Image
import numpy
import moviepy.editor as mpy
import deal_with_files



def zoom_in_effect(clip, zoom_ratio=0.04):
    def effect(get_frame, t):
        img = Image.fromarray(get_frame(t))
        base_size = img.size

        new_size = [
            
            math.ceil(img.size[0] * (1 + (zoom_ratio * t))),
            math.ceil(img.size[1] * (1 + (zoom_ratio * t)))
        ]

        # The new dimensions must be even.
        new_size[0] = new_size[0] + (new_size[0] % 2)
        new_size[1] = new_size[1] + (new_size[1] % 2)

        img = img.resize(new_size, Image.LANCZOS)

        x = math.ceil((new_size[0] - base_size[0]) / 2)
        y = math.ceil((new_size[1] - base_size[1]) / 2)

        img = img.crop([
            x, y, new_size[0] - x, new_size[1] - y
        ]).resize(base_size, Image.LANCZOS)

        result = numpy.array(img)
        img.close()

        return result

    return clip.fl(effect)








def make_vid_material(listOfFiles,ind,duration=5,size=(1920,1080)):
    "function that takes list of the imgs directories and makes zoom in videos that can be then used to generate the final video by combining them and an audio"

    for ind2,img in enumerate(listOfFiles):

        clip = mpy.ImageClip(img).set_fps(30).set_duration(duration).resize(size)
        clip = zoom_in_effect(clip, 0.04)
        clip.write_videofile(fr"parts_videos\{ind}\my_video{ind2}.mp4",audio=False) # save the video as mp4






def make_final_video(ind):
    vids =[]
    listOfFiles = deal_with_files.getListOfFiles(fr"parts_videos\{ind}")
    for vid_path in enumerate(listOfFiles):
        vids.append(mpy.VideoFileClip(vid_path))

    # Load the audio
    audio_path = r'audios\prob.mp3'
    audio = mpy.AudioFileClip(audio_path)


    # Combine the videos
    final_video = mpy.concatenate_videoclips([vids])
    final_video.set_duration(audio.duration)

    # Add the audio to the final video
    final_video = final_video.set_audio(audio)

    # Write the final video to a file
    final_video.write_videofile(f'final_videos/final_video {ind}.mp4')




def make_final_video_I_give_audio(ind,audio):
    vids =[]
    listOfFiles = deal_with_files.getListOfFiles(fr"parts_videos\{ind}")


    for ind2,vid_path in enumerate(listOfFiles):
        print(vid_path)
        vids.append(mpy.VideoFileClip(vid_path))


    # Combine the videos
    final_video = mpy.concatenate_videoclips([vid for vid in vids])
    final_video.set_duration(audio.duration)

    # Add the audio to the final video
    final_video = final_video.set_audio(audio)

    # Write the final video to a file
    final_video.write_videofile(f'final_videos/final_video {ind}.mp4')


