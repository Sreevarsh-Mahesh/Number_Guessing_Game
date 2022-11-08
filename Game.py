# guess no. game
from random import randint
while True:
    print('The game begins!!')
    pick_mode=input('Enter difficulty (easy,hard,hell):  ').lower()
    if pick_mode=='easy' or pick_mode=='e' or pick_mode=='ez' or pick_mode=='esy':
        n=randint(5,15)
    elif pick_mode=='hard' or pick_mode=='h':
        n=randint(5,50)
    elif pick_mode=='hell' :
        n=randint(5,150)
    else:       #to ensure default pick is easy 
        n=randint(5,15)
    
#players guesses
        
    for i in range(1,6):
        guess=int(input('Enter the guess here : '))
        if guess==n:
            print(f'Congrats you won in {i} attempts')
            break
        else:
            if guess <= n-2 or guess <= n+2:
                print(f'hot , you have {5-i} lives left!')
            elif guess <= n-4 or guess <= n+4:
                print(f'cold, you have {5-i} lives left!')
            else:
                print(f'very cold , you have {5-i} lives left!')
    else:
        print('Game Over !!')

    play_again=input('Do you wanna play again ? (y/n) : ').lower()
    if play_again=='y' or play_again=='yes' or play_again=='yeah' or play_again=='ye' or play_again=='yh':
        continue
    else:
        print('Thank you for playing!')
        break
        
