from openai import OpenAI
from pathlib import Path
import os
import sys
with open('API.txt') as file:
        api = file.read().replace('\n','')
client = OpenAI(api_key=api)

response = client.images.generate(
        model =sys.argv[2],
        prompt = sys.argv[1],
        size = sys.argv[3],
        quality= sys.argv[4],
        n=int(sys.argv[5]),
)

image_url = response.data[0].url

print(image_url)

