import pyautogui
import time
from random import uniform
import pyperclip  # handy cross-platform clipboard text handler
import cv2
import numpy as np


def clear_bing_prompt(bing_ai_text_position):
    "clears the prompt only so you can write new one if needed"
    pyautogui.moveTo(bing_ai_text_position) # move the mouse to the pixel 
    time.sleep(0.3) # wait for 1 second
    pyautogui.click() # click the mouse

    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.3) # wait for 1 seconds
    pyautogui.hotkey("del")




def clear_bing(bing_ai_text_position,bing_ai_no_text_position2,bing_ai_clear_position):
    "clears the conversation  and the prompt"
    pyautogui.moveTo(bing_ai_text_position) # move the mouse to the pixel 
    time.sleep(0.3) # wait for 1 second
    pyautogui.click() # click the mouse

    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.3) # wait for 1 seconds
    pyautogui.hotkey("del")

    pyautogui.moveTo(bing_ai_no_text_position2) # move the mouse to the pixel 
    pyautogui.click() # click the mouse
    time.sleep(0.5) # wait for 1 seconds

    pyautogui.moveTo(bing_ai_clear_position) # move the mouse to the pixel 
    time.sleep(0.5) # wait for 1 seconds
    pyautogui.click() # click the mouse
    time.sleep(1)


def write_in_bing(text_to_write,bing_ai_text_position):
    pyautogui.moveTo(bing_ai_text_position) # move the mouse to the pixel 
    time.sleep(0.3) # wait for 1 second
    pyautogui.click() # click the mouse
    time.sleep(0.3)
    pyautogui.write(text_to_write)


def copy_answer(bing_answer_position):
    pyautogui.moveTo(bing_answer_position) # move the mouse to the pixel 
    time.sleep(0.3) # wait for 1 second
    pyautogui.click() # click the mouse

    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.3) # wait for 1 second

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1) # wait for 1 second
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1) # wait for 1 second
    return pyperclip.paste()



def find_temp_in_img(template,image):
    bgr= cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    

    gray= cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

    height, width= template.shape[:2]


    top_left= max_loc
    bottom_right= (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)
    print(top_left[0] + width , top_left[1] )
    return top_left[0] + width-10 , top_left[1] +10




def find_the_copy_buttom(temp):
    "Takes a screenshot and searches for 'more' buttom"
    im1= np.asarray(pyautogui.screenshot())
    return  find_temp_in_img(temp,im1)
    



def copy_answer2(bing_answer_position,temp):
    "Takes a screenshot and searches for 'more' buttom, clicks on it then click on copy then returns this as a variable"
    pyautogui.moveTo(bing_answer_position) # move the mouse to the pixel 
    time.sleep(0.3) # wait for 1 second
    pyautogui.click() # click the mouse
    time.sleep(1)

    copy_button_pos = find_the_copy_buttom(temp)

    pyautogui.moveTo(copy_button_pos) # move the mouse to the pixel 
    time.sleep(0.2) # wait for 1 second
    pyautogui.click() # click the mouse

    pyautogui.moveTo(copy_button_pos[0],copy_button_pos[1]+30) # move the mouse to the pixel 
    time.sleep(0.2) # wait for 1 second
    pyautogui.click() # click the mouse
    time.sleep(0.5)


    return pyperclip.paste()



def get_bing_img():

    # time.sleep(2) # wait for 1 second
    x = uniform(1620,1700)
    if x>1640 and  x<1660:
        pyautogui.moveTo(1680, 500)
    else:
        pyautogui.moveTo(x, 500)
        
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(5) # wait for 1 second

    im = np.asarray(pyautogui.screenshot(region=(60,190, 850-60, 920-190)))
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    return im

