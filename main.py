import time
import random
import os
from os import system

selText = str("Þú hefur valið:")
selOption = 0
selConfirm = "j"

def main():
    os.system('cls')
    lidur = int(input('Sláðu in númer á lið: '))
    
    if lidur == 1:
        print('-' * 20)
        lidur1()
        input()
    elif lidur == 2:
        print('-' * 20)
        lidur2()
        input()
    elif lidur == 3:
        print('-' * 20)
        lidur3()
        input()
    main()

def lidur1():
    os.system('cls')
    global selText
    global selOption
    global selConfirm
    
    selOption = int(input('\nValkostir:\n 1) LaugardagsLottó\n 2) VíkingaLottó\n\n>>> '))
    lotteryLau = list(range(1, 99))
    
    if selOption == 1:
        selConfirm = input(selText + ' LaugardagsLottó\nEr þetta rétt? (J/N): ')
        if selConfirm.lower() == "j":
            print("\nNúmerin í þessari viku eru:")
            for x in range(5):
                print(random.sample(lotteryLau,1), end=" ", flush=True)
                time.sleep(1)
        else:
            input("Reyndu aftur [ENTER]")
            lidur1()
        print("\n\n Takk fyrir og sjáumst síðar! [ENTER]")
            
    elif selOption == 2:
        selConfirm = input(selText + ' VíkingaLottó\nEr þetta rétt? (J/N): ')
        if selConfirm.lower() == "j":
            print("\nNúmerin í þessari viku eru:")
            for x in range(6):
                print("[" + str(random.randint(1,100)), end="] ", flush=True)
                time.sleep(1)
            print('Og víkingatalan er [' + str(random.randint(1,10)) + ']')
        else:
            input("Reyndu aftur [ENTER]")
            lidur1()
        input("\n\n Takk fyrir og sjáumst síðar! [ENTER]")
        main()
    else:
        print('Þú hefur sláð inn vitlaust... Reyndu aftur [ENTER]')
        
def lidur2():
    os.system('cls')
    def lidur2_guess():
        selOption = input('Gískaðu töluna! (Talan er ' + str(rightNumber) + ')\n>>> ')
        if selOption == str(rightNumber):
            print('Þú gískaðir rétt... talan var ' + str(rightNumber))
        elif selOption == "q":
            print("\n\n Takk fyrir og sjáumst síðar! [ENTER]")
            main()
        else:
            lidur2_guess()
    
    print('Nú er kominn tími til að spila... Gískaðu töluna!')
    print('Reglurnar eru auðveldar, þú velur tölu á milli 1 og 100')
    print('Ef að þú velur rétta töluna þá vinnur þú!')
    selConfirm = input('Ertu tilbúinn? (J/N): ')
    if selConfirm.lower() == "j":
        rightNumber = random.randint(1,10)
        print('Þá byrjum við! (Sláðu inn \'q\' til þess að hætta)')
        lidur2_guess()
    else:
        print('Reyndu aftur [ENTER]')
        lidur2()
        
def lidur3():
    os.system('cls')
    
    print('Spilum skæri, blað, steinn!')
    selConfirm = input('Vilt þú spila skæri, blað, steinn? (J/N): ')
    
    if selConfirm == "j":
        selOption = input('Skæri, blað eða steinn? ')
        cpuOption = random.choice([1, 2, 3])
        
        if cpuOption == 1:
            print('\nSkæri!')
            if selOption.lower() == "steinn":
                print('Þú vannst!')
            elif selOption.lower() == "skæri":
                print('Jafntefli!')
            else:
                print('Þú tapaðir!')
        
        elif cpuOption == 2:
            print('\nSteinn!')
            if selOption.lower() == "blað":
                print('Þú vannst!')
            elif selOption.lower() == "steinn":
                print('Jafntefli!')
            else:
                print('Þú tapaðir!')
                
        elif cpuOption == 3:
            print('\nBlað!')
            if selOption.lower() == "skæri":
                print('Þú vannst!')
            elif selOption.lower() == "blað":
                print('Jafntefli!')
            else:
                print('Þú tapaðir!')
        
main()
os.system('cls')