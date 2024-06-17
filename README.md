# My First Site

This project is a web application that leverages the power of OpenAI to provide various functionalities such as content generation, translation, text-to-speech, image generation, and more. Built using Django and Django Rest Framework (DRF), it demonstrates the integration of AI-based features to enhance user experience.

## Features

1. **Content Generation**:
   - **getcontent**: Generate content based on user prompts.
   - **essaywriter**: Create essays on various topics with the help of AI.
   - **personalprojectwriter**: Assist in writing personal projects and documents.
   
2. **Text-to-Speech**:
   - **text_to_speech**: Convert written text into spoken words for accessibility and convenience.

3. **Image Generation**:
   - **imageGenerator**: Generate images based on textual descriptions.

4. **Grammar Correction**:
   - **grammarCorrection**: Correct grammatical errors in the provided text.

5. **Slide Content Generation**:
   - **getslidecontent**: Create content for presentation slides.

6. **Translation**:
   - **translateTo**: Translate text into different languages.

7. **Community and Project Tools**:
   - **communityProjectCreator**: Assist in creating community projects.
   - **informatics**: Mode for programming

## Installation

1. **Clone the repository**:
   - git clone https://github.com/Aren2020/BookMarkWeb.git
2. **Create and activate a virtual environment:**
   - python -m venv env
   - source env/bin/activate
3. **Install the dependencies:** 
   - pip install -r requirements.txt
4. **Apply migrations:**
   - python manage.py makemigrations
   - python manage.py migrate
6. **Run the development server:**
   - python manage.py runserver
