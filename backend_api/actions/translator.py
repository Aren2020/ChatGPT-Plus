from deep_translator import GoogleTranslator

def translateTo(response,language,source = 'en'):
    response = GoogleTranslator(source = 'auto',target = language).translate(response)
    return response,'text'
