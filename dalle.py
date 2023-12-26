from openai import OpenAI
from pathlib import Path
import os

with open('API.txt') as file:
        api = file.read().replace('\n','')
client = OpenAI(api_key=api)
response = client.images.generate(
        model = 'dall-e-2',
        prompt = 'a minimal remote control robot application',
        size = '256x256',
        quality='standard',
        n=1,
)

image_url = response.data[0].url

print(image_url)



