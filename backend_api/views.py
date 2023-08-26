from django.shortcuts import render
from rest_framework.views import APIView
from .models import Section
from rest_framework.response import Response
from django.http import HttpResponse
from .serializer import SimpleSectionSerializer
from rest_framework import generics
from backend_api.actions.gpt import (getcontent,
                                     essaywriter,
                                     personalprojectwriter,
                                     text_to_speech,
                                     imageGenerator,
                                     grammarCorrection,
                                     # speech_to_text,
                                     getslidecontent,
                                     translateTo,
                                     communityProjectCreator,
                                     informatics
                                    )
from deep_translator import GoogleTranslator

FUNC_FOR_MODELS = {
    1: getcontent, # gpt
    2: personalprojectwriter,
    3: imageGenerator,
    4: getslidecontent,
    5: essaywriter,
    6: communityProjectCreator,
    # 7: speech_to_text,
    7: translateTo,
    8: text_to_speech,
    9: informatics,
    10: grammarCorrection,
}

FORMAT_CONTENT_TYPES = {
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'mp3': 'audio/mpeg',
}

class SectionDetailsView(APIView):
    def get(self,request,slug = 'gpt-response'):
        output = [
            {
                'sections': [],
            },
        ]
        for section in Section.objects.all():
            section_config = {
                'name': section.name,
            }
            if section.slug == 'gpt-response' and slug == 'gpt-response':
                section_config['active'] = '.'
            else:
                section_config['active'] = section.slug
            output[0]['sections'].append(section_config)
        return Response(output)

    def post(self,request,slug = 'gpt-response'): 
        arr = []
        for key in request.data:
            if key != 'active':
                arr.append(request.data.get(key))
            else:
                slug = request.data.get('active')
        
        section = Section.objects.get(slug = slug)
        action = FUNC_FOR_MODELS[section.pk]
        
        data,format = action(*arr) 
        if format == 'text':
            return Response({'message': data})  
        else:
            with open(data, 'rb') as file:
                response = HttpResponse(file.read(), content_type = FORMAT_CONTENT_TYPES[format])
                response['Content-Disposition'] = f'attachment; filename="output.{format}"'
                return response

class SectionHomeView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SimpleSectionSerializer

class SupportedLanguagesView(APIView):
    def get(self,request):
        output = {'supported_languages': GoogleTranslator().get_supported_languages(as_dict=True)}
        return Response(output)
