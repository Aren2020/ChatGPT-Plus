import re

def handleGptSlide(text):
    for match in ['Slide \d\d?:','Title:','Description:','Picture:']:
        text = re.split(match,text)
        text = ''.join(text)

    text = text.split('\n')
    for line in text:
        if line == '':
            text.remove(line)

    return text

def splitlinks(text):
    return re.split('\d*[.] ',text)[1:10]