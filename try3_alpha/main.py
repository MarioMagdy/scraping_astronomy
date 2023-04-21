import cv2
import numpy as np
import positions
import os
import deal_with_files
import time
from bing_functions import *
###### I'm sopposing that you already have a script ######



Generate_script_prompt= ["I'm making a short video 30 seconds for my tik tok talking about space and astronomy trying to make an exciting and enthusiastic video... Trying to make the videos exciting and people can relate to it while being useful and fun","I need your help, I'm making a short video 30 seconds for my tik tok talking about space and astronomy trying to make exciting and enthusiastic video, Write me a script containing one fact, make the video script in no more than 80 word without instructions in the middle of the script, no intro, and a very short outro Just “follow me for more crazy facts”... try to make the illustrations or comparisons to illustrate the fact,  here is the fact I want you to use"]

Image_prompt_generator_prompt = "I'm making a short video 30 seconds for my tik tok talking about space and astronomy trying to make exciting and enthusiastic video, I will make the video as an audio of a script being read and images of the things we talk about, while using the AI generated Images to illustrate, I'm going to change the image every 10 seconds, give me 5 image prompts suitable to illustrate what I will be talking about at that time, make sure the prompts are clear and address the image very well, Make your answer ONLY the prompts no other notes or anything just the prompts that I will give to midjourney to generate the image and here is the video script in"

prompt_to_draw = "draw in a very realistic, acurate saturated colors, acurate, magnificente, beautiful, cinematic, exciting, high details style "

bing_pos = positions.obj_pos('bing')

temp = cv2.imread(r'essentials\1.png',0)


# print(bing_pos.text_pos)
path_scripts = 'scripts'
scripts = deal_with_files.getListOfFiles(path_scripts)

print(scripts)

############################################################
############## The Algorithm starts here ###################
############################################################

for ind,script in enumerate (scripts):

    ## Making dir for each script
    if not os.path.exists(f'images/{ind}'):
        os.makedirs(f'images/{ind}')

    if not os.path.exists(f'parts_videos/{ind}'):
        os.makedirs(f'parts_videos/{ind}')
    #####################################






    #### getting the script and prompt that gets me the prompts for images generation
    todays_script = deal_with_files.read_script(script)
    my_prompt = Image_prompt_generator_prompt+' "'+todays_script+'"'
    print(my_prompt)




    #### start using bing here
    time.sleep(5)


    #### write the prompt in bing and click then wait 30 sec
    clear_bing(bing_pos.text_pos,bing_pos.no_text_pos2,bing_pos.clear_pos)

    write_in_bing(my_prompt,bing_pos.text_pos)

    pyautogui.press("enter")

    time.sleep(20)


    #### now we take the output from bing by finding the copy button with opencv then copy it to a variable
    the_answer = copy_answer2(bing_pos.answer_pos,temp)

    deal_with_files.save_txt(f'prompts/for_imgs/script{ind}',the_answer)


    img_prompts = deal_with_files.find_points(f'prompts/for_imgs/script{ind}')


    print(img_prompts)
    for ind2,img_prompt in enumerate(img_prompts):
        clear_bing_prompt(bing_pos.text_pos)
        time.sleep(0.5)
        prompt_for_img = prompt_to_draw + "'" + img_prompt+ "'"
        write_in_bing(prompt_for_img,bing_pos.text_pos)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(35)

        img = get_bing_img()
        cv2.imwrite(f"images/{ind}/{ind2}.png",img)





