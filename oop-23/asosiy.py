class Inson:
    qari = '1443'
    def __init__(self, ism, yosh, jinsi, qavm, shajara):
        self.ism = ism
        self.yosh = yosh
        self.__jins = jinsi
        self.qavm = qavm
        self.shajara = shajara

    
    def yoshi(self):
        print(f"{self.ism}ning yoshi {self.yosh}da")

    
    def turi(self, gavdalanish):
        print(f"{self.ism} {self.__jins}lardan! va {gavdalanish} holda")


    @staticmethod
    def stat():
        print('hello hammaga')

    @classmethod
    def clacc(cls):
        print('hello malekum')

usmon = Inson('Usmon', 19, 'erkak', 'o`g`uz', 'Ertug`rul')
usmon.turi('ko`rkam')
# print(usmon._Inson__jins)

usmon.stat()
usmon.clacc()