from pyrogram import Client, filters ,types

#معلومات البوت
api_id = 27766208
api_hash = "f9d1a332b194bdc93d5bf838b60a52c5"
bot_token = "7425298916:AAHtIIszbYTF41RnuyrpWFlVRxyaP_gPETE"

#برمجة البوت
#---------------------------------------رسالة البدء--------------------------------------------------------------------
start_msg = "اهلا بك في البوت المميز لشروحات لعبة bleach brave souls"
start_img = "https://bucket.bbs-simulator.com/character_gachas/1150-d67aecee-ee6f-4b90-b340-5f4961473a40.png"
#-----------------------------------------------صورة و نص التعريف------------------------------------------------------
introduction = " اللعبة عبارة عن لعبة حركة في الوقت الفعلي تتضمن عناصر لعب الأدوار، وتتميز بأوضاع مثل:القصة، والقصص الجانبية، والقصص الفرعية، ومهام الوقائع، والأحداث، ومهام Senkaimon، والتعاونية، والغارات الملحمية، ومهام النقابة، و  PVP.\n\nتسمح طريقة اللعب للاعبين بمتابعة قصة Bleach من Substitute Soul Reaper Arc إلى Lost Agent Arc.توفر القصة الجانبية والقصص الفرعية والأحداث الأخرى فرصة لمتابعة TYBW Arc وأقواس حشو الاختيار والمحتويات الجديدة."
introduction_img = "https://static.wikia.nocookie.net/bleach-bravesouls/images/a/ac/Banner4.png/revision/latest/scale-to-width-down/670?cb=20230729044034"
#------------------------------------------------------------------------------------------------------------------------


bot = Client('bbs_session',api_id=api_id,api_hash=api_hash,bot_token=bot_token)
#الازرار
buttons = [
    [types.KeyboardButton("تعريف اللعبة💥")],
    [types.KeyboardButton("قريبا")]
]

@bot.on_message()
def start(bot,msg):
    reply_markup = types.ReplyKeyboardMarkup(buttons, is_persistent=True,resize_keyboard=True)
    if(msg.text == "/start"):
        bot.send_photo(msg.chat.id,start_img,start_msg ,reply_markup=reply_markup)
    handle_text(bot,msg)


#رسائل الازرار
def handle_text(bot,msg):
    if (msg.text == "تعريف اللعبة💥"):
        bot.send_photo(msg.chat.id,introduction_img,introduction)
    elif (msg.text == "قريبا"):
        bot.send_message(msg.chat.id, "قريبا")





bot.run()


