from deep_translator import GoogleTranslator

def translateTo(response,language,source = 'en'):
    if language!='en' or source!='en':
        response = GoogleTranslator(source = source,target = language).translate(response)
    return response,'text'
