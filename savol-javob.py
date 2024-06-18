def savol_javob():    
    import random
    print('***Qabrda so\'raladigan savollar chat boti.***')
    print('Shartlar: to\'xtatish uchun q ni bosing.\nTo\'g\'ri javobni kiriting.')
    source= {
        'Robbing kim?':'Robbimiz Alloh',
        'Dining qaysi?':'Dinim Islom!',
        'Payg\'ambaring kim?':'Payg\'ambarim Muhammad (S.A.V)!',
        'Kitobing qaysi?':'Kitobim Qur\'oni Karim!',
        'Tilaging nima?':'Tilagim Iymon!',
        'Qiblang qaysi?':'Qiblam Ka\'batulloh!',
        'Millating qaysi?':'Ibrohim Xalilulloh millati!',
        'Mazhabing qaysi?':'Imomi A\'zam Abu Xanifa mazhabi!',
        'Do\'stlaring kim?':'Do\'stlarim chohor yorlar!',
        'Chohor yorlar kim?':'Abu Bakr Siddiq,Xazrati Umar,Xazrati Usmon,Xazrati Alidir!',
        'Qachondan beri musulmonsan?':'Al\'-Misoqdan beri!',
        'Al\'-Misoq nima?':'Alloh taola ruhimizni yaratib ulardan Vada olgan kun!',
        'E\'tiqoding qaysi?':'Ahli Sunnat val Jamoat etiqodi!',
        'Kimni yaxshi ko\'rasan?':'Alloh taolani!',
        'Allah\' dan keyin kimni yaxshi ko\'rasan?':'Payg\'ambarimiz Muhammad (S.A.V) ni!',
        'Payg\'ambarimizdan keyin kimni yaxshi ko\'rasan?':'Ota-onamni!',
        'Ota- onadan keyin kimni yaxshi ko\'rasan?':'Barcha mo\'minlarni!',
        'Seni kim yaratgan?':'Alloh taolo!',
        'Nima uchun yaratgan?':'O\'ziga ibodat qilish uchun!',
        'Ibodat degani nima?':'Ibodat Allohning aytganlari!',
        'Iymon kalimasini ayt!':'La ilaha ilalloh Muhammadur Rasulolloh!',
        'Ma\'nosi nima?':'Allohdan o\'zga iloh yo\'q va Muhammad (S.A.V) uning Elchisi ekanligiga Guvohlik beraman!'

    }
    keys_list= list(source.keys())
    score=0
    while True:
        question= random.choice(keys_list)
        print(f'Savol: {question}')
        answer= input(f'''{question}: ''')
        # if answer=='q':
        #     answer=answer.title()
        print(f'''Sizning javobingiz: {answer}''')
        if answer=='q':
            print(f'Savol-javobni to\'xtatdingiz. Yig\'ilgan ball:{score}.')
            break
        elif answer in source[question]: # or answer==source[question]:
            score+=1
            print(f'Javobingiz to\'g\'ri. Sizning ballingiz:{score}.\nJavob: {source[question]}')
        else:
            print(f'To\'g\'ri javobni kiritmadingiz. Qaytadan urining. Yig\'ilgan ball:{score}.\nJavob: {source[question]}')
