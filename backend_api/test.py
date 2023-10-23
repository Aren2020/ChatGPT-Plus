import requests

result = requests.post('http://localhost:8000/chat/chat-gpt/',data = {'message': 'hi'})

print(result)