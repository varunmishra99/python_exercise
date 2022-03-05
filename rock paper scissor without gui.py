import random

def game (comp,a):
    if comp == a:
        return None
    if comp == 's':
        if a == 'r':
            return False
        else :
            return True
    elif comp == 'p':
        if a == 'r':
            return False
        else:
            return True
    else:
        if a =='p':
            return True
        else:
            return False


rand1= random.randint(1,3)
if rand1 == 1:
    comp ='s'
elif rand1 == 2:
    comp = 'p'
elif rand1 == 3:
    comp = 'r' 

a=''
while (a !='r'  and a !='p' and a !='s'):
    a=input("Enter your choice for rock (r), paper(p), scissor(s):    ")    
    if(a == 'r' or a == 's'or a == 'p'):
        r = game(comp,a)
        if r == True:
                print("You won the game :) Computer choice was:   " + str(comp))
        elif r == False:
                print("You loss the game :( Computer choice was:  " + str(comp))
        else:
            print("The Game tied. Computer coice was " + str(comp))
    else:    
        print("Enter a valid choice")