from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from start_kb import queue_start_kb

queue_list = {
    "queue" : [],
    "list":{},
    "message": None
}



async def admin_start(bot:Bot, message:types.Message):
         
    if message.from_user.username in ["FRZBin", "Fenix888YT", "Luks138"]:
        queue_list['queue'].clear()
        queue_list['list'].clear()
        if queue_list["message"]:
            await bot.delete_message(message.chat.id, queue_list["message"].message_id)
        
        message = await bot.send_message(message.chat.id,"Занимаем очередь:", reply_markup=queue_start_kb())
        queue_list["message"] = message


        
        

async def add_queue(bot:Bot, call:types.CallbackQuery):
    if call.from_user.id in queue_list['queue']:
        await bot.send_message(call.message.chat.id, "Не сегодня")
        return
    
  
    queue_list['queue'].append(call.from_user.id)
    queue_list['list'][len(queue_list['queue'])] = call.from_user.username

    text = ""

    for key, value in queue_list["list"].items():
        text += str(key)+": " + str(value) + "\n"
        

    message = await bot.edit_message_text("Занимаем очередь:\n" +text, call.message.chat.id, queue_list["message"].message_id, reply_markup=queue_start_kb())
    queue_list["message"] = message
    
    
