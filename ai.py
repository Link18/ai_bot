import os
from dotenv import load_dotenv
import httpx
from openai import AsyncOpenAI
from mistralai import Mistral

load_dotenv()

client=AsyncOpenAI(api_key=os.getenv("AI_TOKEN"),
                   http_client=httpx.AsyncClient(
                       proxies=os.getenv('PROXY'),
                       transport=httpx.HTTPTransport(local_address="0.0.0.0")))

async def gpt(question):
    response=await client.chat.completions.create(
        messages=[{"role":"user",
                   "comtent":str(question)}],
        model="gpt-3.5-turbo"
    )
    return response

async def gpt_image(image_prompt):
    response = await client.images.generate(
        prompt=str(image_prompt),
        model='dall-e-2',
        size='512x512',
        response_format='url',
        n=1
    )
    return response


async def mistral_ai(question):
    s = Mistral(
        api_key=os.getenv("MISTRAL_API_KEY"),
    )
    res = await s.chat.complete_async(model="mistral-small-latest", messages=[
        {
            "content":str(question),
            "role": "user",
        },
    ])
    return res

async def mistral_ai_fl(question):
    s = Mistral(
        api_key=os.getenv("MISTRAL_API_KEY"),
    )
    res = await s.chat.complete_async(model="mistral-small-latest", messages=[
        {
            "content":f'напиши отклик на отклик на задачу с фриланс биржи с таким описанем:({str(question)}). Отклик должен бытьнаписан от лица Python разработчика.',
            "role": "user",
        },
    ])
    return res