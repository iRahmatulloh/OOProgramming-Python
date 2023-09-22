class Foiz:
    def __init__(self, x : int, y : int):
        self.__x = x
        self.__y = y
        

    def __foiz_hisobi(self):
        return (self.__x * self.__y) / 100

    def getFoiz(self):
        return f'{self.__x}ning {self.__y} foizi : {self.__foiz_hisobi()}'


    def setFoiz(self, y):
        self.__y = y


a = Foiz(571, 12)
a.setFoiz(27)
print(a.setFoiz(21))
print(a.getFoiz())
# 