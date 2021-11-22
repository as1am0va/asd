from telegram import (
    Update,
    chat, 
    
)
from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    PicklePersistence,
    CallbackQueryHandler

)
from menu import (
    otkuda_inline_menu,
    kuda_inline_menu,
    kuda_list,
    otkuda_list,
    car_inline_menu,
    drivers,
    cars_list,
    otkuda_dict,
    kuda_dict
)
from credentials import TOKEN


otkuda = []
kuda = []

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Добро пожалоавть, {username}, в каком городе вы находитесь: ".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username),
        reply_markup=otkuda_inline_menu()
    )
    

def driver_choice(a, b, c):
    choices = []
    for key, value in drivers.items():
      if value['otkuda']==a and value['kuda']==b and value['car']==c:
        choices.append(
          f"Водитель: {key}\n"\
          f"{otkuda_dict[value['otkuda']]} - {kuda_dict[value['kuda']]}\n"\
          f"{value['mobile']}\n"
          )
    return choices

def button(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    query.answer()
    
    if query.data in otkuda_list:
        otkuda.append(query.data)
        query.message.edit_text(
            text='Хорошо теперь выберите куда вам надо: ',
            reply_markup=kuda_inline_menu()
        )
    if query.data in kuda_list:
        kuda.append(query.data)
        query.message.edit_text(
            text='Выберите транспорт: ',
            reply_markup=car_inline_menu()
        )
    if query.data in cars_list:
        car = query.data
        d = driver_choice(otkuda[-1], kuda[-1], car)
        if d != []:
            for i in d:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=i
                )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="К сожеление нет попутчиков"
            )





updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CallbackQueryHandler(button))



updater.start_polling()
updater.idle()













