#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' {} |'.format(board[7]),end="")
    print(' {} |'.format(board[8]),end="")
    print(' {} '.format(board[9]))
    print('-----------')
    print(' {} |'.format(board[4]),end="")
    print(' {} |'.format(board[5]),end="")
    print(' {} '.format(board[6]))
    print('-----------')
    print(' {} |'.format(board[1]),end="")
    print(' {} |'.format(board[2]),end="")
    print(' {} '.format(board[3]))


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[3]:


def player_input():
    while True:
        ch=input("Player 1 choose your marker 'X or 'O' : ")
        if(ch not in ('X','O')):
            print("Enter valid input!")
            continue
        break
    play1=ch
    if(play1=='X'):
        play2='O'
    else:
        play2='X'
    return (play1,play2)


# In[4]:


def place_marker(board, marker, position):
    board[position]=marker


# In[5]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[6]:


def win_check(board, mark):
    pos=[(7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1)]
    for (a,b,c) in pos:
        if(board[a]==mark)and(board[b]==mark)and(board[c]==mark):
            return True
    return False


# In[7]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
win_check(test_board,'X')


# In[8]:


import random

def choose_first():
    play=random.randint(1,2)
    print(f"Player {play} will go first")
    return play


# In[9]:


choose_first()


# In[10]:


def space_check(board, position):
    return(board[position]==' ')


# In[11]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[12]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[13]:


def replay():
    while True:
        a=input("Do you want to play again?(Y/N) : ")
        if(a=='Y'):
            return True
        elif(a=='N'):
            return False
        else:
            print("Enter valid input!")
            continue


# In[15]:


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marker={'1':'','2':''}
    (a,b)=player_input()
    marker['1']=a
    marker['2']=b
    winner =0
    first=choose_first()
    display_board(board)
    print("Player {} will go first".format(first))
    ch=input('Ready to play?(Y/N)')
    if(ch=='Y'):
        ch=True
    
    while (ch):
        
        #Player 1 Turn
        if(first==1):
            display_board(board)
            pos=player_choice(board)
            place_marker(board,marker['1'],pos)
            if win_check(board,marker['1']):
                winner=1
                break
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    first=2
            
        # Player2's turn.
        if(first==2):
            display_board(board)
            pos=player_choice(board)
            place_marker(board,marker['2'],pos)
            if win_check(board,marker['2']):
                winner=2
                break
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    first=1
        
    display_board(board)
    if(winner == 1):
        print("Player 1 won! Congratulations!")
    elif(winner == 2):
        print("Player 2 won! Congratulations!")
    else:
        print("The game is draw!")
           
    if not replay():
        break


# In[ ]:




