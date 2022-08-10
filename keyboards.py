from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='ПМ', callback_data='ПМ'),
                                            InlineKeyboardButton(text="ИВТ", callback_data="ИВТ")
                                            ],
                                           [InlineKeyboardButton(text='Общежитие', callback_data='Общежитие'),]
                                       ]
                                       )