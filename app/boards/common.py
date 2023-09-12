from aiogram.types        import InlineKeyboardMarkup, InlineKeyboardButton
from library.translations import (l, languages)

class Application:

    def __init__(self, lang='en') -> None:
        self.lang = lang

    def balance_menu(self):
        self.base = InlineKeyboardMarkup(row_width=2, inline_keyboard=[                        
            [InlineKeyboardButton(text=l('home', self.lang), callback_data="OnButton_Exit"), InlineKeyboardButton(text=l('help', self.lang), callback_data="OnButton_Help")],            
        ])

        return self.base   

    def language_menu(self):
        self.base = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
            # [InlineKeyboardButton(l('home', self.lang), callback_data='OnButton_Exit')]
        ])        

        ''''''
        for key in languages:
            button = InlineKeyboardButton(text=languages[key], callback_data=f'l_{key}')
            self.base.insert(button)
        
        return self.base
    
    def init_menu(self):
        self.base = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
            [InlineKeyboardButton(text=l('balanceButton', self.lang), callback_data="OnButton_Balance"), 
             InlineKeyboardButton(text=l('help', self.lang), callback_data="OnButton_Help"),
             InlineKeyboardButton(text=l('language', self.lang), callback_data="OnButton_Language")],                        
        ])   

        return self.base
    
    def home_button(self):
        self.base = InlineKeyboardMarkup(row_width=2, inline_keyboard=[                        
            [InlineKeyboardButton(text=l('home', self.lang), callback_data="OnButton_Exit")],            
        ])

        return self.base

    def request_question(self, stage):
        if stage > 1:
            self.base = InlineKeyboardMarkup(row_width=2, inline_keyboard=[                        
                [InlineKeyboardButton(text=l('q_got_answers' if stage > 1 else 'home', self.lang), callback_data="OnButton_Exit")]])

        else:            
            self.base = InlineKeyboardMarkup(row_width=2, inline_keyboard=[                        
                [InlineKeyboardButton(text=l('q_got_answers' if stage > 1 else 'home', self.lang), callback_data="OnButton_Exit"), 
                InlineKeyboardButton(text=l('add_question' if stage > 1 else 'req_question', self.lang), callback_data=f"OnButton_Question_{stage}")],            
            ])

        return self.base