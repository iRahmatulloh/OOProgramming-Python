from os import system
from time import sleep

from amaz_uz import categ
from amaz_en import categ_en


system('cls')
class Amazon:
    basic_page_1 = []
    basic_page_2 = []

    def __init__(self, lang=None, register=None, search=None, cart=None, category=None):
        self.lang = lang
        self.category = category
        self.search = search
        self.cart = cart
        self.__register = register

    @classmethod
    def basic_page_run(cls):
        print(cls.basic_page_1)
        print(cls.basic_page_2)


    def setlang_choise(self):
        lang_ind = input("Boshlang'ich tilni o'zgartiring!: \n-- En \n-- Uz \n   -> ")
        if lang_ind.lower() == 'en':
            self.lang = lang_ind
            return categ_en()
        elif lang_ind.lower() == 'uz':
            self.lang = lang_ind
            return categ()
        else:
            self.lang = lang_ind
            return categ()


    
rashed = Amazon('uz')
rashed.basic_page_run()

rashed.setlang_choise()