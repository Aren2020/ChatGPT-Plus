import openai
import os
import speech_recognition as sr
import os
from gtts import gTTS


from backend_api.actions.wordcreater import wordCreater
from backend_api.actions.handlegptslide import handleGptSlide,splitlinks
from backend_api.actions.removetrashes import removeTrash
from backend_api.actions.slidecreater import slidegptmaker
from backend_api.actions.translator import translateTo
from backend_api.actions.namegenerator import nameGenerator

openai.api_key = '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'

def getcontent(message):
    msgs = []
    msgs.append(
            {'role':'user',
             'content':message})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages = msgs,
        temperature = 0.2,
        max_tokens = 1024,
    )
    content = response['choices'][0]['message']['content']
    return content,'text'

def essaywriter(title,words,language):
    message = f'''Write a {words}-word essay about {title} with this criteria. 
    The essay must contain citations.
    The essay must contain the research question. 
    The essay must answer the research question in the conclusion.
    The essay must contain an in-text reference in each paragraph.
    And give links which you use in the bottom.
    '''
    response, type = getcontent(message)
    content = wordCreater(response.split('\n'),language)
    return content, type

def personalprojectwriter(title,language):
    message =  '''I am writing my personal project about a %s.
         It contains  criteria (A.1, A.2, A.3, B.1, B.2, B.3, C.1, C.2). 
         The A.1 criteria should contain My Learning Goal and Personal Interests.
         The A.2 criteria should contain My Product and The Success Criteria.
         The A.3 criteria should contain My Action Plan/ Timeline To Achieve My Learning Goal And Product Goal.
         The B.1 criteria should contain Doing research: Achieving My Learning Goal - ATL Skills: Research.
         The B.2 criteria should contain Self-management, Communication, and Collaboration, Self-management, and Thinking.
         The B.3 criteria should contain The Creating The Product: Achieving My Product Goal - ATL Skills: Communication and Collaboration, Self-management, Thinking. 
         The C.1 criteria should contain The impact of my project.
         The C.2 criteria should contain the evaluation of the product.
         You should help me write %s criterion using 850 words.'''
    messages = [
        message % (title,'A.1'),
        message % (title,'A.2'),
        message % (title,'A.3'),
        message % (title,'B.1'),
        message % (title,'B.2'),
        message % (title,'B.3'),
        message % (title,'C.1'),
        message % (title,'C.2'),
    ]

    responses = []
    for message in messages:
        response, type = getcontent(message)
        responses.append(response)
    response = '\n'.join(responses)
    content = wordCreater(response.split('\n'),language)
    return content,type

def communityProjectCreator(title,language = 'en'):
    title = translateTo(title,'en',source='auto')
    message = f'''
    write a report about {title} with these criteria. 
    The report should contain 700-1000 words. The report has 4 parts.
    The first part should contain What did you research and what information did you study.
    The second part should contain What end result are you planning to get and What steps/actions have you planned to achieve the result. 
    Describe in detail the activities you did as part of the community project. 
    The third part should contain Also describe the difficulties, and obstacles you faced and who you collaborated with in implementing the community project. Forth part should contain Assessing the quality of your end result What went well, and what would you change the next time you do the job, What skills (ATL skills) have you developed within the community project  and What qualities of MB student characteristics have you developed
    '''
    response,type = getcontent(message)
    content = wordCreater(response.split('\n'),language)
    return content, type
    
def getslidecontent(title,language):
    message = f'''create slideshow with this strict criteria about {title}.
    SlideShow should contain 5 slides.Each slide start with title then come description and one picture.
    Each description should contain 25 words
    Slideshow should not have conclusion and intruduction.
    And use "picture:  "  instead of [Insert an image'''
    
    response,type = getcontent(message)
    content = handleGptSlide(response)
    content = removeTrash(content,'')
    links = splitlinks(getcontent(f'which books do you use when you write essay about {title}')[0])
    url = slidegptmaker(content,links,language,title=title)
    return url, 'pptx'

def speech_to_text(file,language = 'en'):
    engine = sr.Recognizer()
    mp3Filename = file.replace('\\','\\\\')
    with sr.AudioFile(mp3Filename) as source: # C:\Users\User\Desktop\django_react\test.mp3
        audio = engine.record(source)
    text = engine.recognize_google(audio)
    return text, 'text'

def text_to_speech(text,language = 'en'):
    speech = gTTS(text = text, lang = language, slow = False)
    name = nameGenerator() + '.mp3'
    savepath = os.path.join('media','mp3',name)
    speech.save(savepath)
    return savepath,'mp3'

def imageGenerator(text,size = '1024x1024'):
    response = openai.Image.create(
        prompt = text,
        n = 1,
        size = size
    )
    image_url = response['data'][0]['url']
    return image_url, 'text'

def grammarCorrection(text,language='English'):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[{
            'role': 'user',
            'user': f'You will be provided with statements, and your task is to convert them to standard {language} and correct the wrong words. {text}',
            }],
        temperature=0,
        max_tokens=15000
    )
    return response, 'text'
