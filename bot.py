import config
import random
from random import choice
from telebot.types import ReactionTypeEmoji
import os
from telebot import types
import telebot



#chat_types
#regexp
#func
#commnds
#content_types










bot = telebot.TeleBot(config.token)

lista = ["ciao","oddio","non ci credo","yessir"]
emoji = ["\U0001F525", "\U0001F917", "\U0001F60E"] 
parole=["Ciao","godo","arrivedrci"]



@bot.message_handler(commands=["test"])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text= "btn1", callback_data="btn1")
    btn2 = types.InlineKeyboardButton(text= "btn2", callback_data="btn2")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, "1", reply_markup=markup)
    
    
     
@bot.callback_query_handler(func=lambda callback: True)
def check_callbackdata(callback):
    print("si")
    if callback.data == "btn1":
        
         markup = types.InlineKeyboardMarkup()
         btn1 = types.InlineKeyboardButton(text= "btn2", callback_data="btn2")
         btn2 = types.InlineKeyboardButton(text= "btn2", callback_data="btn1")
         markup.add(btn1,btn2)
         bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="ancora", reply_markup=markup) 

@bot.message_handler(commands=["file"]) 
def file(message): 
    folder_path = "C:\\Users\\tomas\\Desktop\\tesbot_testima\\photo"
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(files)
    if not files:
            bot.send_message(message.chat.id, "Папка пуста. Добавьте фотографии.")
            return
    random_file = choice(files)
    file_path = os.path.join(folder_path, random_file)
    with open(file_path, "rb") as file:
        if file_path == "C:\\Users\\tomas\\Desktop\\tesbot_testima\\photo\\boar.jpg":
            bot.send_photo(message.chat.id, file, caption=f"Here is a random photo: {random_file}")
  
  
  
  
           
@bot.message_handler(commands=["key"])
def key(message):                                          # Bottoni che quando clicchi fanno il testo
    kb= types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ciao")
    btn2 = types.KeyboardButton("Arrivedrci")
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, "Ciao", reply_markup=kb)
  
  
  
  
  
  
@bot.message_handler(commands=["button"])  
def key(message):
    kb = types.InlineKeyboardMarkup(row_width=2)                            # Bottoni che quando clicchi ti portano ad un sito con url
    btn1 = types.InlineKeyboardButton("gpt", url="https://chatgpt.com/")
    btn2 = types.InlineKeyboardButton("erewhon", url="https://erewhon.com/" )
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, "Here are some buttons", reply_markup=kb)
    

@bot.message_handler(commands=["car"])
def car(message):
    telebot.util.extract_arguments(message.text) 
    


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def home(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
@bot.message_handler(func=lambda x: x.text == "1")
def tut(message):
    bot.send_message(message.chat.id, """Works def tut""") 


@bot.message_handler(commands=['info'])
def house(message):
    bot.send_message(message.chat.id, """<b>Hi and welcome to my first tryout bot</b>""",parse_mode="html") 
    
@bot.message_handler(commands=['random'])
def gg(message):
    
    bot.reply_to(message, choice(lista)  )     
    


@bot.message_handler(func=lambda message: True)
def send_reaction(message):
     if "cool" in message.text.lower():
 # or use [":fire:", ":hugging:", ":sunglasses:"]
        bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emoji))], is_big=False)

        

@bot.message_handler(content_types=['photo'])
def photoo(message):
       bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emoji))], is_big=False) 

 
   
bot.polling(allowed_updates=["message", "callback_query"])


