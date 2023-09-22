class Inson:
    pupil = 'Fotih'
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def uxla(self):
        print(f'{self.name} uxlamoqda!')

    def tushlik(self, ozuqa):
        print(f'{self.name} {ozuqa} tanovul qilyapti!')

    @classmethod
    def turmoq(cls):
        print(cls.name)

    @staticmethod
    def salom():
        print('Salom every one')

umar = Inson('umar', 16, 'Turon')
# umar.salom()
Inson.turmoq()

    # Public -- ommaviy
class Ravon:
    def __init__(self, name):
        self.name = name

    # Public -- ommaviy
    def ochiq(self, rang):
        print(f'{self.name} {rang}dagi xalq uchun!')

# Fotih = Ravon('model Z', 2023)

# Fotih.ochiq('qora')
# Fotih.ochiq('qizil')
    #Private -- shaxsiy
class Ravnaq:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def _view(self):
        print(f'{self.__color} rangidan')

rashed = Ravnaq('rphone','blue')
# rashed._view()

    #Protected -- mahviy

# print(rashed._Ravnaq__name) 
# print(rashed._Ravnaq__color) 
#   print(rashed._Ravnaq_name) # xato ' _ _ ' 2ta va __initni ichidagi  bilan bir xil bo'lishi zarur.

