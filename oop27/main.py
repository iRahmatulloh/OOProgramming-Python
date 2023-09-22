# class Dog:
#     color = 'Black'
#
#     @classmethod
#     def run(cls):
#         print(f'Rangi {cls.color}')
#
# bak = Dog()
# bak.run()

'''num_filter degan funksiya yarating va u 1ta argument olsin
Funksiya vazifasi unga berilgan list ichidan raqam bo'lgan ma'lumotlarni yangi listga o'tkazib qaytarish.
Input: num_filter([1, 'apple', 3, 'banana', 5.4, 'orange'])
Output: [1, 3, 5.4]
Input: num_filter([-15, '12', 23.43, '198-bus', 5, 18, 17, 'orange'])
Output: [-15, '12', 23.43, 5, 18, 17]'''


lst = []
def num_filter(ls):
    if len(ls) != 0:
        x = ls[0]
        # print(x)
        if isinstance(x, int):
            print(x)
            lst.append(x)
            # ls.remove(x)
            num_filter(ls[1])
        else:
            num_filter([1,2,3,'a'])

    return lst

print(num_filter([1,2,3,'a']))

def listSum(seq):
    if not seq:
        return 0
    return seq[0] + listSum

# print(listSum([1,3,4,5,6]))