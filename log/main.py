from datetime import datetime

class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, x, y):
        res = self.func(x, y)
        with open('log.txt', 'a') as file:
            file.write(f'{self.func} funksiya soat: {datetime.now()} da ishladi! \n')
        return res


@logger
def loooper(x, y):
    ls = []
    for i in range(x, y):
        ls.append(i)
    return ls

loooper(1, 2_000_000)



######
######

@logger
class Person:
    def __init__(self) -> None:
        pass


