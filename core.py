from aiogram import types, utils
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from start_kb import queue_start_kb
import random

queue_list = {
    "queue" : [798892590, 1030297121],
    "list":{1:"Fenix888YT", 2:"FRZBin"},
    "message": None
}

async def admin_update(bot:Bot, message:types.Message):
    if message.from_user.username in ["FRZBin", "Fenix888YT", "Luks138"]:
        if queue_list["message"] and len(queue_list["list"]) > 0 and len(queue_list['queue']) > 0:
            text = ""

            for key, value in queue_list["list"].items():
                text += str(key)+": " + str(value) + "\n"
            
            try:
                await bot.edit_message_text("Занимаем очередь:\n" + text, message.chat.id, queue_list["message"].message_id, reply_markup=queue_start_kb())
            except utils.exceptions.MessageNotModified:
                print('all good')
            return
        
    await bot.send_message(message.chat.id, "Куда ты лезешь "+message.from_user.username+", щегол")

            


# 1030297121
async def admin_start(bot:Bot, message:types.Message):
    if message.from_user.username in ["FRZBin", "Fenix888YT", "Luks138"]:
        queue_list['queue'].clear()
        queue_list['list'].clear()
        queue_list['queue'] = [798892590, 581496581]
        queue_list['list'] = {1:"Fenix888YT", 2:"Luks138"}
        prepare_array()

        queue_list['queue'].append(1030297121)
        queue_list['list'][len(queue_list['queue'])] = "FRZBin"

        if queue_list["message"]:
            await bot.delete_message(message.chat.id, queue_list["message"].message_id)
        
        message = await bot.send_message(message.chat.id,"Занимаем очередь:", reply_markup=queue_start_kb())
        queue_list["message"] = message
        return
    
    await bot.send_message(message.chat.id, "Куда ты лезешь "+message.from_user.username+", щегол")


        
        

async def add_queue(bot:Bot, call:types.CallbackQuery):
    if call.from_user.id in queue_list['queue']:
        await bot.answer_callback_query(call.id, "ДиНах", True)
        return
    
    queue_list['queue'].append(call.from_user.id)
    queue_list['list'][len(queue_list['queue'])] = call.from_user.username

    text = ""

    for key, value in queue_list["list"].items():
        text += str(key)+": " + str(value) + "\n"

    await bot.edit_message_text("Занимаем очередь:\n" +text, call.message.chat.id, queue_list["message"].message_id, reply_markup=queue_start_kb())
    
    
    
def prepare_array():
    values = list(queue_list['list'].values())
    random.shuffle(values)
    shuffled_dict = {key: value for key, value in zip(queue_list['list'].keys(), values)}
    queue_list['list'] = shuffled_dict
