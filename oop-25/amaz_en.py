from os import system


def categ_en():
    ls = []
    print(" - 1.Automotive\n - 2.Baby\n - 3.Health\n - 4.Books")
    ins_cat = int(input("Choose! -> "))
    dict_mexanika = {
        'phone' :  {
            'Samsung 23 Ultra' : '949.8$'
        },
        'Computer' : {
            'ZenBook 14 Pro' : '1590$'
        },
        'Watch' : {
            'IWatch Ultra' : '599$'
        }
    }

    dict_kitoblar = {
        'scientific' : {
            'Qora ooqush' : '120 ming'
        },
        'religion' : {
            'Siyrat' : '200 ming'
        },
        'mindset' : {
            'Tasodifga aldanganlar' : '75 000 ming'
        }
    }


    while True:
        if ins_cat == 1:

            print('Phone\nComputer\nWatch')
            ind_tks = input('choose ->  ')
            if ind_tks.lower() == 'phone':
                print(dict_mexanika['phone'])
                tel_ask = input('Do you buy? Yes or no:  ')
                if tel_ask.lower() == 'yes' or 'y':
                    ls.append(dict_mexanika['phone'])
                    break
            elif ind_tks.lower() == 'computer':
                print(dict_mexanika['Computer'])
                tel_ask = input('Do you buy? Yes or no:  ')
                if tel_ask.lower() == 'yes' or 'y':
                    ls.append(dict_mexanika['Computer'])
                    break
            elif ind_tks.lower() == 'watch':
                print(dict_mexanika['Watch'])
                tel_ask = input('Do you buy? Yes or no:  ')
                if tel_ask.lower() == 'yes' or 'y':
                    ls.append(dict_mexanika['Watch'])
                    break
            
        elif ins_cat == 2:
            return 'baby-amazon.com'
        elif ins_cat == 3:
            return 'https://www.amazon.com/s?bbn=16225010011&rh=i%3Aspecialty-aps%2Cn%3A%2116225010011%2Cn%3A3777891&ref_=nav_em__nav_desktop_sa_intl_personal_care_0_2_16_7'
        elif ins_cat == 4:
            ask__book = input(' scientific\n Diniy\n Shahsiy rivojlanish\n       -> ')
            if ask__book.lower() == 'scientific':
                print(dict_kitoblar['scientific'])
                tel_ask = input('Do you buy? Yes or no:  ')
                if tel_ask.lower() == 'yes' or 'y':
                    ls.append(dict_kitoblar['scientific'])
                    break

            elif ask__book.lower() == 'religion':
                print(dict_kitoblar['religion'])
                tel_ask = input('Do you buy? Yes or no:  ')
                if tel_ask.lower() == 'yes' or 'y':
                    ls.append(dict_kitoblar['religion'])
                    break

            elif ask__book.lower() == 'mindset':
                print(dict_kitoblar['mindset'])
                tel_ask = input('Do you buy? Yes or no:  ')
                if tel_ask.lower() == 'yes' or 'y':
                    ls.append(dict_kitoblar['mindset'])
                    break
        else:
            system('cls')
            print(categ_en())
