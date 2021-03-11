
dict1={7:' ', 8:' ', 9:' ',                   #Initailise a dictionery 
       4:' ', 5:' ', 6:' ',
       1:' ', 2:' ', 3:' '}
print('The following is the pattern and the slot number of the game')
print(7,'|',8,'|',9)                          #the user should get the position map
print('--+---+--')
print(4,'|',5,'|',6)    
print('--+---+--')
print(1,'|',2,'|',3)
print()


def display1(turn):                                       #function to display the game after every move
    print(dict1[7],'|',dict1[8],'|',dict1[9])
    print('--+---+--')
    print(dict1[4],'|',dict1[5],'|',dict1[6])
    print('--+---+--')
    print(dict1[1],'|',dict1[2],'|',dict1[3])
    print()
    

def tik():                                               # This is the main game progrm
    turn ="X"
    count = 0
    
    
    for i in range(1,10):
        print('Its your turn ',turn,', move to which place')
        pos =int(input())
        if dict1[pos]==' ':
            dict1[pos]= turn
            count+=1
            print('count is ',count)
            display1(turn)
        else:
            print("The slot is filled try again")
            continue
        if count >=5:
            if dict1[1]==dict1[2]==dict1[3]!=' ': # bottom row 123
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
                
            elif dict1[4]==dict1[5]==dict1[6]!=' ': # middle row 456
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
                
            elif dict1[7]==dict1[8]==dict1[9]!=' ': # top row row 789
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
                
            elif dict1[1]==dict1[5]==dict1[9]!=' ': #left bottom to right top diagonal 159 
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
                
            elif dict1[3]==dict1[5]==dict1[7]!=' ': #right bottom to left top diagonal 357
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
            elif dict1[7]==dict1[4]==dict1[1]!=' ': #right column top to bottom 741
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
            elif dict1[8]==dict1[5]==dict1[2]!=' ': #middle column top to bottom 852
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
            elif dict1[9]==dict1[6]==dict1[3]!=' ': #left column top to bottom  963
                print('Game Over.')
                print()
                print('**** ',turn,' won. ****')
                break
                
                
                
        if count == 9:
            print("It's a tie.")
            
        
        if turn =='X':
            turn ='O'
        else:
            turn ='X'
    print('Do you want to restart \nYes or No???')
    again=input()
    
    if again =='Yes' or again=='yes':
        for keys in dict1:
            dict1[keys]=' '
        tik()
    
        
if __name__=='__main__' :
    
    tik()

    
    
