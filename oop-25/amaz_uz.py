from os import system


def categ():
    ls = []
    print(" - 1.Mexanika\n - 2.Bolalar uchun\n - 3.Sog'lom hayot uchun\n - 4.Kitoblar")
    ins_cat = int(input("Tanlang! -> "))
    dict_mexanika = {
        'telefon' :  {
            'Samsung 23 Ultra' : '949.8$'
        },
        'komputer' : {
            'ZenBook 14 Pro' : '1590$'
        },
        'soat' : {
            'IWatch Ultra' : '599$'
        }
    }

    dict_kitoblar = {
        'Ilmiy' : {
            'Qora ooqush' : '120 ming'
        },
        'Diniy' : {
            'Siyrat' : '200 ming'
        },
        'shaxsiy rivojlanish' : {
            'Tasodifga aldanganlar' : '75 000 ming'
        }
    }


    while True:
        if ins_cat == 1:

            print('Telefon\nKomputer\nSoat')
            ind_tks = input('Tanlang ->  ')
            if ind_tks.lower() == 'telefon':
                print(dict_mexanika['telefon'])
                tel_ask = input('Harid qilasizmi? Ha yoki yoq:  ')
                if tel_ask.lower() == 'ha' or 'h':
                    ls.append(dict_mexanika['telefon'])
                    break
            elif ind_tks.lower() == 'komputer' or 'kompyuter':
                print(dict_mexanika['komputer'])
                tel_ask = input('Harid qilasizmi? Ha yoki yoq:  ')
                if tel_ask.lower() == 'ha' or 'h':
                    ls.append(dict_mexanika['komputer'])
                    break
            elif ind_tks.lower() == 'soat':
                print(dict_mexanika['soat'])
                tel_ask = input('Harid qilasizmi? Ha yoki yoq:  ')
                if tel_ask.lower() == 'ha' or 'h':
                    ls.append(dict_mexanika['komputer'])
                    break
            
        elif ins_cat == 2:
            return 'baby-amazon.com'
        elif ins_cat == 3:
            return 'https://www.amazon.com/s?bbn=16225010011&rh=i%3Aspecialty-aps%2Cn%3A%2116225010011%2Cn%3A3777891&ref_=nav_em__nav_desktop_sa_intl_personal_care_0_2_16_7'
        elif ins_cat == 4:
            ask__book = input(' Ilmiy\n Diniy\n Shahsiy rivojlanish\n       -> ')
            if ask__book.lower() == 'ilmiy':
                print(dict_kitoblar['Ilmiy'])
                tel_ask = input('Harid qilasizmi? Ha yoki yoq:  ')
                if tel_ask.lower() == 'ha' or 'h':
                    ls.append(dict_kitoblar['Ilmiy'])
                    break
            elif ask__book.lower() == 'diniy':
                print(dict_kitoblar['Diniy'])
                tel_ask = input('Harid qilasizmi? Ha yoki yoq:  ')
                if tel_ask.lower() == 'ha' or 'h':
                    ls.append(dict_kitoblar['Diniy'])
                    break

            elif ask__book.lower() == 'Shahsiy rivojlanish' or 'Shaxsiy rivojlanish':
                print(dict_kitoblar['shaxsiy rivojlanish'])
                tel_ask = input('Harid qilasizmi? Ha yoki yoq:  ')
                if tel_ask.lower() == 'ha' or 'h':
                    ls.append(dict_kitoblar['shaxsiy rivojlanish'])
                    break
        else:
            system('cls')
            print(categ())
