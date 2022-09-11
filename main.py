# This example requires the 'message_content' intent.
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import torch
import discord
import buffer
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-squad")
model = AutoModelForQuestionAnswering.from_pretrained("savasy/bert-base-turkish-squad")
nlp=pipeline("question-answering", model=model, tokenizer=tokenizer)
        
    
intents = discord.Intents.default()
intents.message_content = True

Bot = discord.Client(intents=intents)

@Bot.event
async def on_ready():
    print(f'We have logged in as {Bot.user}')

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    if(message.channel.id != 1018494784064716932):
        return
    if message.content.startswith("."):
        answer = nlp(question=message.content[1:], context=buffer.text)
        await message.channel.send(answer["answer"])
        return
        
    buffer.text += message.content + ". "    

Bot.run('YOUR_HERE')
