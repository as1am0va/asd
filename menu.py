from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
    
)
otkuda_list=['otkuda_bishkek','otkuda_talas','otkuda_osh','otkuda_naryn','otkuda_batken']
otkuda_dict={'otkuda_bishkek': 'Бишкек',
             'otkuda_talas': 'Талас',
             'otkuda_osh': 'Ош',
             'otkuda_naryn': 'Нарын',
             'otkuda_batken': 'Баткен'}
kuda_list=['kuda_bishkek','kuda_talas','kuda_osh','kuda_naryn','kuda_batken',]
kuda_dict={'kuda_bishkek': 'Бишкек',
           'kuda_talas': 'Талас',
           'kuda_osh': 'Ош',
           'kuda_naryn': 'Нарын',
           'kuda_batken': 'Баткен'}
cars_list=['car','sprinter','bus']
def otkuda_inline_menu():
    keyboard = [
        [InlineKeyboardButton("Бишкек", callback_data='otkuda_bishkek')],
        [
            InlineKeyboardButton("Талас", callback_data='otkuda_talas'),
            InlineKeyboardButton("Ош", callback_data='otkuda_osh'),
        ],
        [
            InlineKeyboardButton("Нарын", callback_data='otkuda_naryn'),
            InlineKeyboardButton("Баткен", callback_data='otkuda_batken'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def kuda_inline_menu():
    keyboard = [
        [InlineKeyboardButton("Бишкек", callback_data='kuda_bishkek')],
        [
            InlineKeyboardButton("Талас", callback_data='kuda_talas'),
            InlineKeyboardButton("Ош", callback_data='kuda_osh'),
        ],
        [
            InlineKeyboardButton("Нарын", callback_data='kuda_naryn'),
            InlineKeyboardButton("Баткен", callback_data='kuda_batken'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def car_inline_menu():
    keyboard = [
        [InlineKeyboardButton("Машина", callback_data='car')],
        [
            InlineKeyboardButton("Спринтер", callback_data='sprinter'),
            InlineKeyboardButton("Маршрутка", callback_data='bus'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

drivers = {
    'Ben': {
        'otkuda': 'otkuda_bishkek',
        'kuda': 'kuda_naryn',
        'car': 'car',
        'mobile': '0700919797'
    },
    'Sam': {
        'otkuda': 'otkuda_bishkek',
        'kuda': 'kuda_talas',
        'car': 'car',
        'mobile': '0700919797'
    },
    'Ron': {
        'otkuda': 'otkuda_bishkek',
        'kuda': 'kuda_osh',
        'car': 'car',
        'mobile': '0700919797'
    },
    'Harry': {
        'otkuda': 'otkuda_bishkek',
        'kuda': 'kuda_naryn',
        'car': 'bus',
        'mobile': '0700919797'
    },
    'Tom': {
        'otkuda': 'otkuda_bishkek',
        'kuda': 'kuda_talas',
        'car': 'car',
        'mobile': '0700919797'
    },
    'Abi': {
        'otkuda': 'otkuda_bishkek',
        'kuda': 'kuda_talas',
        'car': 'sprinter',
        'mobile': '0700919797'
    },
    'Robert': {
        'otkuda': 'otkuda_bishkek',
        'kuda': 'kuda_osh',
        'car': 'bus',
        'mobile': '0700919797'
    },
}
