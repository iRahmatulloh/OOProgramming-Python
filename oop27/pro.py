class Bankamat:
    def __init__(self, balans):
        self.balans = balans
        list =[] 

        a = input("Karta raqamingizni kiriting: ") 
        list.append(a) 

    def malumot():
        print('''
        Tilni tanlang:
        1. O'zbek tili
        2. Rus tili
        3. Eng til 
        ''')

        # miqdor = input("Miqdorini kiriting: ")
    def pul_yechish(self, miqdor):
        if self.balans >= miqdor:
           self.balans -= miqdor
           print("Pul yechildi")

        else:
            print("MAblag' yetarli emas")

    def pul_yuklash(self, miqdor):
        self.balans += miqdor 
        print("Pul yuklandi")


a = Bankamat(100)   
print(a.pul_yechish(50))    