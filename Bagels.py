import random

print('you have to guess a 3 digit number.\n' 
          'you have 10 attempts.\n'
          'if you guess correct you win otherwise loss like any other game')

print("but don't worry I've some clues for you\n")
print("1.if you guess one of three digits correct and in right place then it will print 'Fermi'\n")
print("2.but if you guess it in wrong place then it will print 'Pico'\n")
print("3.for completely wrong guess it will print 'Bagels'\n")

    
def bagel():
    num = random.randint(100,1000)
    num = str(num)
    att = 0
    while(att < 10):
        j = 0
        a = []
        x = input('Enter the number : ')
        if x == num:
            break
        for i in num:
            if(x[j] == i):
                a.append('Fermi')
            elif(x[j] in num):
                a.append('Pico')
            j = j + 1
        if len(a) == 0:
           print('Bagels')
        else:
           a.sort()
           return ' '.join(a)
        att = att + 1
    if att == 10:
        print('oops! no more attempts\n')
        print('The number was : ', num)
    else:
        print('The number was : ', num)
    print('\n')
    print('wanna play again??\n')
    YourTake = input('press yes or no : ')
    if(YourTake == 'yes'):
        bagel()
    else:
        print('Thanks for playing.')
         
bagel()