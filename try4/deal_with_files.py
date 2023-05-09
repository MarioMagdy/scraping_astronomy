import os
from bs4 import BeautifulSoup

def read_script(file_and_dir):
    "reads htm-scripts files and returns the text"

    html =open(file_and_dir,'r', encoding='latin-1').read()

    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = ' '.join(chunk for chunk in chunks if chunk)
    return text



def save_txt(file_and_dir,file):
    text_file = open(file_and_dir, "w",encoding='UTF-8')
    text_file.write(file)
    text_file.close()



def save_htm(file_and_dir,file):
    text_file = open(file_and_dir,  'wb+',encoding='UTF-8')
    text_file.write(file)
    text_file.close()



def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles




def find_points(file_and_dir):
    lines = []
    f = open(file_and_dir,'r', encoding='latin-1')
    full_file = f.readlines()
    for line in full_file:
        if line.startswith("-"):
            lines.append(line)

            print(line[2:])

    return lines

