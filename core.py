from aiogram import types, utils
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from start_kb import queue_start_kb
import random
from collections import OrderedDict
queue_list = {
    "queue" : [798892590, 581496581],
    "list":{1:"Fenix888YT(Ромзесссс None)", 2:"Luks138(Ярик None)"},
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

async def set_user(bot:Bot, message:types.Message):
    if message.from_user.username in ["FRZBin", "Fenix888YT", "Luks138"]:
        try:
            user_id = int(message.text.split()[1])
            name = str(message.text.split()[2])
        except IndexError:
            print("Вы не указали ID пользователя для удаления.")
            return
        except ValueError:
            print("ID пользователя должен быть числом.")
            return
        
        new_entry = {user_id:name}

        updated_dict = {}
        for key, value in queue_list["list"].items():
            if key >= user_id:
                updated_dict[key + 1] = value
            else:
                updated_dict[key] = value

        queue_list["list"].update(new_entry)
        queue_list["list"].update(updated_dict)
    
       

async def delete_user(bot:Bot, message:types.Message):
    if message.from_user.username in ["FRZBin", "Fenix888YT", "Luks138"]:
        try:
            user_id = int(message.text.split()[1])
        except IndexError:
            print("Вы не указали ID пользователя для удаления.")
            return
        except ValueError:
            print("ID пользователя должен быть числом.")
            return
        
        queue_list["list"].pop(user_id)
        print('Успешно del')
        new_list = {index: value for index, value in enumerate(queue_list["list"].values(), start=1)}
        queue_list["list"] = new_list
        await admin_update(bot, message)
        
        return
    
    await bot.send_message(message.chat.id, "Куда ты лезешь "+message.from_user.username+", щегол")



async def admin_start(bot:Bot, message:types.Message):
    if message.from_user.username in ["FRZBin", "Fenix888YT", "Luks138"]:
        queue_list['queue'].clear()
        queue_list['list'].clear()
        queue_list['queue'] = [798892590, 581496581]
        queue_list['list'] = {1:"Fenix888YT(Ромзесссс None)", 2:"Luks138(Ярик None)"}
        prepare_array()

        queue_list['queue'].append(1030297121)
        queue_list['list'][len(queue_list['queue'])] = "FRZBin(None None)"
        

        if queue_list["message"]:
            await bot.unpin_chat_message(message.chat.id, queue_list["message"].message_id)
            await bot.delete_message(message.chat.id, queue_list["message"].message_id)
        
        message = await bot.send_message(message.chat.id,"Занимаем очередь:", reply_markup=queue_start_kb())
        

        await bot.pin_chat_message(message.chat.id, message.message_id)
        queue_list["message"] = message
        return
    
    await bot.send_message(message.chat.id, "Куда ты лезешь "+message.from_user.username+", щегол")


        
        

async def add_queue(bot:Bot, call:types.CallbackQuery):
    if call.from_user.id in queue_list['queue']:
        await bot.answer_callback_query(call.id, "ДиНах")
        return
    
    queue_list['queue'].append(call.from_user.id)

    if call.from_user.username:
        queue_list['list'][len(queue_list['queue'])] = str(call.from_user.username) + "(" + str(call.from_user.first_name) + " " + str(call.from_user.last_name) + ")"
    else:
        queue_list['list'][len(queue_list['queue'])] = str(call.from_user.first_name)

    text = ""

    for key, value in queue_list["list"].items():
        text += str(key)+": " + str(value) + "\n"

    await bot.edit_message_text("Занимаем очередь:\n" +text, call.message.chat.id, queue_list["message"].message_id, reply_markup=queue_start_kb())
    
    
    
def prepare_array():
    values = list(queue_list['list'].values())
    random.shuffle(values)
    shuffled_dict = {key: value for key, value in zip(queue_list['list'].keys(), values)}
    queue_list['list'] = shuffled_dict
